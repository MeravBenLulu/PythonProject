from pymongo import MongoClient

client = MongoClient('localhost:27017')

db = client['balance_DB']
users = db['users']
incomes=db['incoms']
expenses=db['expenses']