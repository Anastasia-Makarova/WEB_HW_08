from mongoengine import  Document, CASCADE
from mongoengine.fields import  StringField, BooleanField
from mongoengine import connect

url = 'mongodb+srv://pythonweb18:5txFAXOlDGmCl2df@Subscribers.ohw57vp.mongodb.net/?retryWrites=true&w=majority'

connect(host=url, ssl=True)

class Subscriber(Document):
    fullname = StringField()
    email = StringField()
    phone = StringField()
    got_mail = BooleanField(default=False)

   


    