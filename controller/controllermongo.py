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
        queryDict["PurchaseStatus"] = ["Unsold"]  # find only Unsold items
        for (key, value) in selection.items():
            if len(value) != 0:
                queryDict[key[:1].upper() + key[1:]] = { # Make key and value title case, no spaces
                    "$in": 
                        [float(v)
                            if key == "productionYear" else v for v in value
                        ]
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
                "$addFields": {
                    "Unsold": {"$cond": [{"$eq": ["$PurchaseStatus","Unsold"]}, 1, 0]},
                }
            },
            {
                "$group": {
                    "_id": {"$first": "$Model_Item.ProductID"},
                    "model": {"$first": {"$first": "$Model_Item.Model"}},
                    "category": {"$first": {"$first": "$Model_Item.Category"}},
                    "price": {"$first": {"$first": "$Model_Item.Price ($)"}},
                    "numItemsInStock": {"$sum": "$Unsold"},
                    "warranty": {"$first": {"$first": "$Model_Item.Warranty (months)"}},
                    "itemIDs": {"$push": "$ItemID"}
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

        # flatMap values that are in lists
        # columns = ['productId', 'model', 'category', 'price', 'warranty']
        # for column in columns:
        #     df[column] = df[column].apply(lambda arr: arr[0])

        return df


    def adminSearch(self, selection):
        queryDict = {}
        for (key, array) in selection.items():
            if len(array) != 0:
                queryDict[key.title()] = { # Make key and value title case, no spaces
                    "$in": 
                        [float(value)
                            if key == "productionYear" else value for value in array
                        ]
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
                    "Sold": {"$cond": [{"$eq": ["$PurchaseStatus","Sold"]}, 1, 0]},
                    "Unsold": {"$cond": [{"$eq": ["$PurchaseStatus","Unsold"]}, 1, 0]},
                    "serviceFee": { "$sum": [40, { "$multiply": [ {"$first": "$Model_Item.Cost ($)"}, 0.2 ] }]}
                }
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
                    "itemIDs": {"$push": "$ItemID"}
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

        return df


# TESTING

if __name__ == '__main__':
    m = Mongo()
    print(m.customerSearch({"model": [], "category": ["locks"],  "color": ["white"],
                        "productionYear": ["2015"], "factory": [], "powerSupply": ["Battery"]}))
    print(m.customerSearch({"model": [], "category": [],  "color": [],
                        "productionYear": [], "factory": [], "powerSupply": []}))
    print(m.adminSearch({"model": ["Light1", "Light2", "SmartHome1"]}))