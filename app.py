"""
SkillSwap Hub - Main Flask Application
Skill Exchange Platform
"""
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from dotenv import load_dotenv
import os
from database import Database
from bson.objectid import ObjectId
from datetime import datetime

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')

# Helper function to check if user is logged in
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please login first.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


# ==================== HOME ROUTES ====================

@app.route('/')
def index():
    """Home page with featured skills"""
    try:
        all_skills = Database.get_all_skills()
        # Get recent skills (limit to 6)
        recent_skills = all_skills[:6]
        total_skills = len(all_skills)
        total_users = Database.users_collection.count_documents({})
        
        return render_template('index.html', 
                             skills=recent_skills,
                             total_skills=total_skills,
                             total_users=total_users)
    except Exception as e:
        flash(f'Error loading home page: {e}', 'danger')
        return render_template('index.html', skills=[], total_skills=0, total_users=0)


# ==================== AUTHENTICATION ROUTES ====================

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """User signup page"""
    if request.method == 'POST':
        try:
            name = request.form.get('name', '').strip()
            email = request.form.get('email', '').strip()
            password = request.form.get('password', '').strip()
            confirm_password = request.form.get('confirm_password', '').strip()

            # Validation
            if not name or not email or not password:
                flash('All fields are required.', 'warning')
                return redirect(url_for('signup'))

            if len(password) < 6:
                flash('Password must be at least 6 characters long.', 'warning')
                return redirect(url_for('signup'))

            if password != confirm_password:
                flash('Passwords do not match.', 'warning')
                return redirect(url_for('signup'))

            # Check if user already exists
            existing_user = Database.get_user_by_email(email)
            if existing_user:
                flash('Email already registered. Please login.', 'warning')
                return redirect(url_for('login'))

            # Hash password and create user
            password_hash = generate_password_hash(password)
            user_id = Database.add_user(name, email, password_hash)

            if user_id:
                flash('Account created successfully! Please login.', 'success')
                return redirect(url_for('login'))
            else:
                flash('Error creating account. Please try again.', 'danger')
                return redirect(url_for('signup'))

        except Exception as e:
            flash(f'Signup error: {e}', 'danger')
            return redirect(url_for('signup'))

    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login page"""
    if request.method == 'POST':
        try:
            email = request.form.get('email', '').strip()
            password = request.form.get('password', '').strip()

            if not email or not password:
                flash('Email and password are required.', 'warning')
                return redirect(url_for('login'))

            # Get user from database
            user = Database.get_user_by_email(email)
            if not user:
                flash('Invalid email or password.', 'danger')
                return redirect(url_for('login'))

            # Check password
            if not check_password_hash(user['password'], password):
                flash('Invalid email or password.', 'danger')
                return redirect(url_for('login'))

            # Set session
            session['user_id'] = str(user['_id'])
            session['user_name'] = user['name']
            session['user_email'] = user['email']
            flash(f"Welcome back, {user['name']}!", 'success')
            return redirect(url_for('dashboard'))

        except Exception as e:
            flash(f'Login error: {e}', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    """Logout user"""
    session.clear()
    flash('You have been logged out successfully.', 'success')
    return redirect(url_for('index'))


# ==================== DASHBOARD ROUTES ====================

@app.route('/dashboard')
@login_required
def dashboard():
    """User dashboard"""
    try:
        user_id = session.get('user_id')
        user_name = session.get('user_name')
        
        # Get user's skills
        user_skills = Database.get_user_skills(user_id)
        
        return render_template('dashboard.html', 
                             user_name=user_name,
                             skills=user_skills,
                             total_skills=len(user_skills))
    except Exception as e:
        flash(f'Error loading dashboard: {e}', 'danger')
        return redirect(url_for('index'))


# ==================== SKILL MANAGEMENT ROUTES ====================

@app.route('/create_skill', methods=['GET', 'POST'])
@login_required
def create_skill():
    """Create a new skill post"""
    if request.method == 'POST':
        try:
            title = request.form.get('title', '').strip()
            description = request.form.get('description', '').strip()
            category = request.form.get('category', '').strip()

            # Validation
            if not title or not description or not category:
                flash('All fields are required.', 'warning')
                return redirect(url_for('create_skill'))

            if len(title) < 3:
                flash('Title must be at least 3 characters long.', 'warning')
                return redirect(url_for('create_skill'))

            if len(description) < 10:
                flash('Description must be at least 10 characters long.', 'warning')
                return redirect(url_for('create_skill'))

            # Create skill
            user_id = session.get('user_id')
            user_name = session.get('user_name')
            
            skill_id = Database.create_skill(title, description, category, user_id, user_name)

            if skill_id:
                flash('Skill post created successfully!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Error creating skill post.', 'danger')
                return redirect(url_for('create_skill'))

        except Exception as e:
            flash(f'Error creating skill: {e}', 'danger')
            return redirect(url_for('create_skill'))

    categories = [
        'Programming', 'Web Development', 'Mobile Development', 'Data Science',
        'Design', 'Writing', 'Music', 'Languages', 'Business', 'Marketing',
        'Photography', 'Video Editing', 'Other'
    ]
    return render_template('create_skill.html', categories=categories)


@app.route('/edit_skill/<skill_id>', methods=['GET', 'POST'])
@login_required
def edit_skill(skill_id):
    """Edit a skill post"""
    try:
        skill = Database.get_skill_by_id(skill_id)
        
        if not skill:
            flash('Skill not found.', 'danger')
            return redirect(url_for('dashboard'))

        # Check if user owns the skill
        if str(skill['user_id']) != session.get('user_id'):
            flash('You do not have permission to edit this skill.', 'danger')
            return redirect(url_for('dashboard'))

        if request.method == 'POST':
            title = request.form.get('title', '').strip()
            description = request.form.get('description', '').strip()
            category = request.form.get('category', '').strip()

            # Validation
            if not title or not description or not category:
                flash('All fields are required.', 'warning')
                return redirect(url_for('edit_skill', skill_id=skill_id))

            if len(title) < 3:
                flash('Title must be at least 3 characters long.', 'warning')
                return redirect(url_for('edit_skill', skill_id=skill_id))

            if len(description) < 10:
                flash('Description must be at least 10 characters long.', 'warning')
                return redirect(url_for('edit_skill', skill_id=skill_id))

            # Update skill
            success = Database.update_skill(skill_id, title, description, category)

            if success:
                flash('Skill post updated successfully!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Error updating skill post.', 'danger')
                return redirect(url_for('edit_skill', skill_id=skill_id))

        categories = [
            'Programming', 'Web Development', 'Mobile Development', 'Data Science',
            'Design', 'Writing', 'Music', 'Languages', 'Business', 'Marketing',
            'Photography', 'Video Editing', 'Other'
        ]
        return render_template('edit_skill.html', skill=skill, categories=categories)

    except Exception as e:
        flash(f'Error editing skill: {e}', 'danger')
        return redirect(url_for('dashboard'))


@app.route('/delete_skill/<skill_id>', methods=['POST'])
@login_required
def delete_skill(skill_id):
    """Delete a skill post"""
    try:
        skill = Database.get_skill_by_id(skill_id)
        
        if not skill:
            flash('Skill not found.', 'danger')
            return redirect(url_for('dashboard'))

        # Check if user owns the skill
        if str(skill['user_id']) != session.get('user_id'):
            flash('You do not have permission to delete this skill.', 'danger')
            return redirect(url_for('dashboard'))

        # Delete skill
        success = Database.delete_skill(skill_id)

        if success:
            flash('Skill post deleted successfully!', 'success')
        else:
            flash('Error deleting skill post.', 'danger')

        return redirect(url_for('dashboard'))

    except Exception as e:
        flash(f'Error deleting skill: {e}', 'danger')
        return redirect(url_for('dashboard'))


# ==================== SEARCH & FILTER ROUTES ====================

@app.route('/search')
def search():
    """Search for skills"""
    try:
        query = request.args.get('q', '').strip()
        category = request.args.get('category', '').strip()

        skills = []
        
        if query:
            skills = Database.search_skills(query)
        elif category:
            skills = Database.get_skills_by_category(category)
        else:
            skills = Database.get_all_skills()

        categories = [
            'Programming', 'Web Development', 'Mobile Development', 'Data Science',
            'Design', 'Writing', 'Music', 'Languages', 'Business', 'Marketing',
            'Photography', 'Video Editing', 'Other'
        ]

        return render_template('search_results.html', 
                             skills=skills, 
                             query=query,
                             category=category,
                             categories=categories)

    except Exception as e:
        flash(f'Error searching skills: {e}', 'danger')
        return redirect(url_for('index'))


@app.route('/category/<category>')
def filter_by_category(category):
    """Filter skills by category"""
    try:
        skills = Database.get_skills_by_category(category)
        
        categories = [
            'Programming', 'Web Development', 'Mobile Development', 'Data Science',
            'Design', 'Writing', 'Music', 'Languages', 'Business', 'Marketing',
            'Photography', 'Video Editing', 'Other'
        ]

        return render_template('search_results.html',
                             skills=skills,
                             category=category,
                             categories=categories)

    except Exception as e:
        flash(f'Error loading category: {e}', 'danger')
        return redirect(url_for('index'))


# ==================== API ROUTES ====================

@app.route('/api/skills')
def api_get_skills():
    """API endpoint to get all skills"""
    try:
        skills = Database.get_all_skills()
        # Convert ObjectId to string for JSON serialization
        for skill in skills:
            skill['_id'] = str(skill['_id'])
            skill['user_id'] = str(skill['user_id'])
            skill['created_at'] = skill['created_at'].isoformat()
            skill['updated_at'] = skill['updated_at'].isoformat()
        return jsonify(skills)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors"""
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return render_template('500.html'), 500


# ==================== CONTEXT PROCESSORS ====================

@app.context_processor
def inject_user():
    """Inject user data into template context"""
    return dict(
        logged_in='user_id' in session,
        user_name=session.get('user_name', ''),
        user_id=session.get('user_id', '')
    )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
