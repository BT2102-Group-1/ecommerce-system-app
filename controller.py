from sqlalchemy import create_engine
from sqlalchemy.sql import text
import pandas as pd
import numpy as np
import json
import random


class Connection:
    def __init__(self):
        self.engine = create_engine(
            'mysql+mysqlconnector://root:password@localhost/oshes', connect_args={'use_pure': True})
        self.connection = self.engine.connect()


if __name__ == '__main__':
    db = Connection()
    print(db.engine)
    # print(pd.read_sql('customer', db.connection))
    # print(pd.read_sql_query('SELECT * FROM Customer WHERE gender = "F"', db.connection))

    # insert = pd.DataFrame(np.array([['Lyn Tan', 'F', '123 Tiong Bahru Rd', 'hihi@jeno.com', 'cpassword', '92969405']]), columns=['name', 'gender', 'address', 'email', 'password', 'phoneNo'])
    # insert.to_sql('customer', db.connection, if_exists='append', index_label='customerId') # write “customers” to database
    # print(pd.read_sql('customer', db.connection))

# -------------------------------------------------##--Customer Login Page--#------------------------------------------------------
# LYN


def customerLogin(email, password):
    # check against customer database that it exists and matches

    result = pd.read_sql_query(
        'SELECT customerId, password FROM Customer WHERE email = "%s"' % email, db.connection)
    return

    # return generated customerId
    # -1 means unsuccessful login (customer don't exist)

   # we will use this customerId as global variable to be used later as our parameter values

# -------------------------------------------------##--Customer Registration Page--#-----------------------------------------------
# LYN


def registerCustomer(email, password, name, address, phoneNo, gender):
    return
    # validation checks
    # - email must not exist in database
    # create customer in database + generate customerId on your end
    # return generated customerId
    # -1 means unsuccessful login

# -------------------------------------------------##--Product Search Page--#-----------------------------------------------------


def customerSearch(selection):
    return
    # selection comes in the form of a dictionary
    #{ "model": "safe1", "category": "locks",  "colour": "white", "productionYear": "2011", "factory": "Singapore", "powerSupply": "Battery"}

    # if user does not select any filter for the category, the value of the category will be an empty string, eg category: ""

    # ONLY OF UNSOLD!!
    # return should be like this
    # arr = [[productNameVar, price, # of items in stock, warranty, [list of items objects]],[[productNameVar, price, # of items in stock, warranty, [list of items objects]],[[productNameVar, price, # of items in stock, warranty, [list of items objects]] etc ...
    # BECAUSE we follow the design sent into the group drawn by hongpei sent by megan


def purchase(itemId, customerId, date):
    return
    # edit attributes of the item in the database - change unsold to sold and input customerId, record purchase date (impt for servicing later)

    # return true if successful, false otherwise (in any case where there are two customers viewing a product, one bought alr but not enough time to update in the product page and hence, the 2nd customer click yeet)

# -------------------------------------------------##--Purchase History Page--#-----------------------------------------------


class Item:
    def __init__(self, itemId, price, modelName, category, productionYear, colour, factory, powerSupply, purchaseDate):
        self.itemId = itemId
        self.price = price
        self.modelName = modelName
        self.category = category
        self.productionYear = productionYear
        self.colour = colour
        self.factory = factory
        self.powerSupply = powerSupply
        self.purchaseDate = purchaseDate


def getPurchaseHistory(customerId):
    # return all products bought by customer in the form of an array, consisting of item objects sorted base on purchase date (latest at the top)
    # item object should have itemid, price, model name, category, production year, colour, factory, powersupply, purchaseDate

    items_df = pd.read_sql_query(
        '''SELECT itemId, modelPrice, modelName, categoryName, productionYear, color, factory, powerSupply, purchaseDate
        FROM Item LEFT JOIN Model USING (productId) WHERE customerId = 1 ORDER BY purchaseDate DESC''' % customerId, db.connection)
    items = [Item(itemId, price, modelName, category, productionYear, colour, factory, powerSupply, purchaseDate)
             for itemId, price, modelName, category, productionYear, colour, factory, powerSupply, purchaseDate in items_df.iterrows()]

    return items

# -------------------------------------------------##--Request Service Page--#-----------------------------------------------


def getUnrequestedItems(customerId):
    # return all products bought by customer which DOES NOT HAVE A SERVICE REQUESTED OR HAD A MOST RECENT REQUEST WITH REQUEST STATUS AS CANCELLED OR COMPLETED in the form of an array, consisting of item objects
    # suggested METHOD: find items purchased then query requests based on the itemId -> just shows the requests for that itemId, since requestId will be incremented in increasing order, can get the largest requestId and check status
    # item object should have itemid, model name, purchaseDate, serviceFee, warranty (you can give us extra attributes if it is more convenient for your implementation) -- possible to give us warranty end date?

    items_df = pd.read_sql_query(
        "SELECT itemId, modelName, modelCost, modelWarranty, purchaseDate, DATE_ADD(purchaseDate, INTERVAL modelWarranty MONTH) warrantyDate " +
        "FROM Item LEFT JOIN Model USING (productId) LEFT JOIN  Request USING (itemId) " +
        "WHERE customerId = %d " +
        "ORDER BY purchaseDate DESC"
        % customerId,
        db.connection)
    items = [tbd for tbd in items_df.iterrows()]

    return items


