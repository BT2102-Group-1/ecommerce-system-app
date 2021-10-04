from sqlalchemy import create_engine
from sqlalchemy.sql import text
import pandas as pd
import numpy as np

class Connection:
    def __init__(self):
        self.engine = create_engine('mysql+mysqlconnector://root:password@localhost/oshes', connect_args={'use_pure': True})
        self.connection = self.engine.connect()

if __name__ == '__main__':
    db = Connection()
    print(db.engine)
    # print(pd.read_sql('customer', db.connection))
    # print(pd.read_sql_query('SELECT * FROM Customer WHERE gender = "F"', db.connection))

    # insert = pd.DataFrame(np.array([['Lyn Tan', 'F', '123 Tiong Bahru Rd', 'hihi@jeno.com', 'cpassword', '92969405']]), columns=['name', 'gender', 'address', 'email', 'password', 'phoneNo']) 
    # insert.to_sql('customer', db.connection, if_exists='append', index_label='customerId') # write “customers” to database
    # print(pd.read_sql('customer', db.connection))

#-------------------------------------------------##--Customer Login Page--#------------------------------------------------------
# Return generated customerId for successful login
# Return -1 for unsuccessful login (i.e. customer doesn't exist)
# we will use this customerId as global variable to be used later as our parameter values
def customerLogin(self, email, password):
  
  # check against customer database that it exists and matches
  result = pd.read_sql_query('SELECT customerId FROM Customer WHERE email = "%s" AND password = "%s"' % (email, password), self.connection)

  if (result.empty):
    return -1
  
  return result['customerId'][0]

#-------------------------------------------------##--Customer Registration Page--#-----------------------------------------------
# Return generated customerId for successful registration
# Return -1 for unsuccessful registration
def registerCustomer(self, email, password, name, address, phoneNo, gender):
  # validation check - email must not exist in database
  checkIfEmailExists = pd.read_sql_query('SELECT customerId FROM Customer WHERE email = "%s"' % email, self.connection)
  if (not checkIfEmailExists.empty):
    return -1

  # create customer in database + generate customerId on your end
  newCustomer = pd.DataFrame(np.array([[name, gender, address, email, password, phoneNo]]), columns=['name', 'gender', 'address', 'email', 'password', 'phoneNo']) 
  newCustomer.to_sql('Customer', self.connection, if_exists='append', index_label='customerId') # write “newCustomer” to database

  newCustomerId = pd.read_sql_query('SELECT customerId FROM Customer WHERE email = "%s"' % email, self.connection)
  
  # If writing to database unsuccessful, return -1
  if (newCustomerId.empty):
    return -1
  
  return newCustomerId['customerId'][0]
    
# -------------------------------------------------##--Product Search Page--#-----------------------------------------------------
def customerSearch(selection):
  # selection comes in the form of a dictionary
  #{ "model": "safe1", "category": "locks",  "colour": "white", "productionYear": "2011", "factory": "Singapore", "powerSupply": "Battery"}

  # if user does not select any filter for the category, the value of the category will be an empty string, eg category: "" 

  #ONLY OF UNSOLD!! 
  # return should be like this
  # arr = [[productNameVar, price, # of items in stock, warranty, [list of items objects]],[[productNameVar, price, # of items in stock, warranty, [list of items objects]],[[productNameVar, price, # of items in stock, warranty, [list of items objects]] etc ...
  # BECAUSE we follow the design sent into the group drawn by hongpei sent by megan 

  #----- for front end ------# 
  # card.title = arr[0]
  # for n in range(len(arr[0].[3])):
  #   Label(main, text=arr[0].[3].name)

#frontend method, backend ignore!!!!!!
def settlePurchase():
  #frontend side
  itemId = # get from front end side
  date = # get from front end side
  if not purchase(itemId, customerId, date):
    # throw error on frontend
  
  # take note of refresh (frontend)

def purchase(itemId, customerId, date):
  # edit attributes of the item in the database - change unsold to sold and input customerId, record purchase date (impt for servicing later)

  # return true if successful, false otherwise (in any case where there are two customers viewing a product, one bought alr but not enough time to update in the product page and hence, the 2nd customer click yeet)

# -------------------------------------------------##--Purchase History Page--#-----------------------------------------------
def getPurchaseHistory(customerId):
   # return all products bought by customer in the form of an array, consisting of item objects sorted base on purchase date (latest at the top)

  # item object should have itemid, price, model name, category, production year, colour, factory, powersupply, purchaseDate 

