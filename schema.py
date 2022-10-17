from dataclasses import field
from marshmallow import Schema, fields


class UserRegisterSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str()
    email = fields.Str()
    password = fields.Str(load_only=True)
    first_name = fields.Str()
    middle_name = fields.Str()
    last_name = fields.Str()
    mobile_phone = fields.Int()
    Address = fields.Str()


class LoginSchema(Schema):
    username = fields.Str()
    password = fields.Str()


class DailyExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    exercise_name = fields.Str()
    exercise_start_date = fields.DateTime()
    exercise_end_date = fields.DateTime()
    # user_id = fields.Int(required=True, load_only=True)
    user = fields.Nested(UserRegisterSchema(), dump_only=True)
