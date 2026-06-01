# MongoDB Setup & Commands

## 🗄️ MongoDB Installation & Setup

### Windows Installation

#### Using MongoDB Community
1. Download from: https://www.mongodb.com/try/download/community
2. Run the installer (.msi file)
3. Choose "Complete" installation
4. Check "Run as a Service" during installation
5. Keep default settings

#### Verify Installation
```powershell
mongod --version
```

#### Start MongoDB Service
```powershell
# Method 1: As a service
net start MongoDB

# Method 2: Manually
mongod

# Method 3: With Homebrew (if installed)
brew services start mongodb-community
```

#### Access MongoDB Shell
```powershell
mongo
# or newer version:
mongosh
```

### macOS Installation

```bash
# Using Homebrew
brew tap mongodb/brew
brew install mongodb-community

# Start the service
brew services start mongodb-community

# Access MongoDB shell
mongosh
```

### Linux Installation (Ubuntu)

```bash
# Install
sudo apt-get update
sudo apt-get install -y mongodb

# Start service
sudo systemctl start mongodb

# Check status
sudo systemctl status mongodb
```

---

## 📝 Useful MongoDB Commands

### Database Operations
```javascript
// Show all databases
show dbs

// Switch to database
use skillswap_hub

// Show current database
db

// Drop database
db.dropDatabase()
```

### Collection Operations
```javascript
// Show all collections
show collections

// Create collection
db.createCollection("users")

// Drop collection
db.users.drop()

// Get collection size
db.users.dataSize()
```

### Document Operations - Users

```javascript
// Insert a test user
db.users.insertOne({
  name: "John Doe",
  email: "john@example.com",
  password: "hashed_password_here",
  created_at: new Date()
})

// Find all users
db.users.find()

// Find specific user
db.users.findOne({ email: "john@example.com" })

// Update user
db.users.updateOne(
  { email: "john@example.com" },
  { $set: { name: "Jane Doe" } }
)

// Delete user
db.users.deleteOne({ email: "john@example.com" })

// Count users
db.users.countDocuments()
```

### Document Operations - Skills

```javascript
// Insert a test skill
db.skills.insertOne({
  title: "Web Development",
  description: "Learn web development with HTML, CSS, and JavaScript",
  category: "Web Development",
  user_id: ObjectId("..."),
  user_name: "John Doe",
  created_at: new Date(),
  updated_at: new Date()
})

// Find all skills
db.skills.find()

// Find skills by category
db.skills.find({ category: "Web Development" })

// Find skills by user
db.skills.find({ user_id: ObjectId("...") })

// Search in skills
db.skills.find({
  $or: [
    { title: /web/i },
    { description: /web/i }
  ]
})

// Update skill
db.skills.updateOne(
  { _id: ObjectId("...") },
  { $set: { title: "Advanced Web Development" } }
)

// Delete skill
db.skills.deleteOne({ _id: ObjectId("...") })

// Count skills
db.skills.countDocuments()
```

### Advanced Queries

```javascript
// Find and sort
db.skills.find().sort({ created_at: -1 }).limit(10)

// Aggregation example - Get user skill counts
db.skills.aggregate([
  {
    $group: {
      _id: "$user_id",
      skillCount: { $sum: 1 }
    }
  }
])

// Search with regex (case-insensitive)
db.skills.find({ title: /python/i })

// Get recent skills
db.skills.find().sort({ created_at: -1 }).limit(5)

// Count by category
db.skills.aggregate([
  {
    $group: {
      _id: "$category",
      count: { $sum: 1 }
    }
  }
])
```

### Index Operations

```javascript
// Create index on email (for faster searches)
db.users.createIndex({ email: 1 }, { unique: true })

// Create index on user_id
db.skills.createIndex({ user_id: 1 })

// Create text index for full-text search
db.skills.createIndex({ title: "text", description: "text" })

// List all indexes
db.users.getIndexes()

// Drop index
db.users.dropIndex("email_1")

// Drop all indexes
db.users.dropIndexes()
```

### Backup & Restore

```bash
# Backup database
mongodump --db skillswap_hub --out ./backup

# Restore database
mongorestore --db skillswap_hub ./backup/skillswap_hub

# Backup specific collection
mongodump --db skillswap_hub --collection users --out ./backup

# Restore specific collection
mongorestore --db skillswap_hub --collection users ./backup/skillswap_hub/users.bson
```

---

## 🔧 MongoDB Configuration (.env)

