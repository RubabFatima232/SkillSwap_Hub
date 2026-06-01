# Troubleshooting Guide

## 🆘 Common Issues & Solutions

### MongoDB Connection Issues

#### Problem: "MongoDB Connection Refused"
```
Error: [Errno 111] Connection refused
```

**Solutions**:
1. **Start MongoDB Service**
   ```powershell
   mongod
   ```

2. **Check if MongoDB is installed**
   ```powershell
   mongod --version
   ```

3. **Verify MongoDB is on port 27017**
   ```powershell
   netstat -ano | findstr :27017
   ```

4. **Restart MongoDB service**
   ```powershell
   net stop MongoDB
   net start MongoDB
   ```

---

#### Problem: "Address already in use [Errno 48]"
```
Error: Address already in use
```

**Solution**: MongoDB is already running

```powershell
# Check what's using the port
netstat -ano | findstr :27017

# Kill the process
taskkill /PID <PID> /F

# Or just restart
net stop MongoDB
net start MongoDB
```

---

#### Problem: "Authentication failed: 'username' not found"
**Solution**: Create proper credentials or disable authentication

```javascript
// In MongoDB shell:
use skillswap_hub
db.createUser({
  user: "app_user",
  pwd: "password123",
  roles: [{ role: "readWrite", db: "skillswap_hub" }]
})
```

---

### Flask/Python Issues

#### Problem: "ModuleNotFoundError: No module named 'flask'"
```
ModuleNotFoundError: No module named 'flask'
```

**Solutions**:
1. **Activate virtual environment**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

2. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Verify installation**
   ```powershell
   pip list
   ```

---

#### Problem: "Port 5000 already in use"
```
OSError: [Errno 48] Address already in use
```

**Solutions**:
1. **Use a different port**
   ```python
   # In app.py, change:
   app.run(port=5001)
   
   # Or from command line:
   python -c "from app import app; app.run(port=5001)"
   ```

2. **Kill the process using port 5000**
   ```powershell
   netstat -ano | findstr :5000
   taskkill /PID <PID> /F
   ```

3. **Find what's using the port**
   ```powershell
   lsof -i :5000  # macOS/Linux
   ```

---

#### Problem: "SyntaxError: invalid syntax"
**Solution**: Check Python version is 3.8+

```powershell
python --version
```

Update Python if needed and reinstall dependencies.

---

### Virtual Environment Issues

#### Problem: "Cannot find venv folder"
**Solution**: Create it again

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

#### Problem: Virtual environment won't activate
**Solution**: Check path and permissions

```powershell
# Check current directory
Get-Location

# Navigate to correct folder
cd "c:\Users\haroon traders\OneDrive\Desktop\SkillSwap Hub"

# Try activation
.\venv\Scripts\Activate.ps1

# If it fails, try:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\Activate.ps1
```

---

### Form & Validation Issues

#### Problem: "Form validation failing"
**Solution**: Check browser console and server logs

1. Open **Developer Tools** (F12)
2. Check **Console** tab for errors
3. Check **Network** tab for failed requests
4. Check **terminal** for Flask errors

---

#### Problem: "Password validation not working"
**Solution**: Verify requirements are met

- Minimum 6 characters
- Passwords must match
- No special character limits
- Case sensitive

---

### Database Issues

#### Problem: "Database not found"
**Solution**: MongoDB will auto-create the database

1. Insert first document:
   ```javascript
   use skillswap_hub
   db.users.insertOne({ test: "data" })
   ```

2. Or just run the app - it auto-creates on first use

---

#### Problem: "Collection missing"
**Solution**: App auto-creates collections. If not:

```javascript
db.createCollection("users")
db.createCollection("skills")
```

---

#### Problem: "Index errors"
**Solution**: Drop and recreate indexes

```javascript
db.users.dropIndexes()
db.skills.dropIndexes()

db.users.createIndex({ email: 1 }, { unique: true })
db.skills.createIndex({ user_id: 1 })
```

---

### Application Issues

#### Problem: "Blank page loading"
**Solutions**:
1. Check browser console for JavaScript errors
2. Clear browser cache (Ctrl+Shift+Delete)
3. Check terminal for Flask errors
4. Verify all template files exist
5. Check static files are loading (F12 > Network)

---

#### Problem: "404 Page not found"
**Solution**: Check the route exists

```python
# Verify route in app.py:
@app.route('/path')
def function():
    pass
```

Common routes:
- `/` - Home
- `/signup` - Sign up
- `/login` - Login
- `/dashboard` - Dashboard
- `/search` - Search

---

#### Problem: "500 Internal Server Error"
**Solutions**:
1. Check terminal for error messages
2. Verify all dependencies installed
3. Check .env file configuration
4. Verify MongoDB connection
5. Check database operations in database.py

---

#### Problem: "Static files not loading (CSS/JS)"
**Solution**: Check file structure

```
static/
├── css/
│   └── style.css     ✅ Must be here
├── js/
│   └── main.js       ✅ Must be here
└── images/
```

If missing, recreate with:
```powershell
mkdir static\css
mkdir static\js
mkdir static\images
```

---

#### Problem: "Flash messages not appearing"
**Solution**: Check message setup

```python
# In app.py, verify:
from flask import flash

# Use it correctly:
flash('Message text', 'success')  # or 'danger', 'warning', 'info'

# In template:
{% for category, message in messages %}
    {{ message }}
{% endfor %}
```

---

### Configuration Issues

#### Problem: ".env file not being loaded"
**Solution**: Verify dotenv setup

