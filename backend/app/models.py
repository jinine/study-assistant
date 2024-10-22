from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, DateTime
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)                            # Auto-incrementing ID
    username = db.Column(db.String(50), nullable=False, unique=True)       # Unique username, max length of 50 characters
    email = db.Column(db.String(100), nullable=False, unique=True)         # Unique email address, max length of 100 characters
    first_name = db.Column(db.String(50))                                  # First name, max length of 50 characters
    last_name = db.Column(db.String(50))                                   # Last name, max length of 50 characters
    encrypted_pass = db.Column(db.String(128), nullable=False)             # Encrypted password, max length of 128 characters
    profile_picture_url = db.Column(db.String(255))                        # URL of the user's profile picture, max length of 255 characters
    is_active = db.Column(Boolean, default=True)                           # User account active status
    created_at = db.Column(DateTime, default=datetime.utcnow)              # Timestamp of account creation
    updated_at = db.Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Timestamp of last update

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,  
            "first_name": self.first_name,
            "last_name": self.last_name,
            "profile_picture": self.profile_picture_url,
            "is_active": self.is_active,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

class StudyMaterial(db.Model):
    __tablename__ = 'study_materials'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description
        }

class StudyProgress(db.Model):
    __tablename__ = 'study_progress'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) 
    study_material_id = db.Column(db.Integer, db.ForeignKey('study_materials.id'), nullable=False)
    summary_completed = db.Column(db.Boolean, default=False)
    quiz_completed = db.Column(db.Boolean, default=False)
    last_studied = db.Column(db.DateTime)
    study_streak = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "study_material_id": self.study_material_id,
            "summary_completed": self.summary_completed,
            "quiz_completed": self.quiz_completed,
            "last_studied": self.last_studied,
            "study_streak": self.study_streak
        }

class Quiz(db.Model):
    __tablename__ = 'quizzes'
    
    id = db.Column(db.Integer, primary_key=True)
    study_material_id = db.Column(db.Integer, db.ForeignKey('study_materials.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "study_material_id": self.study_material_id,
            "title": self.title,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

class QuizQuestion(db.Model):
    __tablename__ = 'quiz_questions'
    
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'), nullable=False)
    question = db.Column(db.String(255), nullable=False)
    option_a = db.Column(db.String(100), nullable=False)
    option_b = db.Column(db.String(100), nullable=False)
    option_c = db.Column(db.String(100), nullable=False)
    option_d = db.Column(db.String(100), nullable=False)
    correct_answer = db.Column(db.String(1), nullable=False)  # 'A', 'B', 'C', or 'D'

    def to_dict(self):
        return {
            "id": self.id,
            "quiz_id": self.quiz_id,
            "question": self.question,
            "options": {
                "A": self.option_a,
                "B": self.option_b,
                "C": self.option_c,
                "D": self.option_d,
            },
            "correct_answer": self.correct_answer
        }

class StudyNotification(db.Model):
    __tablename__ = 'study_notifications'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Fix: should reference 'users.id'
    study_material_id = db.Column(db.Integer, db.ForeignKey('study_materials.id'), nullable=False)
    notification_time = db.Column(db.DateTime, nullable=False)
    message = db.Column(db.String(255), nullable=False)
    is_sent = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "study_material_id": self.study_material_id,
            "notification_time": self.notification_time,
            "message": self.message,
            "is_sent": self.is_sent
        }
