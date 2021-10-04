from pymongo import MongoClient
from bson.son import SON
import pandas as pd
import numpy as np

mongodb = MongoClient('localhost', 27017) # connect to mongoDB at localhost, port 27017

db = mongodb.oshes # use "oshes" database
# print(db)

collection = db.Item
# print(collection)


# Takes in a selection in the form of a dictionary, e.g. { "model": "safe1", "category": "locks",  "color": "white", "productionYear": "2011", "factory": "Singapore", "powerSupply": "Battery"}
# If user does not select any filter for the category, the value of the category will be an empty string, eg category: ""
# Returns an array of UNSOLD items
def customerSearch(selection): 
    
    queryDict = dict()
    queryDict["PurchaseStatus"] = "Unsold" # find only Unsold items
    for (key, value) in selection.items():
      if value != "":

        if key == "productionYear":
          queryDict[key[:1].upper() + key[1:]] = float(value) # Make key title case, no spaces
        else:
          queryDict[key[:1].upper() + key[1:]] = value[:1].upper() + value[1:] # Make value title case, no spaces (esp for Model)

    print(queryDict) # debugging

    pipeline = [
      { 
        "$match": queryDict 
      },
      { 
        "$group": {
          "_id": "$Model", 
          "numItemsInStock": {"$sum": 1}, 
          "itemIDs": {"$push": "$ItemID"}
        }
      },
      {
        "$sort": SON([("Model", 1)])
      },
    ]

    cursor = collection.aggregate(pipeline)
  
    results = list(cursor) # convert the documents object into a list
    df = pd.DataFrame(results)
    df.rename(columns={'_id': 'productName'}, inplace=True)
    print(df) # debugging


    # return should be like this
    # arr = [[productNameVar, price, # of items in stock, warranty, [list of items objects]],[[productNameVar, price, # of items in stock, warranty, [list of items objects]],[[productNameVar, price, # of items in stock, warranty, [list of items objects]] etc ...
    # BECAUSE we follow the design sent into the group drawn by hongpei sent by megan
    return df

customerSearch({ "model": "", "category": "locks",  "color": "white", "productionYear": "2015", "factory": "", "powerSupply": "Battery"})
