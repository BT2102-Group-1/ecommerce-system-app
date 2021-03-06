from pymongo import MongoClient
from bson.son import SON
import pandas as pd
import numpy as np

class Mongo:
    def __init__(self):
    # connect to mongoDB at localhost, port 27017
        self.mongodb = MongoClient('localhost', 27017)
        self.db = self.mongodb.oshes  # use "oshes" database
        self.collection = self.db.Item

    # Takes in a selection in the form of a dictionary, e.g. {'model': ["Light1", "Light2"], 'category': ["Lights"], 'Colours': ["Black", "Red", "Blue"], 'Factory': [], 'ProductionYear': [], 'PowerSupply: []}
    # If user does not select any filter for the category, the value of the category will be an empty array
    # Returns an dataframe of UNSOLD items (productId, model, category, price, number of items in stock, warranty, [list of items objects])

    # NOTE FOR BACKEND: Currently it's based on the old array input, where values are one single string
    # Incorrect array input: { "model": "safe1", "category": "locks",  "colour": "white", "productionYear": "2011", "factory": "Singapore", "powerSupply": "Battery"}


    def customerSearch(self, selection):
        queryDict = dict()

        # Only Unsold
        queryDict["PurchaseStatus"] = "Unsold"  # find only Unsold items

        # Price
        price = dict()
        if bool(selection["MinPrice"]):
            price["$gte"] = selection["MinPrice"][0]
            selection.pop("MinPrice")
        if bool(selection["MaxPrice"]):
            price["$lte"] = selection["MaxPrice"][0]
            selection.pop("MaxPrice")
        if bool(price):
            queryDict["Model_Item.Price ($)"] = price

        # Other attributes
        for (key, array) in selection.items():
            if len(array) != 0:
                queryDict[key[:1].upper() + key[1:]] = { # Make key and value title case, no spaces
                    "$in": 
                        [value[:1].upper() + value[1:] for value in array]
                    }

        # Perform MongoDB aggregation
        pipeline = [
            {
                "$lookup": {
                    "from": "Product",
                    "let": {"model": "$Model", "category": "$Category"},
                    "pipeline": [
                        {"$match":
                            {"$expr":
                                {"$and":
                                    [
                                        {"$eq": ["$Model",  "$$model"]},
                                        {"$eq": ["$Category", "$$category"]}
                                    ]
                                }
                            }
                        }
                    ],
                    "as": "Model_Item"
                }
            },
            {
                "$match": queryDict
            },
            {
                "$addFields": {
                    "Unsold": {"$cond": [{"$eq": ["$PurchaseStatus","Unsold"]}, 1, 0]},
                }
            },
            {
                "$sort": SON([("ItemID", 1)])
            },
            {
                "$group": {
                    "_id": {"$first": "$Model_Item.ProductID"},
                    "model": {"$first": {"$first": "$Model_Item.Model"}},
                    "category": {"$first": {"$first": "$Model_Item.Category"}},
                    "price": {"$first": {"$first": "$Model_Item.Price ($)"}},
                    "numItemsInStock": {"$sum": "$Unsold"},
                    "warranty": {"$first": {"$first": "$Model_Item.Warranty (months)"}},
                    "items": {"$push": {"ItemID": "$ItemID", "Color": "$Color", "Factory": "$Factory", "PowerSupply": "$PowerSupply", "ProductionYear": "$ProductionYear"}}
                }
            },
            {
                "$sort": SON([("model", 1)])
            },
        ]

        cursor = self.collection.aggregate(pipeline)

        results = list(cursor)  # convert the documents object into a list
        if (not bool(results)):
            return []
        
        df = pd.DataFrame(results)
        df.rename(columns={'_id': 'productId'}, inplace=True)
        df.drop(columns=['productId', 'numItemsInStock'], inplace=True)
        return df.to_dict('records')


    def adminSearch(self, selection):
        queryDict = dict()
        
        # Price
        price = dict()
        if bool(selection["MinPrice"]):
            price["$gte"] = selection["MinPrice"][0]
            selection.pop("MinPrice")
        if bool(selection["MaxPrice"]):
            price["$lte"] = selection["MaxPrice"][0]
            selection.pop("MaxPrice")
        if bool(price):
            queryDict["Model_Item.Price ($)"] = price

        # Other attributes
        for (key, array) in selection.items():
            if len(array) != 0:
                queryDict[key[:1].upper() + key[1:]] = { # Make key and value title case, no spaces
                    "$in": 
                        [value[:1].upper() + value[1:] for value in array]
                    }

        # DEBUGGING
        print(queryDict)

        # Perform MongoDB aggregation
        pipeline = [
            {
                "$lookup": {
                    "from": "Product",
                    "let": {"model": "$Model", "category": "$Category"},
                    "pipeline": [
                        {"$match":
                            {"$expr":
                                {"$and":
                                    [
                                        {"$eq": ["$Model",  "$$model"]},
                                        {"$eq": ["$Category", "$$category"]}
                                    ]
                                }
                            }
                        }
                    ],
                    "as": "Model_Item"
                }
            },
            {
                "$match": queryDict
            },
            {
                "$addFields": {
                    "Sold": {"$cond": [{"$eq": ["$PurchaseStatus","Sold"]}, 1, 0]},
                    "Unsold": {"$cond": [{"$eq": ["$PurchaseStatus","Unsold"]}, 1, 0]},
                    "serviceFee": { "$sum": [40, { "$multiply": [ {"$first": "$Model_Item.Cost ($)"}, 0.2 ] }]}
                }
            },
            {
                "$sort": SON([("ItemID", 1)])
            },
            {
                "$group": {
                    "_id": {"$first": "$Model_Item.ProductID"},
                    "model": {"$first": {"$first": "$Model_Item.Model"}},
                    "category": {"$first": {"$first": "$Model_Item.Category"}},
                    "price": {"$first": {"$first": "$Model_Item.Price ($)"}},
                    "serviceFee": {"$first": "$serviceFee"},
                    "numItemsInStock": {"$sum": "$Unsold"},
                    "numItemsSold": {"$sum": "$Sold"},
                    "warranty": {"$first": {"$first": "$Model_Item.Warranty (months)"}},
                    "items": {"$push": {"ItemID": "$ItemID", "Color": "$Color", "Factory": "$Factory", "PowerSupply": "$PowerSupply", "ProductionYear": "$ProductionYear", "PurchaseStatus": "$PurchaseStatus"}}
                }
            },
            {
                "$sort": SON([("model", 1)])
            },
        ]

        cursor = self.collection.aggregate(pipeline)

        results = list(cursor)  # convert the documents object into a list
        df = pd.DataFrame(results)
        df.rename(columns={'_id': 'productId'}, inplace=True)

        return df.to_dict('records')

    def findItem(self, itemId):
        
        # Perform MongoDB aggregation
        pipeline = [
            {
                "$lookup": {
                    "from": "Product",
                    "let": {"model": "$Model", "category": "$Category"},
                    "pipeline": [
                        {"$match":
                            {"$expr":
                                {"$and":
                                    [
                                        {"$eq": ["$Model",  "$$model"]},
                                        {"$eq": ["$Category", "$$category"]}
                                    ]
                                }
                            }
                        }
                    ],
                    "as": "Model"
                }
            },
            {
                "$match": {"ItemID": str(itemId)}
            },
            {
                "$addFields": {
                    "ModelName": {"$first": "$Model.Model"},
                    "Price": {"$first": "$Model.Price ($)"},
                    "Cost": {"$first": "$Model.Cost ($)"},
                    "Warranty": {"$first": "$Model.Warranty (months)"},
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "Model": 0,
                    "ServiceStatus": 0,
                    # "Price": { "$concat": ["$", "$Price"] },
                    # "Cost": { "$concat": ["$", "$Cost"] },
                    # "Warranty": { "$concat": ["$Model.Warranty (months)", " Months"] }
                }
            },
        ]

        cursor = self.collection.aggregate(pipeline)
        results = list(cursor)  # convert the documents object into a list
        df = pd.DataFrame(results)
        df.rename(columns={'ModelName': 'Model'}, inplace=True)
        return df.to_dict('records')
    
    # Returns True if MongoDB database was successfully updated, False otherwise
    def purchase(self, itemId):
        cursor = self.collection.update_one({"ItemID": itemId}, {"$set": {"PurchaseStatus": "Sold"}})
        print(cursor.raw_result['updatedExisting'])
        return cursor.raw_result['updatedExisting']

# TESTING

if __name__ == '__main__':
    m = Mongo()
    # print(m.findItem(1009))
    # print(m.adminSearch({'Model': [], 'Category': [], 'Color': [], 'Factory': [], 'PowerSupply': [], 'ProductionYear': [], 'PurchaseStatus': [], 'MinPrice': [100], 'MaxPrice': []}))
    # print(m.customerSearch({'Model': [], 'Category': [], 'Color': [], 'Factory': [], 'PowerSupply': [], 'ProductionYear': [], 'MinPrice': [], 'MaxPrice': [100]}))