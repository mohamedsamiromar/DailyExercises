from binascii import a2b_hqx
from db import db 


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True, nullable=False)
    email = db.Column(db.String(120),nullable=False)
    password = db.Column(db.String(), nullable=False, unique=True)
    first_name = db.Column(db.String(80), nullable=False)
    middle_name = db.Column(db.String(80), nullable=False)
    Address = db.Column(db.String(120), nullable=False)
    # daily_exercise = db.relationship("DailyExercise", back_populates="daily_exercise")


