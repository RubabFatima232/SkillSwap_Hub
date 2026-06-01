"""
Database connection and operations for SkillSwap Hub
"""

from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import os


# =========================
# MongoDB Connection
# =========================
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
DB_NAME = os.getenv('MONGO_DB', 'skillswap_hub')

client = MongoClient(MONGO_URI)
db = client[DB_NAME]


# =========================
# Database Class (FIXED)
# =========================
class Database:
    # ✅ Collections inside class (IMPORTANT FIX)
    users_collection = db['users']
    skills_collection = db['skills']

    # =========================
    # User Operations
    # =========================
    @staticmethod
    def add_user(name, email, password_hash):
        try:
            user_data = {
                'name': name,
                'email': email,
                'password': password_hash,
                'created_at': datetime.utcnow()
            }
            result = Database.users_collection.insert_one(user_data)
            return result.inserted_id
        except Exception as e:
            print(f"Error adding user: {e}")
            return None

    @staticmethod
    def get_user_by_email(email):
        try:
            return Database.users_collection.find_one({'email': email})
        except Exception as e:
            print(f"Error getting user: {e}")
            return None

    @staticmethod
    def get_user_by_id(user_id):
        try:
            return Database.users_collection.find_one({'_id': ObjectId(user_id)})
        except Exception as e:
            print(f"Error getting user by ID: {e}")
            return None


    # =========================
    # Skill Operations
    # =========================
    @staticmethod
    def create_skill(title, description, category, user_id, user_name):
        try:
            skill_data = {
                'title': title,
                'description': description,
                'category': category,
                'user_id': ObjectId(user_id),
                'user_name': user_name,
                'created_at': datetime.utcnow(),
                'updated_at': datetime.utcnow()
            }
            result = Database.skills_collection.insert_one(skill_data)
            return result.inserted_id
        except Exception as e:
            print(f"Error creating skill: {e}")
            return None

    @staticmethod
    def get_all_skills():
        try:
            return list(Database.skills_collection.find().sort('created_at', -1))
        except Exception as e:
            print(f"Error getting skills: {e}")
            return []

    @staticmethod
    def get_user_skills(user_id):
        try:
            return list(Database.skills_collection.find(
                {'user_id': ObjectId(user_id)}
            ).sort('created_at', -1))
        except Exception as e:
            print(f"Error getting user skills: {e}")
            return []

    @staticmethod
    def get_skill_by_id(skill_id):
        try:
            return Database.skills_collection.find_one({'_id': ObjectId(skill_id)})
        except Exception as e:
            print(f"Error getting skill: {e}")
            return None

    @staticmethod
    def update_skill(skill_id, title, description, category):
        try:
            result = Database.skills_collection.update_one(
                {'_id': ObjectId(skill_id)},
                {
                    '$set': {
                        'title': title,
                        'description': description,
                        'category': category,
                        'updated_at': datetime.utcnow()
                    }
                }
            )
            return result.modified_count > 0
        except Exception as e:
            print(f"Error updating skill: {e}")
            return False

    @staticmethod
    def delete_skill(skill_id):
        try:
            result = Database.skills_collection.delete_one(
                {'_id': ObjectId(skill_id)}
            )
            return result.deleted_count > 0
        except Exception as e:
            print(f"Error deleting skill: {e}")
            return False

    @staticmethod
    def search_skills(query):
        try:
            search_query = {
                '$or': [
                    {'title': {'$regex': query, '$options': 'i'}},
                    {'description': {'$regex': query, '$options': 'i'}},
                    {'category': {'$regex': query, '$options': 'i'}}
                ]
            }
            return list(Database.skills_collection.find(search_query).sort('created_at', -1))
        except Exception as e:
            print(f"Error searching skills: {e}")
            return []

    @staticmethod
    def get_skills_by_category(category):
        try:
            return list(Database.skills_collection.find(
                {'category': {'$regex': category, '$options': 'i'}}
            ).sort('created_at', -1))
        except Exception as e:
            print(f"Error getting skills by category: {e}")
            return []