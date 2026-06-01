# QUICK START GUIDE

## ⚡ 5-Minute Setup

### Step 1: Open Terminal/PowerShell
Navigate to the project directory:
```powershell
cd "c:\Users\haroon traders\OneDrive\Desktop\SkillSwap Hub"
```

### Step 2: Start MongoDB
Open a new terminal/PowerShell window and run:
```powershell
mongod
```
Leave it running in the background.

### Step 3: Create Virtual Environment
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Step 4: Install Dependencies
```powershell
pip install -r requirements.txt
```

### Step 5: Run Flask App
```powershell
python app.py
```

### Step 6: Open Browser
Go to: **http://localhost:5000**

---

## 🎯 First Time Use

### Create a Test Account
1. Click **"Sign Up"**
2. Fill in:
   - Name: `John Doe`
   - Email: `john@example.com`
   - Password: `password123`
3. Click **"Create Account"**

### Login
1. Click **"Login"**
2. Enter:
   - Email: `john@example.com`
   - Password: `password123`
3. Click **"Login to Account"**

### Create Your First Skill
1. Click **"Share New Skill"** button
2. Fill in:
   - Title: `Web Development`
   - Category: `Web Development`
   - Description: `I can teach you modern web development with HTML, CSS, and JavaScript...`
3. Click **"Post Skill"**

### View Skills
1. Click **"Browse Skills"** in the navbar
2. Search or filter by category
3. See all posted skills

### Edit Your Skill
1. Go to **Dashboard**
2. Click **"Edit"** on your skill
3. Make changes
4. Click **"Save Changes"**

### Delete Your Skill
1. Go to **Dashboard**
2. Click **"Delete"** on your skill
3. Confirm deletion

---

## 🆘 Troubleshooting

### MongoDB Not Starting?
- Make sure MongoDB is installed
- Run `mongod` in a separate terminal/PowerShell
- Check if port 27017 is available

### Port 5000 Already in Use?
```powershell
# Use a different port:
python -c "from app import app; app.run(port=5001)"
# Then access: http://localhost:5001
```

### ModuleNotFoundError?
```powershell
# Reinstall dependencies:
pip install -r requirements.txt
```

### Virtual Environment Issues?
```powershell
# Deactivate and reactivate:
deactivate
.\venv\Scripts\Activate.ps1
```

---

## 📁 Project Structure at a Glance

```
SkillSwap Hub/
├── app.py ............................ Flask application
├── database.py ....................... Database operations
├── requirements.txt .................. Python packages
├── .env .............................. Configuration
├── README.md ......................... Documentation
├── QUICKSTART.md ..................... This file
│
├── templates/ ........................ HTML pages
│   ├── base.html
│   ├── index.html
│   ├── signup.html
│   ├── login.html
│   ├── dashboard.html
│   ├── create_skill.html
│   ├── edit_skill.html
│   └── search_results.html
│
└── static/
    ├── css/
    │   └── style.css ................. Styling
    └── js/
        └── main.js ................... JavaScript
```

---

## 🔗 Important Links

- **Home Page**: http://localhost:5000/
- **Sign Up**: http://localhost:5000/signup
- **Login**: http://localhost:5000/login
- **Dashboard**: http://localhost:5000/dashboard
- **Search**: http://localhost:5000/search
- **API**: http://localhost:5000/api/skills

---

## 🎨 Default Theme

- **Primary Color**: Blue (#4f46e5)
- **Secondary Color**: Purple (#7c3aed)
- **Success Color**: Green (#10b981)
- **Danger Color**: Red (#ef4444)

---

## 📚 Main Features Overview

| Feature | Location | Status |
|---------|----------|--------|
| User Authentication | /signup, /login | ✅ Working |
| Dashboard | /dashboard | ✅ Working |
| Create Skills | /create_skill | ✅ Working |
| Edit Skills | /edit_skill/<id> | ✅ Working |
| Delete Skills | Dashboard | ✅ Working |
| Search Skills | /search | ✅ Working |
| Filter by Category | /category/<name> | ✅ Working |
| Responsive Design | All pages | ✅ Working |
| Mobile Support | All pages | ✅ Working |

---

## ✨ Tips & Tricks

1. **Search Tips**
   - Search by skill title
   - Search by description
   - Filter by category
   - Use multiple keywords

2. **Profile Management**
   - Create meaningful skill titles
   - Write detailed descriptions
   - Choose accurate categories
   - Update regularly

3. **Best Practices**
   - Use clear, descriptive titles
   - Include your experience level
   - Mention what learners will gain
   - Keep descriptions concise but informative

---

## 🚀 Next Steps

After successful setup:
1. Explore the dashboard
2. Create multiple skills
3. Test the search functionality
4. Try different categories
5. Test on mobile browsers
6. Customize colors in CSS if desired

---

## 📞 Need Help?

- Check **README.md** for detailed documentation
- Review **Troubleshooting** section above
- Verify MongoDB is running
- Check terminal for error messages
- Ensure all files are in the correct directory

---

## 🎉 You're All Set!

Your SkillSwap Hub application is ready to use. Start sharing your skills and connecting with others!

**Happy coding!** ✨