# -------------------------------------------------##--Request Service Page--#-----------------------------------------------
def getUnrequestedItems(customerId):
  # return all products bought by customer which DOES NOT HAVE A SERVICE REQUESTED OR HAD A MOST RECENT REQUEST WITH REQUEST STATUS AS CANCELLED OR COMPLETED in the form of an array, consisting of item objects 

  # suggested METHOD: find items purchased then query requests based on the itemId -> just shows the requests for that itemId, since requestId will be incremented in increasing order, can get the largest requestId and check status 

  # item object should have itemid, model name, purchaseDate, serviceFee, warranty (you can give us extra attributes if it is more convenient for your implementation) -- possible to give us warranty end date? 

def submitRequest(itemId):
  # change request status, generate service if under warranty
  # no need to return anything

# -------------------------------------------------##--List of Requests Page--#-----------------------------------------------
def retrieveRequests(customerId):
  # return all products with A REQUEST in the form of an array, consisting of requests objects

  # requests object should have requestsid, request date, service fee, request status, itemid

  # return array should be sorted by request status (cancelled at the bottom, completed at the middle, rest at the top) then by request date


def onPay(itemId):
  # changes request status, generates a service 

def onCancelRequest(itemId):
  # change request staus to cancelled 

# -------------------------------------------------##--Admin Login Page--#-----------------------------------------------
# Returns True if admin name exists and password matches
# Returns False otherwise (i.e. unsuccessful login)
def adminLogin(self, adminId, password):
  # check against admin database that it exists and matches
  result = pd.read_sql_query('SELECT adminId FROM Administrator WHERE adminId = "%s" AND password = "%s"' % (adminId, password), self.connection)

  if (result.empty):
    return False
  
  return True
 
# -------------------------------------------------##--Admin Menu Page--#-----------------------------------------------

def initialiseDatabase():
  # button does the populating of the database according to the PDF requirements (UNSOLD and SOLD items for each ProductID)
  # return true if successful
  # links to next method viewInventory() where view just does the display of this insertion

def viewInventory():
  # upon clicking of button, it retrieves the number of UNSOLD and SOLD items for each Product ID from the database(purchase status)
  
  # return in the form of dictionary, key will be product ID, value will be in the form of array, array[0] is # of sold items and array[1] is # of unsold items
  
  # for front end side: it will display the table just like the PDF

# -------------------------------------------------##--Product Catalogue Page --#-----------------------------------------------

def adminSearch(selection):
  # selection comes in the form of a dictionary
  #{ "model": "safe1", "category": "locks",  "colour": "white", "productionYear": "2011", "factory": "Singapore", "powerSupply": "Battery"}

  # if admin does not select any filter for the category, the value of the category will be an empty string, eg category: "" 

  #OF SOLD AND UNSOLD 
  # return should be like this
  # arr = [[productNameVar, price, cost(service fee), # of items in stock, # of sold, warranty, [list of items objects]],[[productNameVar, price, cost(service fee), # of items in stock, # of sold, warranty, [list of items objects]] etc ...
  
  # BECAUSE we follow the design sent into the group drawn by hongpei sent by megan 

# -------------------------------------------------##--View Service List Page--#-----------------------------------------------
# Display all past service sorted based on service status (awaiting approval on top, in progress in the middle, completed at the bottom), 
# then sorted by service id (decreasing order, largest which is the latest service is on top)
# Return a dataframe of services which have the columns: serviceid, itemid, customerid, service status
def requestServices(self):
    return pd.read_sql_query('''SELECT s.serviceId, r.itemId, r.customerId, s.serviceStatus FROM Service AS s INNER JOIN Request AS r ON s.requestId = r.requestId
                                    ORDER BY FIELD(s.serviceStatus,'Waiting for approval', 'In progress', 'Completed'), s.serviceId DESC''', self.connection)

def approveServiceRequest(serviceId):
   # clicking approved checkbox will update service status to be in progress.
  
def completeServiceRequest(serviceId):
   # clicking completed checkbox will update service status to be completed.

# -------------------------------------------------##--View Requests (Unpaid Service Fee)--#--------------------------------------
# not including customers whose requests have been cancelled due to non-payment
# include customers whose request status is "submitted and waiting for payment"
# Return a dataframe of requests which have columns requestId, requestDate, requestStatus, customerId, itemId
def getUnpaidServiceCustomers(self):
  
  return pd.read_sql_query('SELECT requestId, requestDate, requestStatus, customerId, itemId FROM oshes.Request WHERE requestStatus = "Submitted and Waiting for payment"', self.connection)
  
