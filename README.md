<<<<<<< HEAD
# SkillSwap Hub - Skill Exchange Platform

A modern, responsive full-stack web application where users can share and explore different skills. Built with Flask, MongoDB, Bootstrap 5, and vanilla JavaScript.

## 🌟 Features

### ✅ Authentication & Security
- User signup and registration
- Secure login with password hashing
- Session management
- Logout functionality
- Flash messages for user feedback

### 💼 Skill Management
- Create skill posts
- Read/Display all skills with pagination
- Update existing skill posts
- Delete skill posts
- Skill categories
- Timestamps for creation and updates

### 🔍 Search & Filter
- Search skills by title, description, or keywords
- Filter by category
- Real-time search results

### 👥 User Dashboard
- View personal skill posts
- Edit skills
- Delete skills
- Quick statistics (total skills, likes, connections)
- User profile information

### 📱 Responsive Design
- Mobile-first responsive layout
- Desktop, tablet, and mobile optimized
- Bootstrap 5 grid system
- Smooth animations and transitions

### 🎨 Modern UI
- Gradient navbar
- Hero section
- Skill cards with hover effects
- Beautiful icons
- Professional color scheme
- Footer with social links

## 🛠 Tech Stack

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with animations
- **Bootstrap 5** - Responsive framework
- **JavaScript** - Client-side interactions
- **Font Awesome Icons** - Beautiful icons

### Backend
- **Python 3.8+** - Server language
- **Flask 2.3.2** - Web framework
- **PyMongo 4.4.1** - MongoDB driver

### Database
- **MongoDB** - NoSQL database (localhost)
- **Database Name**: skillswap_hub
- **Collections**: users, skills

## 📋 Project Structure

```
SkillSwap Hub/
│
├── app.py                          # Main Flask application
├── database.py                     # Database operations
├── requirements.txt                # Python dependencies
├── .env                           # Environment variables
│
├── templates/                      # Jinja2 templates
│   ├── base.html                  # Base template with navbar/footer
│   ├── index.html                 # Home page
│   ├── signup.html                # Registration page
│   ├── login.html                 # Login page
│   ├── dashboard.html             # User dashboard
│   ├── create_skill.html          # Create skill form
│   ├── edit_skill.html            # Edit skill form
│   ├── search_results.html        # Search results page
│   ├── 404.html                   # 404 error page
│   └── 500.html                   # 500 error page
│
├── static/                         # Static files
│   ├── css/
│   │   └── style.css              # Main stylesheet
│   ├── js/
│   │   └── main.js                # Main JavaScript file
│   └── images/                     # Image assets
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- MongoDB running on localhost:27017
- pip (Python package manager)
- Git (optional)

### Installation Steps

#### 1. Clone or Download the Project
```bash
cd "c:\Users\haroon traders\OneDrive\Desktop\SkillSwap Hub"
```

#### 2. Create a Virtual Environment (Recommended)

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Configure Environment Variables

The `.env` file is already set up with default values:
```
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your_secret_key_here_change_this_in_production
MONGO_URI=mongodb://localhost:27017/
MONGO_DB=skillswap_hub
```

**Important**: For production, change the `SECRET_KEY` to a secure random string.

#### 5. Ensure MongoDB is Running

Make sure MongoDB is running on localhost:27017:

**Windows (using MongoDB Community):**
```bash
mongod
```

**Or if MongoDB is installed as a service:**
```bash
net start MongoDB
```

**macOS (using Homebrew):**
```bash
brew services start mongodb-community
```

**Verify MongoDB is running:**
```bash
mongo
# or
mongosh
```

#### 6. Run the Application

**Windows (PowerShell):**
```powershell
python app.py
```

**Windows (Command Prompt):**
```cmd
python app.py
```

**macOS/Linux:**
```bash
python3 app.py
```

The application will start at: **http://localhost:5000**

## 📖 Usage Guide

### 1. Home Page
- View featured skills
- See platform statistics
- Learn how SkillSwap Hub works
- Sign up or login

### 2. Sign Up
- Create a new account with name, email, and password
- Password must be at least 6 characters
- Confirm password must match

### 3. Login
- Enter your email and password
- Session will be created and stored

### 4. Dashboard
- View all your posted skills
- See your statistics
- Edit or delete your skills
- Create new skill posts

### 5. Create Skill Post
- Fill in the skill title (3-100 characters)
- Select a category
- Write a detailed description (10-2000 characters)
- Post the skill

### 6. Edit Skill
- Navigate to your dashboard
- Click the "Edit" button on your skill
- Modify the details
- Save changes

### 7. Delete Skill
- Navigate to your dashboard
- Click the "Delete" button
- Confirm deletion

### 8. Search & Browse
- Use the search bar to find skills by keyword
- Filter by category
- View all skills from the community
- Click on skills to view details

### 9. Logout
- Click on your user profile dropdown
- Select Logout

## 🗄️ Database Schema

### Users Collection
```json
{
  "_id": ObjectId,
  "name": "John Doe",
  "email": "john@example.com",
  "password": "hashed_password_here",
  "created_at": ISODate("2026-05-25T10:00:00Z")
}
```

### Skills Collection
```json
{
  "_id": ObjectId,
  "title": "Web Development",
  "description": "Learn modern web development...",
  "category": "Web Development",
  "user_id": ObjectId("..."),
  "user_name": "John Doe",
  "created_at": ISODate("2026-05-25T10:00:00Z"),
  "updated_at": ISODate("2026-05-25T10:00:00Z")
}
```

## 🔑 API Endpoints

### Authentication Routes
- `GET /signup` - Sign up page
- `POST /signup` - Register new user
- `GET /login` - Login page
- `POST /login` - Authenticate user
- `GET /logout` - Logout user

### Skill Routes
- `GET /create_skill` - Create skill form
- `POST /create_skill` - Submit new skill
- `GET /edit_skill/<skill_id>` - Edit skill form
- `POST /edit_skill/<skill_id>` - Update skill
- `POST /delete_skill/<skill_id>` - Delete skill

### Dashboard & Search
- `GET /dashboard` - User dashboard
- `GET /search` - Search page
- `GET /category/<category>` - Filter by category

### API Endpoints
- `GET /api/skills` - Get all skills (JSON)

## 🎨 Customization

### Change Colors
Edit `static/css/style.css`:
```css
:root {
    --primary-color: #4f46e5;      /* Change this */
    --secondary-color: #7c3aed;    /* And this */
    --success-color: #10b981;
    /* ... etc */
}
```

### Add More Categories
Edit `app.py` and update the categories list:
```python
categories = [
    'Programming', 'Web Development', ...
    'Your New Category'  # Add here
]
```

### Modify Navbar
Edit `templates/base.html` to customize the navigation

## 🐛 Troubleshooting

### Issue: "MongoDB Connection Error"
**Solution**: Make sure MongoDB is running on localhost:27017
```bash
mongod
```

### Issue: "ModuleNotFoundError"
**Solution**: Install dependencies again
```bash
pip install -r requirements.txt
```

### Issue: Port 5000 Already in Use
**Solution**: Either stop the other process or run Flask on a different port:
```bash
python -c "from app import app; app.run(port=5001)"
```

### Issue: CORS Errors
**Solution**: The app is configured for localhost. For production, update the CORS settings in `app.py`

### Issue: Session Not Persisting
**Solution**: Make sure `SECRET_KEY` is set in `.env` and MongoDB is running

## 📚 File Descriptions

### `app.py`
- Main Flask application
- Contains all routes
- User authentication logic
- Error handlers

### `database.py`
- MongoDB connection
- Database operations class
- CRUD methods for users and skills
- Search functionality

### `requirements.txt`
- Python package dependencies
- Flask, PyMongo, python-dotenv, Werkzeug

### `templates/base.html`
- Main layout template
- Navigation bar
- Footer
- Flash messages
- Responsive grid

### `templates/index.html`
- Home page
- Hero section
- Feature showcase
- Call to action

### `templates/signup.html` & `login.html`
- Authentication forms
- Form validation
- User guidance

### `templates/dashboard.html`
- User's personal dashboard
- Skill management
- Statistics display
- Quick actions

### `templates/create_skill.html` & `edit_skill.html`
- Skill creation/editing forms
- Category selection
- Form validation tips

### `templates/search_results.html`
- Search interface
- Results display
- Category filtering

### `static/css/style.css`
- Complete styling
- Responsive design
- Animations and transitions
- Theme customization

### `static/js/main.js`
- Client-side validations
- Form handling
- Animations
- Utility functions
- API calls

## 🔐 Security Notes

1. **Password Hashing**: Passwords are hashed using Werkzeug's security utilities
2. **Session Management**: Flask sessions are used for user authentication
3. **CSRF Protection**: Can be added with Flask-WTF (not included in basic version)
4. **Change SECRET_KEY**: Always change the SECRET_KEY in `.env` for production
5. **HTTPS**: Use HTTPS in production

## 🚀 Deployment

### Heroku Deployment
1. Create a `Procfile`: `web: gunicorn app:app`
2. Create `runtime.txt`: `python-3.9.7`
3. Install gunicorn: `pip install gunicorn`
4. Deploy to Heroku

### Local Network Access
To access from other devices on your network:
```bash
python -c "from app import app; app.run(host='0.0.0.0', port=5000)"
```

Then access via: `http://your-computer-ip:5000`

