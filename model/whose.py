from mongoengine import Document,fields


class whose_ostad(Document):
    sign=fields.IntField(required=True)
    username=fields.StringField(required=True)
    verify=fields.BooleanField(required=True)