def submitRequest(itemId):
    return
    # change request status, generate service if under warranty
    # no need to return anything

# -------------------------------------------------##--List of Requests Page--#-----------------------------------------------


def retrieveRequests(customerId):
    return
    # return all products with A REQUEST in the form of an array, consisting of requests objects

    # requests object should have requestsid, request date, service fee, request status, itemid

    # return array should be sorted by request status (cancelled at the bottom, completed at the middle, rest at the top) then by request date


def onPay(requestId): # changed from itemId to requestId
    pd.read_sql_query(
        "UPDATE REQUEST SET requestStatus = 'In progress' WHERE requestId = %s AND requestStatus = 'Submitted and Waiting for payment'"
        % requestId,
        db.connection
    )
    pd.read_sql_query(
        "UPDATE Payment SET paymentDate = CURDATE() WHERE requestId = %s"
        % requestId,
        db.connection
    )
    return
    # changes request status, generates a service


def onCancelRequest(itemId):
    return pd.read_sql_query(
        "UPDATE Request SET requestStatus = 'Canceled' WHERE itemId = %d"
        % itemId,
        db.connection)

    # change request staus to cancelled

# -------------------------------------------------##--Admin Login Page--#-----------------------------------------------
# LYN


def adminLogin(username, password):
    return
    # check against admin database that it exists and matches
    # return True

    # -------------------------------------------------##--Admin Menu Page--#-----------------------------------------------

def initialiseDatabase():
    try:
        products_json = json.load(open('data/products.json'))
        pQuery = [
            "INSERT INTO Model (categoryName, modelName, modelCost, modelPrice, modelWarranty) VALUES "]

        for product in products_json:
            pQuery.append(
                "('%s', '%s', %s, %s, %s)"
                % (product["Category"], product["Model"], product["Cost ($)"], product["Price ($)"], product["Warranty (months)"])
            )

        pd.read_sql_query(" ".join(pQuery), db.connection)

        items_json = json.load(open('data/items.json'))
        iQuery = [
            "INSERT INTO Item(itemId, powerSupply, factory, color, productionYear, purchaseStatus, productId, customerId, purchaseDate)"]

        for item in items_json:
            iQuery.append(
                "(%s, '%s', '%s', '%s', %s, '%s', %s, %s, '%s')"
                % (item["ItemId"], item["PowerSupply"], item["Factory"], item["Color"], item["ProductionYear"], item["PurchaseStatus"], item["Model"], random.randint(1, 4), "CURDATE()")
            )

        pd.read_sql_query(" ".join(iQuery), db.connection)

        return True

    except:
        return False
    # button does the populating of the database according to the PDF requirements (UNSOLD and SOLD items for each ProductID)
    # return true if successful
    # links to next method viewInventory() where view just does the display of this insertion


def viewInventory():
    return
    # upon clicking of button, it retrieves the number of UNSOLD and SOLD items for each Product ID from the database(purchase status)

    # return in the form of dictionary, key will be product ID, value will be in the form of array, array[0] is # of sold items and array[1] is # of unsold items

    # for front end side: it will display the table just like the PDF

    # -------------------------------------------------##--Product Catalogue Page --#-----------------------------------------------


def adminSearch(selection):
    return
    # selection comes in the form of a dictionary
    #{ "model": "safe1", "category": "locks",  "colour": "white", "productionYear": "2011", "factory": "Singapore", "powerSupply": "Battery"}

    # if admin does not select any filter for the category, the value of the category will be an empty string, eg category: ""

    # OF SOLD AND UNSOLD
    # return should be like this
    # arr = [[productNameVar, price, cost(service fee), # of items in stock, # of sold, warranty, [list of items objects]],[[productNameVar, price, cost(service fee), # of items in stock, # of sold, warranty, [list of items objects]] etc ...

    # BECAUSE we follow the design sent into the group drawn by hongpei sent by megan

    # -------------------------------------------------##--View Service List Page--#-----------------------------------------------
    # LYN


def requestServices():
    return
    # display all past service sorted based on service status (awaiting approval on top, in progress in the middle, completed at the bottom), then sorted by service id (decreasing order, largest which is the latest service is on top)

    # return in the form of array of service objects which has the attributes: serviceid, itemid, customerid, service status


def approveServiceRequest(serviceId):
    return
   # clicking approved checkbox will update service status to be in progress.


def completeServiceRequest(serviceId):
    return
   # clicking completed checkbox will update service status to be completed.

    # -------------------------------------------------##--View Requests (Unpaid Service Fee)--#--------------------------------------
    # LYN


def getUnpaidServiceCustomers():
    return
    # not including customers whose requests have been cancelled due to non-payment

    # include customers whose request status is "submitted and waiting for payment"

    # return in the form of array of requests objects which has requestId, requestDate, requestStatus, customerId, itemId
