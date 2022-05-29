from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import  LoginManager
from flask_migrate import Migrate
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from flask_login import UserMixin


login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class DailyExercise(db.Model):
    __tablename__ = "daily_exercise"

    id = db.Column(db.Integer, primary_key=True)
    exercise_name = db.Column(db.String, nullable=False)
    exercise_start_date = db.Column(db.DateTime, defualt=False)
    exercise_end_date = db.Column(db.DateTime, defualt=False)

    def __repr__(self):
        return '<DailyExercise %r>' % self.exercise_name
