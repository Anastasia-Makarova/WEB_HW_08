from mongoengine import  Document, CASCADE
from mongoengine.fields import DateTimeField, ListField, StringField, ReferenceField
from mongoengine import connect

connect(host='mongodb+srv://pythonweb18:5txFAXOlDGmCl2df@homework.ohw57vp.mongodb.net/?retryWrites=true&w=majority', ssl=True)


class Author(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()

   
class Quote(Document):
    tags = ListField(StringField(max_length=30))
    author = ReferenceField(Author, dbref=False) 
    quote = StringField()
    meta = {'allow_inheritance': True}

    