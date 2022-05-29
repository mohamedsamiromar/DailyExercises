from flask import Flask

app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
from flask_migrate import Migrate

migrate = Migrate(app, db)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
