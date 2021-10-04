from pymongo import MongoClient
from bson.son import SON
import pandas as pd
import numpy as np

mongodb = MongoClient('localhost', 27017) # connect to mongoDB at localhost, port 27017

db = mongodb.oshes # use "oshes" database
collection = db.Item

# Takes in a selection in the form of a dictionary, e.g. {'model': ["Light1", "Light2"], 'category': ["Lights"], 'Colours': ["Black", "Red", "Blue"], 'Factory': [], 'ProductionYear': [], 'PowerSupply: []} 
# If user does not select any filter for the category, the value of the category will be an empty array
# Returns an dataframe of UNSOLD items (productId, model, category, price, number of items in stock, warranty, [list of items objects])

# NOTE FOR BACKEND: Currently it's based on the old array input, where values are one single string
# Incorrect array input: { "model": "safe1", "category": "locks",  "colour": "white", "productionYear": "2011", "factory": "Singapore", "powerSupply": "Battery"}
def customerSearch(selection): 
    
    # Transform selection input into a MongoDB query dictionary
    queryDict = dict()
    queryDict["PurchaseStatus"] = "Unsold" # find only Unsold items
    for (key, value) in selection.items():
      if value != "":

        if key == "productionYear":
          queryDict[key[:1].upper() + key[1:]] = float(value) # Make key title case, no spaces
        else:
          queryDict[key[:1].upper() + key[1:]] = value[:1].upper() + value[1:] # Make value title case, no spaces (esp for Model)

    print(queryDict) # debugging

    # Perform MongoDB aggregation
    pipeline = [
        {
          "$lookup": {
            "from": "Product",
            "let": { "model": "$Model", "category": "$Category" },
            "pipeline": [
                { "$match":
                  { "$expr":
                      { "$and":
                        [
                          { "$eq": [ "$Model",  "$$model" ] },
                          { "$eq": [ "$Category", "$$category" ] }
                        ]
                      }
                  }
                }
            ],
            "as": "Model"
        }
      },
      # {
      #   "$lookup": {
      #       "from": "Product",
      #       "localField": "Model",
      #       "foreignField": "Model",
      #       # "let": { <var_1>: <expression>, …, <var_n>: <expression> },
      #       "pipeline": [ <pipeline to run> ],
      #       "as": "Model",
      #   }
      # },
      { 
        "$match": queryDict 
      },
      { 
        "$group": {
          "_id": "$Model.ProductID", 
          "model": {"$first": "$Model.Model"},
          "category": {"$first": "$Model.Category"},
          "price": {"$first": "$Model.Price"},
          "numItemsInStock": {"$sum": 1}, 
          "warranty": {"$first": "$Model.Warranty"},
          "itemIDs": {"$push": "$ItemID"}
        }
      },
      {
        "$sort": SON([("model", 1)])
      },
    ]

    cursor = collection.aggregate(pipeline)
  
    results = list(cursor) # convert the documents object into a list
    df = pd.DataFrame(results)
    df.rename(columns={'_id': 'productId'}, inplace=True)

    # flatMap values that are in lists
    columns = ['productId', 'model', 'category', 'price', 'warranty']
    for column in columns:
      df[column] = df[column].apply(lambda arr: arr[0])
      
    return df

# TESTING
print(customerSearch({ "model": "", "category": "locks",  "color": "white", "productionYear": "2015", "factory": "", "powerSupply": "Battery"}))
print(customerSearch({ "model": "", "category": "",  "color": "", "productionYear": "", "factory": "", "powerSupply": ""}))
