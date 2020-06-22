first_name='Emily'
last_name='Richter'
print(first_name+' '+last_name)

from pymongo import MongoClient

import pprint
import datetime

client = MongoClient('localhost', 27017)

db = client.web335

db.users.update_one(
    { "employee_id":"9873425"},

    {
        "$set":{
            "email":"emrichter@my365.bellevue.edu"
        }
    }
)

pprint.pprint(db.users.find_one({"employee_id":"9873425"}, {"_id":0,"email":1,"employee_id":1,"first_name":1,"last_name":1}))