```python
# In app.py, check this is at top:
from dotenv import load_dotenv
load_dotenv()
```

Alternatively, export variables:
```powershell
# PowerShell
$env:FLASK_ENV="development"
$env:MONGO_URI="mongodb://localhost:27017/"
```

---

#### Problem: "SECRET_KEY error"
**Solution**: Set a strong SECRET_KEY

```env
# In .env:
SECRET_KEY=your_super_secret_key_here_change_this

# Or generate random:
# Python:
import secrets
secrets.token_hex(32)
```

---

### Network & Connectivity

#### Problem: "Cannot access localhost:5000"
**Solutions**:
1. Make sure Flask is running
2. Check you're using http:// not https://
3. Check firewall settings
4. Try: http://127.0.0.1:5000

---

#### Problem: "Cannot access from other device on network"
**Solution**: Run Flask with 0.0.0.0

```python
app.run(host='0.0.0.0', port=5000)

# Or in terminal:
python -c "from app import app; app.run(host='0.0.0.0')"
```

Then access via: `http://your-computer-ip:5000`

---

### Email/Validation Issues

#### Problem: "Email validation failing"
**Solution**: Check email format

- Must contain @
- Must have domain (.com, .net, etc)
- No spaces allowed
- Example: user@example.com ✅

---

#### Problem: "User already exists"
**Solution**: Use different email or delete user

```javascript
// In MongoDB:
db.users.deleteOne({ email: "test@example.com" })
```

---

### Performance Issues

#### Problem: "Slow database queries"
**Solution**: Check indexes

```javascript
db.users.getIndexes()
db.skills.getIndexes()

// Should see email and user_id indexes
```

---

#### Problem: "Page loading slowly"
**Solutions**:
1. Check MongoDB is running and responsive
2. Verify no blocking operations
3. Check network in browser DevTools
4. Try incognito/private mode (fresh cache)

---

### Security Issues

#### Problem: "Password hash errors"
**Solution**: Verify Werkzeug is installed

```powershell
pip install Werkzeug==2.3.6
```

---

#### Problem: "Session not saving"
**Solution**: Check SECRET_KEY is set

```python
# In app.py:
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# In .env:
SECRET_KEY=your_secret_here
```

---

### Browser Issues

#### Problem: "CSS not styling correctly"
**Solutions**:
1. Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
2. Clear browser cache
3. Check DevTools for 404 on style.css
4. Verify style.css exists in static/css/

---

#### Problem: "JavaScript not working"
**Solutions**:
1. Check console (F12) for errors
2. Verify main.js loads (check Network tab)
3. Check for syntax errors in JavaScript
4. Try in different browser

---

#### Problem: "Forms not submitting"
**Solutions**:
1. Check form has `name` attributes
2. Verify method is POST
3. Check action URL
4. Verify button is type="submit"
5. Check browser console for JS errors

---

## 🔍 Debugging Tips

### Enable Debug Mode
```python
# In app.py:
app.run(debug=True)

# Or in .env:
FLASK_DEBUG=True
```

### Check Server Logs
Look at terminal output when running Flask

```
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
 * Restarting with reloader
```

### Browser Developer Tools
- **Console**: JavaScript errors
- **Network**: Failed requests/resources
- **Elements**: HTML structure
- **Sources**: JavaScript debugging

### Python Debugging
```python
# Add debug prints:
print(f"User: {user}")
print(f"Skills: {skills}")

# Or use debugging:
import pdb; pdb.set_trace()
```

---

## 📋 Diagnostic Checklist

Before asking for help, verify:

- [ ] Python 3.8+ installed: `python --version`
- [ ] Virtual environment activated: Check prompt
- [ ] MongoDB running: `mongo` or `mongosh` works
- [ ] Dependencies installed: `pip list` shows Flask, PyMongo
- [ ] .env file exists: Check current directory
- [ ] app.py exists and readable
- [ ] templates/ folder exists with 10 files
- [ ] static/ folder exists with css/ and js/
- [ ] Flask starts: `python app.py` shows no errors
- [ ] Port 5000 accessible: http://localhost:5000
- [ ] Can sign up and login
- [ ] Can create a skill

---

## 🚀 Reset Everything

If things get too complicated, start fresh:

```powershell
# 1. Deactivate environment
deactivate

# 2. Remove venv (optional)
Remove-Item -Recurse venv

# 3. Remove __pycache__ (optional)
Remove-Item -Recurse -Include "__pycache__" -Force

# 4. Create fresh environment
python -m venv venv

# 5. Activate
.\venv\Scripts\Activate.ps1

# 6. Reinstall dependencies
pip install -r requirements.txt

# 7. Clear MongoDB (optional)
mongosh
# Then: db.dropDatabase()

# 8. Run again
python app.py
```

---

## 📞 Getting Help

1. **Check this file first** - Most issues covered here
2. **Check README.md** - Full documentation
3. **Check QUICKSTART.md** - Quick reference
4. **Check browser console** - JavaScript errors
5. **Check terminal output** - Flask/Python errors
6. **Check MongoDB connection** - Run `mongosh`

---

## 📝 Error Log Template

When reporting issues:

```
Error Message: [copy exact error]
Steps to Reproduce: [1. 2. 3.]
Environment:
- OS: Windows/Mac/Linux
- Python Version: [output of python --version]
- Flask Running: Yes/No
- MongoDB Running: Yes/No
- Browser: Chrome/Firefox/Safari

What I've tried:
- [ ]
- [ ]
```

---

**Remember**: Most issues are configuration related. Verify your setup matches QUICKSTART.md!

Last Updated: May 25, 2026
