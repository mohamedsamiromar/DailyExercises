from flask import Flask, flash
import os

app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from forms import RegisterForm

db = SQLAlchemy()
migrate = Migrate(app, db)
bcrypt = Bcrypt()
db.init_app(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from flask_login import UserMixin

basedir = os.path.abspath(os.path.dirname(__file__))
from flask import render_template

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = Falsedb = SQLAlchemy(app)


class User(UserMixin, db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return self.username


class DailyExercise(db.Model):
    __tablename__ = "daily_exercise"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    exercise_name = db.Column(db.String, nullable=False)
    exercise_start_date = db.Column(db.DateTime, default=datetime.utcnow())
    exercise_end_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return self.exercise_name


@app.route('/')
def index():
    return render_template('register.html')


@app.route('/register', methods=(['GET', 'POST']))
def register():
    if RegisterForm.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(RegisterForm.password.data).decode('utf-8')
        user = User()
        user.username = RegisterForm.username.data
        user.email = RegisterForm.email
        user.password = hashed_password
        db.session.add(user)
        flash('Your Account Has Been Created! You Are Now Able To Login ّّّّ')
        return render_template('register.html', title='Register', form=RegisterForm)


if __name__ == '__main__':
    app.run(debug=True)
