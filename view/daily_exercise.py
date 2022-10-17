from email import message
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from models.daily_exercise import DailyExercise
from schema import DailyExerciseSchema
from flask_jwt_extended import jwt_required
from db import db
from flask_login import LoginManager

blp = Blueprint("daily_exercise", __name__, description="Operations on daily_exercise")


@blp.route("/daily_exercise")
class AddDailyExercise(MethodView):

    @jwt_required()
    
    @blp.arguments(DailyExerciseSchema)
    @blp.response(200, DailyExerciseSchema)
    def post(self, daily_exercise_data):
        new_daily_attendance=DailyExercise(
            exercise_name=daily_exercise_data['exercise_name'],
            exercise_start_date=daily_exercise_data['exercise_start_date'],
            exercise_end_date=daily_exercise_data['exercise_end_date'],
            # user_id=user.id
        )
        db.session.add(new_daily_attendance)
        db.session.commit
        print(new_daily_attendance.id)
        return {"message": "Done!"}


@blp.route("/get-daily-attendance/<int:de_id>")
class GetDailyExercise(MethodView):
    @jwt_required()
    @blp.response(200, DailyExerciseSchema)
    def get(self, de_id):
        d_e = DailyExercise.query.get_or_404(de_id)
        if not d_e:
            abort(404, message="Daily Exercise Not Found")
        return d_e