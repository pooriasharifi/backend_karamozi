from mongoengine import Document, fields, EmbeddedDocument

# from model.comment import Comment


class Comment(EmbeddedDocument):
    comment=fields.StringField()
    date = fields.StringField()
    timer=fields.IntField()


class Users(Document):
    username = fields.IntField( unique=True)
    password = fields.StringField()
    kar_location=fields.StringField()
    name=fields.StringField()
    sarparast=fields.StringField()
    ostad=fields.StringField()
    sign=fields.IntField()
    verify=fields.BooleanField()
    comments=fields.ListField(fields.EmbeddedDocumentField(Comment))
    hour=fields.IntField(default=0)
    # comments = fields.EmbeddedDocumentField(Comment)
    # fields.ListField(fields.EmbeddedDocumentField(Date))
    # timer = fields.ReferenceField()