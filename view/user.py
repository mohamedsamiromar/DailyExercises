from email import message
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from sqlalchemy.exc import SQLAlchemyError
from schema import UserRegisterSchema, LoginSchema
from models.user_model import User
from db import db
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token, create_refresh_token


blp = Blueprint("users", "Users", __name__, description="Operations on User")


@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserRegisterSchema)
    def post(self, user_data):
        print(user_data["username"])
        if User.query.filter(User.username == user_data["username"]).first():
            abort(409, message="A user with that username already exists.")
        user = User(
            username=user_data["username"],
            email = user_data["email"],
            password=pbkdf2_sha256.hash(user_data["password"]),
            first_name =user_data["first_name"],
            middle_name =user_data["middle_name"],
            last_name=user_data["last_name"],
            mobile_phone=user_data["mobile_phone"],
            Address=user_data["Address"]
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


@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(LoginSchema)
    def post(self, user_data):
        user = User.query.filter(
            User.username == user_data["username"]
        ).first()
        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {"access_token": access_token, "refresh_token": refresh_token}, 200

        abort(401, message="Invalid credentials.")