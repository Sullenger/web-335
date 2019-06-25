# ============================================
# ; Title:  sullenger-User-Service.py
# ; Author: Professor Krasso
# ; Date:  24 June 2019
# ; Modified By: Jason Sullenger
# ; Description: updating and deleting documents with Python and pymongo
# ;===========================================

from pymongo import MongoClient

import pprint

import datetime

client=MongoClient('localhost', 27017)

db=client.web335

db.users.update_one(
    {"employee_id": "2468246"},
    {
        "$set": {
            "email": "ssimpsonUPDATED@fakeEmail.com"
        }
    }
)

pprint.pprint(db.users.find_one({"employee_id": "2468246"}))