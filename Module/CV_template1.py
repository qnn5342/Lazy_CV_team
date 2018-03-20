from mongoengine import Document, StringField, IntField, BooleanField



class Template1(Document):

    name = StringField()
    street_address = StringField()
    city = StringField()
    country = StringField()
    university = StringField()
    location = StringField()
    major = StringField()
    graduation = StringField()
    GPA = StringField()
    Line2 = StringField()
    Line3 = StringField()
