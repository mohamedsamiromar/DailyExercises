from flask import Flask, render_template, request, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required
from models import User, bcrypt

app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
import forms

db = SQLAlchemy(app)
from flask_migrate import Migrate

migrate = Migrate(app, db)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def hello_world():
    if forms.RegistrationForm().validate_on_submit():
        register_form = forms.RegistrationForm()
        hashed_password = bcrypt.generate_password_hash(register_form.password.data).decode('utf-8')
        user = User(username=register_form.username.data,
                    email=register_form.email.data,
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()
        user = User.query.filter_by(
            email=forms.RegistrationForm().email.data).first()

        if user and bcrypt.check_password_hash(
                user.password, forms.RegistrationForm().password.data):
            login_user(user)
        # return redirect(url_for('hello_world')))
        return render_template('index.html',
                               login_form=forms.LoginForm(),
                               register_form=forms.RegistrationForm())

if __name__ == '__main__':
    app.run()
