from mongoengine import Document, StringField, IntField, BooleanField



class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField() #0: female, 1: male
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
