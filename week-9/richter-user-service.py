# Title: Exercise 9.2
# Author: Emily Richter
# Date:  22 June 2020
# Description: Creating and querying documents through Python

first_name='Emily'
last_name='Richter'
print(first_name+' '+last_name)

from pymongo import MongoClient

import pprint
import datetime

client = MongoClient('localhost', 27017)

db = client.web335

user = {
    "first_name":"Jonah",
    "last_name":"Simms",
    "email":"jsimms@user.com",
    "employee_id":"9873425",
    "date_created":datetime.datetime.utcnow()
}

user_id=db.users.insert_one(user).inserted_id

print(user_id)

pprint.pprint(db.users.find_one({"employee_id":"9873425"}))