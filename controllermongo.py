from pymongo import MongoClient # import MongoClient
import pandas as pd
import numpy as np

mongodb = MongoClient('localhost', 27017) # connect to mongoDB at localhost, port 27017

db = mongodb.oshes # use "oshes" database
# print(db)

collection = db.Product
# print(collection)

cursor = collection.find()
r = (list(cursor)) # convert the documents object into a list
print(r)

S = pd.DataFrame(r)
print(S)

