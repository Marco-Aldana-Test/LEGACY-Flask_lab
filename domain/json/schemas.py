"""
This is a python document to work with schemas validation in marshmallow
"""
from marshmallow import Schema, fields


# Homework, see the "validate="
class PlayerSchema(Schema):
    IdPlayer = fields.Int(required=True)
    PlayerName = fields.Str(required=True)
    PlayerScore = fields.Float(required=True)


class CardSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    attack = fields.Int(required=True)
    defense = fields.Int(required=True)


class ParameterLoadSchema(Schema):
    attribute = fields.Str(required=True)
    value = fields.Field(required=True)
