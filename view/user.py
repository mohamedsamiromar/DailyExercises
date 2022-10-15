from email import message
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from sqlalchemy.exc import SQLAlchemyError
from schema import UserRegisterSchema
from models.user_model import User
from db import db
from passlib.hash import pbkdf2_sha256


blp = Blueprint("users", "Users", __name__, description="Operations on User")


@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserRegisterSchema)
    def post(self, user_data):
        print(user_data)
        if User.query.filter(User.username == user_data["username"]).first():
            abort(409, message="A user with that username already exists.")
        user = User(
            username=user_data["username"],
            email = user_data["email"],
            password=pbkdf2_sha256.hash(user_data["password"]),
        )
        db.session.add(user)
        db.session.commit()

        return {"message": "User created successfully."}, 201



@blp.route("/get_user/<int:user_id>")
class GetUser(MethodView):
    # @blp.arguments(UserRegisterSchema)
    @blp.response(200, UserRegisterSchema)
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        print(user)
        if not user:
                abort(404, message="User not found.")
        return user