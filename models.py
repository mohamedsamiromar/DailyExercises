# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
# from flask_migrate import Migrate
# from datetime import datetime
# from flask_login import UserMixin
# from app import  app
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# db = SQLAlchemy(app)
# migrate = Migrate(db, app)
#
#
# class User(UserMixin, db.Model):
#     __tablename__ = "user"
#
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(50), nullable=False, unique=True)
#
#     def __repr__(self):
#         return self.username
#
#
# class DailyExercise(db.Model):
#     __tablename__ = "daily_exercise"
#
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
#     exercise_name = db.Column(db.String, nullable=False)
#     exercise_start_date = db.Column(db.DateTime, default=datetime.utcnow())
#     exercise_end_date = db.Column(db.DateTime, nullable=False)
#
#     def __repr__(self):
#         return self.exercise_name
