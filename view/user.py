from email import message
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from sqlalchemy.exc import SQLAlchemyError
from schema import UserRegisterSchema
from models.user_model import User
from db import db



blp = Blueprint("users", "Users", __name__, description="Operations on User")

@blp.route("/register")
class UserRegister(MethodView):

    @blp.arguments(UserRegisterSchema)
    def post(self, user_data):
        if User.query.filter(User.username == user_data["username"]).first():
            abort(409, message="A user with that username already exists.")
        user = User(
            username=user_data["username"],
            password=user_data["password"],
        )
        db.session.add(user)
        db.session.commit()

        return {"message": "User created successfully."}, 201