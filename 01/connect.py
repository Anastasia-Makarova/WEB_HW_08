from pymongo import MongoClient
# import configparser


# config = configparser.ConfigParser()
# config.read('config.ini')

# mongo_user = config.get('DB', 'user')
# mongodb_pass = config.get('DB', 'pass')
# db_name = config.get('DB', 'db_name')
# domain = config.get('DB', 'domain')

connect = MongoClient('mongodb+srv://pythonweb18:5txFAXOlDGmCl2df@homework.ohw57vp.mongodb.net/?retryWrites=true&w=majority')

db = connect.homework