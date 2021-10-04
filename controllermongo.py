from pymongo import MongoClient # import MongoClient
import pandas as pd
import numpy as np

mongodb = MongoClient('localhost', 27017) # connect to mongoDB at localhost, port 27017

db = mongodb.oshes # use "oshes" database
# print(db)

collection = db.Item
# print(collection)

# cursor = collection.find({"PurchaseStatus": "Unsold"}) # find all unsold items
# r = (list(cursor)) # convert the documents object into a list
# S = pd.DataFrame(r)
# del S["_id"]
# print(S)


# Takes in a selection in the form of a dictionary, e.g. { "model": "safe1", "category": "locks",  "color": "white", "productionYear": "2011", "factory": "Singapore", "powerSupply": "Battery"}
# If user does not select any filter for the category, the value of the category will be an empty string, eg category: ""
# Returns an array of UNSOLD items
def customerSearch(selection): 
    
    queryDict = dict()
    for (key, value) in selection.items():
      if value != "":

        if key == "productionYear":
          queryDict[key[:1].upper() + key[1:]] = float(value) # Make key title case, no spaces
        else:
          queryDict[key[:1].upper() + key[1:]] = value.capitalize() 



    # ONLY OF UNSOLD!!
    # return should be like this
    # arr = [[productNameVar, price, # of items in stock, warranty, [list of items objects]],[[productNameVar, price, # of items in stock, warranty, [list of items objects]],[[productNameVar, price, # of items in stock, warranty, [list of items objects]] etc ...
    # BECAUSE we follow the design sent into the group drawn by hongpei sent by megan
    return queryDict

queryDict = customerSearch({ "model": "", "category": "locks",  "color": "white", "productionYear": "2015", "factory": "", "powerSupply": "Battery"})
queryDict["PurchaseStatus"] = "Unsold"
print(queryDict)
cursor = collection.find(queryDict) # find all unsold items
r = (list(cursor)) # convert the documents object into a list
T = pd.DataFrame(r)
del T["_id"]
print(T)