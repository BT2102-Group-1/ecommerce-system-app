import pandas as pd
import numpy as np
import random
import json
from datetime import datetime, timedelta

from sqlalchemy import create_engine
from sqlalchemy.sql import text


class Connection:
    def __init__(self):
        self.engine = create_engine(
            'mysql+mysqlconnector://root:password@localhost/oshes', connect_args={'use_pure': True})
        self.connection = self.engine.connect()


    # -------------------------------------------------##--Customer Login Page--#------------------------------------------------------
    # Return generated customerId for successful login
    # Return -1 for unsuccessful login (i.e. customer doesn't exist)
    # we will use this customerId as global variable to be used later as our parameter values


    def customerLogin(self, email, password):

        # check against customer database that it exists and matches
        result = pd.read_sql_query('SELECT customerId FROM Customer WHERE email = "%s" AND password = "%s"' % (
            email, password), self.connection)

        if (result.empty):
            return -1

        return result['customerId'][0]

    # -------------------------------------------------##--Customer Registration Page--#-----------------------------------------------
    # Return generated customerId for successful registration
    # Return -1 for unsuccessful registration


    def registerCustomer(self, email, password, name, address, phoneNo, gender):
        # validation check - email must not exist in database
        checkIfEmailExists = pd.read_sql_query(
            'SELECT customerId FROM Customer WHERE email = "%s"' % email, self.connection)
        if (not checkIfEmailExists.empty):
            return -1

        # create customer in database + generate customerId on your end
        newCustomer = pd.DataFrame(np.array([[name, gender, address, email, password, phoneNo]]), columns=[
                                'name', 'gender', 'address', 'email', 'password', 'phoneNo'])
        newCustomer.to_sql('Customer', self.connection, if_exists='append',
                        index_label='customerId')  # write 'newCustomer' to database

        newCustomerId = pd.read_sql_query(
            'SELECT customerId FROM Customer WHERE email = "%s"' % email, self.connection)

        # If writing to database unsuccessful, return -1
        if (newCustomerId.empty):
            return -1

        return newCustomerId['customerId'][0]

    # -------------------------------------------------##--Product Search Page--#-----------------------------------------------------


    def customerSearch(self, selection):
        # selection comes in the form of a dictionary
        #{ "model": "safe1", "category": "locks",  "colour": "white", "productionYear": "2011", "factory": "Singapore", "powerSupply": "Battery"}

        # if user does not select any filter for the category, the value of the category will be an empty string, eg category: ""

        # ONLY OF UNSOLD!!
        # return should be like this
        # arr = [[productNameVar, price, # of items in stock, warranty, [list of items objects]],[[productNameVar, price, # of items in stock, warranty, [list of items objects]],[[productNameVar, price, # of items in stock, warranty, [list of items objects]] etc ...
        # BECAUSE we follow the design sent into the group drawn by hongpei sent by megan

        #----- for front end ------#
        # card.title = arr[0]
        # for n in range(len(arr[0].[3])):
        #   Label(main, text=arr[0].[3].name)

        # frontend method, backend ignore!!!!!!
        return


    def purchase(self, itemId, customerId):
            # edit attributes of the item in the database - change unsold to sold and input customerId, record purchase date (impt for servicing later)
            # check if item is sold
        item_df = pd.read_sql_query(
            '''SELECT i.itemId FROM Item i WHERE i.itemId = "%d" AND i.purchaseStatus = "Unsold"''' % (itemId))
        if not item_df.empty:
            pd.read_sql_query('''   UPDATE Item i
                                    SET i.purchaseStatus = "Sold", i.customerId = "%d", i.purchaseDate = CURDATE()
                                    WHERE i.itemId = "%d" AND i.purchaseStatus != "Sold"''' % (itemId, customerId), self.connection)
            return True
        else:
            return False
        # return true if successful, false otherwise (in any case where there are two customers viewing a product, one bought alr but not enough time to update in the product page and hence, the 2nd customer click yeet)

    # -------------------------------------------------##--Purchase History Page--#-----------------------------------------------


    def getPurchaseHistory(self, customerId):
        # return all products bought by customer in the form of an array, consisting of item objects sorted base on purchase date (latest at the top)

        # item object should have itemid, price, model name, category, production year, colour, factory, powersupply, purchaseDate
        return pd.read_sql_query('''SELECT itemId, modelPrice, modelName, categoryName, productionYear, color, factory, powerSupply, purchaseDate 
                                    FROM Item LEFT JOIN Model USING (productId) WHERE customerId = 1 ORDER BY purchaseDate DESC''' % customerId, self.connection)

    # -------------------------------------------------##--Request Service Page--#-----------------------------------------------


    def getUnrequestedItems(self, customerId):
        # return all products bought by customer which DOES NOT HAVE A SERVICE REQUESTED OR HAD A MOST RECENT REQUEST WITH REQUEST STATUS AS CANCELLED OR COMPLETED in the form of an array, consisting of item objects
        # suggested METHOD: find items purchased then query requests based on the itemId -> just shows the requests for that itemId, since requestId will be incremented in increasing order, can get the largest requestId and check status
        # item object should have itemid, model name, purchaseDate, serviceFee, warranty (you can give us extra attributes if it is more convenient for your implementation) -- possible to give us warranty end date?
        return pd.read_sql_query(
            '''SELECT itemId, modelName, modelCost, modelWarranty, purchaseDate, DATE_ADD(purchaseDate, INTERVAL modelWarranty MONTH) warrantyDate 
            FROM Item LEFT JOIN Model USING (productId) LEFT JOIN  Request USING (itemId) 
            WHERE customerId = %d ORDER BY purchaseDate DESC''' % customerId, self.connection)


    def submitRequest(self, customerId, itemId):
        # change request status, generate service if under warranty
        # no need to return anything

        requestStatus = "Submitted"

        item_df = pd.read_sql_query(''' SELECT i.purchaseDate, m.modelCost, m.modelWarranty, r.requestId
                                        FROM Item i
                                        INNER JOIN Model m ON i.productId = m.productId
                                        INNER JOIN Request r ON i.itemId = r.itemId
                                        WHERE i.itemId = "(%d)" 
                                        ''' % (itemId),
                                    db.connection,
                                    parse_dates=['purchaseDate'])
        # if warranty has expired, create payment
        if (datetime.now() + timedelta(months=item_df["modelWarranty"])) > item_df["purchaseDate"]:
            requestId = item_df["requestId"]
            serviceFee = 40.00 + 0.2 * item_df["modelCost"]
            pd.read_sql_query('''   INSERT INTO Payment (requestId, serviceFee, paymentDate)
                                    VALUES (%s, %s, CURDATE())'''
                            % (requestId, '{0:.2f}'.format(serviceFee)),
                            self.connection)
            requestStatus = "Submitted and Waiting for payment"
        # generate request
        pd.read_sql_query('''   INSERT INTO REQUEST (requestDate, requestStatus, customerId, itemId)
                                VALUES (CURDATE(), %s, %d, %d)'''
                        % (requestStatus, customerId, itemId),
                        self.connection)
        # generate service
        pd.read_sql_query('''   INSERT INTO Service(serviceStatus, adminId, requestId)
                                VALUES ("Waiting for approval", NULL, (SELECT requestId FROM Request WHERE itemId = "%d"))''' % (itemId),
                        self.connection)

    # -------------------------------------------------##--List of Requests Page--#-----------------------------------------------


    def retrieveRequests(self, customerId):
        # return all products with A REQUEST in the form of an array, consisting of requests objects
        return pd.read_sql_query(''' SELECT r.requestId, r.requestDate, p.serviceFee, r.requestStatus, r.itemId FROM Request r LEFT JOIN Payment p ON r.requestId = p.requestId WHERE r.customerId = "%d" ORDER BY FIELD(r.requestStatus, 
                                            "Submitted", 
                                            "Submitted and Waiting for payment",
                                            "In progress",
                                            "Approved",
                                            "Completed", 
                                            "Cancelled"''' % (customerId),
                                self.connection)


    def onPay(self, requestId):  # changed from itemId to requestId
        # changes request status, generates a service
        pd.read_sql_query(
            '''UPDATE REQUEST SET requestStatus = 'In progress' WHERE requestId = %s AND requestStatus = 'Submitted and Waiting for payment' '''
            % requestId,
            self.connection
        )
        pd.read_sql_query(
            '''UPDATE Payment SET paymentDate = CURDATE() WHERE requestId = %s'''
            % requestId,
            self.connection
        )
        return


    def onCancelRequest(self, itemId):
        # change request staus to cancelled
        return pd.read_sql_query(
            '''UPDATE Request SET requestStatus = 'Canceled' WHERE itemId = %d'''
            % itemId,
            self.connection)


    # -------------------------------------------------##--Admin Login Page--#-----------------------------------------------
    # Returns True if admin name exists and password matches
    # Returns False otherwise (i.e. unsuccessful login)
    def adminLogin(self, adminId, password):
        # check against admin database that it exists and matches
        result = pd.read_sql_query('SELECT adminId FROM Administrator WHERE adminId = "%s" AND password = "%s"' % (
            adminId, password), self.connection)

        if (result.empty):
            return False

        return True

    # -------------------------------------------------##--Admin Menu Page--#-----------------------------------------------


    def initialiseDatabase(self):
        # button does the populating of the database according to the PDF requirements (UNSOLD and SOLD items for each ProductID)
        # return true if successful
        # links to next method viewInventory() where view just does the display of this insertion
        try:
            products_json = json.load(open('data/products.json'))
            pQuery = [
                "INSERT INTO Model (categoryName, modelName, modelCost, modelPrice, modelWarranty) VALUES "]

            for product in products_json:
                pQuery.append(
                    "('%s', '%s', %s, %s, %s)"
                    % (product["Category"], product["Model"], product["Cost ($)"], product["Price ($)"], product["Warranty (months)"])
                )

            pd.read_sql_query(" ".join(pQuery), self.connection)

            items_json = json.load(open('data/items.json'))
            iQuery = [
                "INSERT INTO Item(itemId, powerSupply, factory, color, productionYear, purchaseStatus, productId, customerId, purchaseDate)"]

            # Change item to have null CustomerId when adding in

            for item in items_json:
                iQuery.append(
                    "(%s, '%s', '%s', '%s', %s, '%s', %s, %s, '%s')"
                    % (item["ItemId"], item["PowerSupply"], item["Factory"], item["Color"], item["ProductionYear"], item["PurchaseStatus"], item["Model"], random.randint(1, 4), "CURDATE()")
                )

            pd.read_sql_query(" ".join(iQuery), self.connection)

            return True

        except:
            return False


    def viewInventory(self):
        # upon clicking of button, it retrieves the number of UNSOLD and SOLD items for each Product ID from the database(purchase status)
        # return in the form of dictionary, key will be product ID, value will be in the form of array, array[0] is # of sold items and array[1] is # of unsold items
        # for front end side: it will display the table just like the PDF
        return pd.read_sql_query(
            '''SELECT table1.iid AS 'ProductID', table1.sold AS 'Number of "SOLD" items', table2.unsold AS 'Number of "UNSOLD" items'
            FROM (SELECT productId AS iid, COUNT(productId) AS sold FROM Item WHERE purchaseStatus='Sold' GROUP BY productId) AS table1
            INNER JOIN (SELECT productId AS iid, COUNT(productId) AS unsold FROM Item WHERE purchaseStatus='Unsold' GROUP BY productId) AS table2
            ON table1.iid = table2.iid;''', self.connection)
    
    # -------------------------------------------------##--Product Catalogue Page --#-----------------------------------------------


    def adminSearch(self, selection):
        # selection comes in the form of a dictionary
        #{ "model": "safe1", "category": "locks",  "colour": "white", "productionYear": "2011", "factory": "Singapore", "powerSupply": "Battery"}

        # if admin does not select any filter for the category, the value of the category will be an empty string, eg category: ""

        # OF SOLD AND UNSOLD
        # return should be like this
        # arr = [[productNameVar, price, cost(service fee), # of items in stock, # of sold, warranty, [list of items objects]],[[productNameVar, price, cost(service fee), # of items in stock, # of sold, warranty, [list of items objects]] etc ...

        # BECAUSE we follow the design sent into the group drawn by hongpei sent by megan
        return

    # -------------------------------------------------##--View Service List Page--#-----------------------------------------------
    # Display all past service sorted based on service status (awaiting approval on top, in progress in the middle, completed at the bottom),
    # then sorted by service id (decreasing order, largest which is the latest service is on top)
    # Return a dataframe of services which have the columns: serviceid, itemid, customerid, service status
    

    def requestServices(self):
        return pd.read_sql_query('''SELECT s.serviceId, r.itemId, r.customerId, s.serviceStatus FROM Service AS s INNER JOIN Request AS r ON s.requestId = r.requestId
                                        ORDER BY FIELD(s.serviceStatus,'Waiting for approval', 'In progress', 'Completed'), s.serviceId DESC''', self.connection)

    # input: int, int


    def approveServiceRequest(self, adminId, serviceId):
        # clicking approved checkbox will update service status to be in progress.
        # void function that updates serviceStatus of Service  to "In progress"
        # update request
        pd.read_sql_query('UPDATE Request r INNER JOIN Service s ON r.requestId = s.requestId SET r.requestStatus = "Approved" WHERE s.serviceId = "%d"' % (
            serviceId), db.connection)
        # update service
        return pd.read_sql_query('UPDATE Service SET serviceStatus = "In progress", adminId = "%d" WHERE serviceId = "%d"' % (adminId, serviceId), self.connection)


    def completeServiceRequest(self, serviceId):
        # clicking completed checkbox will update service status to be completed.
        # update request
        pd.read_sql_query('''   UPDATE Request r
                                INNER JOIN Service s ON r.requestId = s.requestId
                                SET r.requestStatus = "Completed"
                                WHERE s.serviceId = "%d"''' % (serviceId))
        # update service
        return pd.read_sql_query('UPDATE Service SET serviceStatus = "Completed" WHERE serviceId = "%s"' % (serviceId), self.connection)

    # -------------------------------------------------##--View Requests (Unpaid Service Fee)--#--------------------------------------
    # not including customers whose requests have been cancelled due to non-payment
    # include customers whose request status is "submitted and waiting for payment"
    # Return a dataframe of requests which have columns requestId, requestDate, requestStatus, customerId, itemId


    def getUnpaidServiceCustomers(self):
        return pd.read_sql_query('SELECT requestId, requestDate, requestStatus, customerId, itemId FROM oshes.Request WHERE requestStatus = "Submitted and Waiting for payment"', self.connection)
        

if __name__ == '__main__':
    db = Connection()
    print(db.engine)
    print(db.initialiseDatabase())
    print(db.viewInventory())
    # print(pd.read_sql('customer', db.connection))
    # print(pd.read_sql_query('SELECT * FROM Customer WHERE gender = "F"', db.connection))

    # insert = pd.DataFrame(np.array([['Lyn Tan', 'F', '123 Tiong Bahru Rd', 'hihi@jeno.com', 'cpassword', '92969405']]), columns=['name', 'gender', 'address', 'email', 'password', 'phoneNo'])
    # insert.to_sql('customer', db.connection, if_exists='append', index_label='customerId') # write 'customers' to database
    # print(pd.read_sql('customer', db.connection))