## 📊 Testing

### Test Credentials (if added to database)
- Email: test@example.com
- Password: password123

### Manual Testing Checklist
- [ ] Signup with new user
- [ ] Login with credentials
- [ ] Create a skill
- [ ] Edit the skill
- [ ] Search for the skill
- [ ] Filter by category
- [ ] Delete the skill
- [ ] Logout
- [ ] Test on mobile view
- [ ] Test all form validations

## 🎯 Future Enhancements

- [ ] User profiles with images
- [ ] Like/rating system for skills
- [ ] Direct messaging between users
- [ ] Skill ratings and reviews
- [ ] Advanced search with filters
- [ ] Dark mode toggle
- [ ] Email verification
- [ ] Password reset functionality
- [ ] Two-factor authentication
- [ ] Skill recommendations
- [ ] User notifications
- [ ] Skill completion tracking
- [ ] Certificate generation

## 📞 Support

For issues or questions:
1. Check the Troubleshooting section
2. Verify MongoDB is running
3. Check that all files are in correct directories
4. Ensure Python dependencies are installed

## 📄 License

This project is open source and available for educational purposes.

## 👨‍💻 Development

Built with ❤️ as a modern skill exchange platform.

---

**Version**: 1.0.0  
**Last Updated**: May 25, 2026  
**Status**: Production Ready ✅

## 📞 Quick Start Commands

```bash
# Activate virtual environment (Windows)
.\venv\Scripts\Activate.ps1

# Activate virtual environment (macOS/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run MongoDB (Windows)
mongod

# Run MongoDB (macOS with Homebrew)
brew services start mongodb-community

# Run the Flask app
python app.py

# Access the app
# Open browser and go to: http://localhost:5000
```

Enjoy using SkillSwap Hub! 🎉
=======
# SkillSwap_Hub
A modern full-stack web application for skill sharing and collaboration, built with Flask and MongoDB, featuring secure user authentication, skill posting, search, filtering, and dashboard management
>>>>>>> acb1ebadad27698ff68e7ff6f04750910aeaa716

