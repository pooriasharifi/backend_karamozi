from enum import unique
from mongoengine import Document,fields


class Ostad(Document):
    name=fields.StringField(required=True)
    username=fields.IntField(required=True,unique=True)
    password=fields.StringField(required=True)
    sign=fields.IntField(required=True,unique=True)






