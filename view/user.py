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
    @blp.response(201, UserRegisterSchema)
    def post(self, user_data):
        if User.query.filter(User.username == user_data["username"]).first():
            abort(401, 
            message="User With That Username Already Exits")
        user = User(
            username=user_data["username"],
            email=user_data["email"],
            password=user_data["password"]
        )
        db.session.add(user)
        db.session.commit()
        return {"message": "user has been created"}