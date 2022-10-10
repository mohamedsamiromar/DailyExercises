from dataclasses import field
from marshmallow import Schema, fields


class UserRegisterSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
