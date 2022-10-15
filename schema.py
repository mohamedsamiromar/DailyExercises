from dataclasses import field
from marshmallow import Schema, fields


class UserRegisterSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    email = fields.Str()
    password = fields.Str(load_only=True)