Your `.env` file is configured with:

```env
MONGO_URI=mongodb://localhost:27017/
MONGO_DB=skillswap_hub
```

### For Production
```env
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/
MONGO_DB=skillswap_hub
```

### Connection String Format
```
mongodb://[username:password@]host[:port][/[database][?options]]
```

---

## 📊 Database Statistics

### Get Database Stats
```javascript
// Get database size
db.stats()

// Get collection stats
db.users.stats()

// Get all collection sizes
db.adminCommand({listDatabases: 1})
```

### Monitor Connection
```javascript
// Check current connection
db.adminCommand("ping")

// Get server status
db.serverStatus()

// Get connected clients
db.currentOp()
```

---

## 🔒 Security Notes for Production

```javascript
// Create admin user
db.createUser({
  user: "admin",
  pwd: "your_secure_password",
  roles: ["dbOwner", "userAdmin"]
})

// Create app user with limited permissions
db.createUser({
  user: "app_user",
  pwd: "app_password",
  roles: [
    { role: "readWrite", db: "skillswap_hub" }
  ]
})

// List users
db.getUsers()

// Update user password
db.changeUserPassword("app_user", "new_password")

// Remove user
db.removeUser("app_user")
```

---

## ⚠️ Common Issues & Solutions

### Issue: "Timeout connecting to MongoDB"
**Solution**: Make sure MongoDB service is running
```powershell
mongod
# or
net start MongoDB
```

### Issue: "Address already in use"
**Solution**: MongoDB is already running. Check if process exists:
```powershell
netstat -ano | findstr :27017
# Kill the process if needed
taskkill /PID <PID> /F
```

### Issue: "No database with name"
**Solution**: Create the database by inserting a document
```javascript
use skillswap_hub
db.users.insertOne({ temp: "data" })
```

### Issue: "Authentication failed"
**Solution**: Check credentials in connection string or disable auth:
```javascript
# Start without auth (development only)
mongod --noauth
```

---

## 📚 MongoDB Resources

- **Official Documentation**: https://docs.mongodb.com/
- **MongoDB Atlas**: https://www.mongodb.com/cloud/atlas
- **MongoDB Compass** (GUI): https://www.mongodb.com/products/tools/compass
- **PyMongo Docs**: https://pymongo.readthedocs.io/

---

## 🚀 MongoDB Connection in Python

```python
from pymongo import MongoClient

# Connection
client = MongoClient('mongodb://localhost:27017/')

# Get database
db = client['skillswap_hub']

# Get collection
users = db['users']

# Operations
users.insert_one({"name": "John", "email": "john@example.com"})
users.find_one({"email": "john@example.com"})
users.update_one({"_id": id}, {"$set": {"name": "Jane"}})
users.delete_one({"_id": id})
```

---

## 🎯 Quick Reference

| Command | Purpose |
|---------|---------|
| `mongod` | Start MongoDB server |
| `mongosh` or `mongo` | Start MongoDB shell |
| `show dbs` | List databases |
| `use skillswap_hub` | Switch database |
| `show collections` | List collections |
| `db.users.find()` | Find all users |
| `db.skills.find()` | Find all skills |
| `db.users.insertOne({...})` | Insert user |
| `db.skills.insertOne({...})` | Insert skill |
| `db.users.countDocuments()` | Count users |
| `db.stats()` | Database stats |

---

## 📝 Sample Data Import

To test the application with sample data:

```javascript
// Insert test users
db.users.insertMany([
  {
    name: "Alice Johnson",
    email: "alice@example.com",
    password: "$2b$12$...",  // hashed password
    created_at: new Date("2026-05-20")
  },
  {
    name: "Bob Smith",
    email: "bob@example.com",
    password: "$2b$12$...",
    created_at: new Date("2026-05-21")
  }
])

// Insert test skills
db.skills.insertMany([
  {
    title: "Python Programming",
    description: "Learn Python from basics to advanced",
    category: "Programming",
    user_id: ObjectId("..."),  // Alice's ID
    user_name: "Alice Johnson",
    created_at: new Date("2026-05-22")
  },
  {
    title: "Digital Marketing",
    description: "Master digital marketing strategies",
    category: "Marketing",
    user_id: ObjectId("..."),  // Bob's ID
    user_name: "Bob Smith",
    created_at: new Date("2026-05-23")
  }
])
```

---

**Last Updated**: May 25, 2026  
**Version**: 1.0.0
