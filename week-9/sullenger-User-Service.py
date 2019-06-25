# ============================================
# ; Title:  sullenger-User-Service.py
# ; Author: Professor Krasso
# ; Date:  24 June 2019
# ; Modified By: Jason Sullenger
# ; Description: querying and creating documents with Python and pymongo
# ;===========================================

from pymongo import MongoClient

import pprint

import datetime

client=MongoClient('localhost', 27017)

db=client.web335

user={
    "first_name": "Stacy",
    "last_name": "Simpson",
    "email": "ssimpson@fakeEmail.com",
    "employee_id": "2468246",
    "date_created": datetime.datetime.utcnow()
}

user_id = db.users.insert_one(user).inserted_id

print(client)

print(user_id)

pprint.pprint(db.users.find_one({"employee_id": "2468246"}))