from db import db
from datetime import datetime


class DailyExercise(db.Model):
    __tablename__ = "daily_exercise"

    id = db.Column(db.Integer, primary_key=True)
    exercise_name = db.Column(db.String, nullable=False)
    exercise_start_date = db.Column(db.DateTime, default=datetime.now())
    exercise_end_date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id") ,unique=False, nullable=False)
    user = db.relationship("User", backref='users')