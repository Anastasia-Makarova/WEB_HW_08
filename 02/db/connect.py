from mongoengine import connect

url = 'mongodb+srv://pythonweb18:5txFAXOlDGmCl2df@Subscribers.ohw57vp.mongodb.net/?retryWrites=true&w=majority'

connect(host=url, ssl=True)