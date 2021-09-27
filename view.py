# interface 

##--Customer Login Page--#------------------------------------------------------
def customerLogin(username, password):
  # check against customer database that it exists and matches

  # return generated customerId
  # -1 means unsuccessful login (customer don't exist)
  
 # we will use this customerId as global variable to be used later as our parameter values

##--Customer Registration Page--#-----------------------------------------------
def registerCustomer(email, password, name, address, phoneNo, gender):
  # validation checks
  # - email must not exist in database
  # create customer in database + generate customerId on your end
  # return generated customerId
  # -1 means unsuccessful login
    
##--Product Search Page--#-----------------------------------------------------
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

##--Purchase History Page--#-----------------------------------------------
def getPurchaseHistory(customerId):
   # return all products bought by customer in the form of an array, consisting of item objects sorted base on purchase date (latest at the top)

  # item object should have itemid, price, model name, category, production year, colour, factory, powersupply, purchaseDate 

##--Request Service Page--#-----------------------------------------------
def getUnrequestedItems(customerId):
  # return all products bought by customer which DOES NOT HAVE A SERVICE REQUESTED OR HAD A MOST RECENT REQUEST WITH REQUEST STATUS AS CANCELLED OR COMPLETED in the form of an array, consisting of item objects 

  # suggested METHOD: find items purchased then query requests based on the itemId -> just shows the requests for that itemId, since requestId will be incremented in increasing order, can get the largest requestId and check status 

  # item object should have itemid, model name, purchaseDate, serviceFee, warranty (you can give us extra attributes if it is more convenient for your implementation) -- possible to give us warranty end date? 

def submitRequest(itemId):
  # change request status, generate service if under warranty
  # no need to return anything

##--List of Requests Page--#-----------------------------------------------
def retrieveRequests(customerId):
  # return all products with A REQUEST in the form of an array, consisting of requests objects

  # requests object should have requestsid, request date, service fee, request status, itemid

  # return array should be sorted by request status (cancelled at the bottom, completed at the middle, rest at the top) then by request date


def onPay(itemId):
  # changes request status, generates a service 

def onCancelRequest(itemId):
  # change request staus to cancelled 

##--Admin Login Page--#-----------------------------------------------

def adminLogin(username, password):
  # check against admin database that it exists and matches
  # return True
 
##--Admin Menu Page--#-----------------------------------------------

def initialiseDatabase():
  # button does the populating of the database according to the PDF requirements (UNSOLD and SOLD items for each ProductID)
  # return true if successful
  # links to next method viewInventory() where view just does the display of this insertion

def viewInventory():
  # upon clicking of button, it retrieves the number of UNSOLD and SOLD items for each Product ID from the database(purchase status)
  
  # return in the form of dictionary, key will be product ID, value will be in the form of array, array[0] is # of sold items and array[1] is # of unsold items
  
  # for front end side: it will display the table just like the PDF

##--Product Catalogue Page --#-----------------------------------------------

def adminSearch(selection):
  # selection comes in the form of a dictionary
  #{ "model": "safe1", "category": "locks",  "colour": "white", "productionYear": "2011", "factory": "Singapore", "powerSupply": "Battery"}

  # if admin does not select any filter for the category, the value of the category will be an empty string, eg category: "" 

  #OF SOLD AND UNSOLD 
  # return should be like this
  # arr = [[productNameVar, price, cost(service fee), # of items in stock, # of sold, warranty, [list of items objects]],[[productNameVar, price, cost(service fee), # of items in stock, # of sold, warranty, [list of items objects]] etc ...
  
  # BECAUSE we follow the design sent into the group drawn by hongpei sent by megan 

##--View Service List Page--#-----------------------------------------------

def requestServices():
  # display all past service sorted based on service status (awaiting approval on top, in progress in the middle, completed at the bottom), then sorted by service id (decreasing order, largest which is the latest service is on top)

  # return in the form of array of service objects which has the attributes: serviceid, itemid, customerid, service status
  
def approveServiceRequest(serviceId):
   # clicking approved checkbox will update service status to be in progress.
  
def completeServiceRequest(serviceId):
   # clicking completed checkbox will update service status to be completed.

##--View Requests (Unpaid Service Fee)--#--------------------------------------
def getUnpaidServiceCustomers():
  # not including customers whose requests have been cancelled due to non-payment

  # include customers whose request status is "submitted and waiting for payment"

  # return in the form of array of requests objects which has requestId, requestDate, requestStatus, customerId, itemId
  
