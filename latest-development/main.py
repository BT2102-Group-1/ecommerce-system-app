import tkinter as tk

# from Admin.AdminLogin import *
from Admin.AdminMenu import *
from RequestService import *
from CustomerLogin import *
from PurchaseHistory import *
from ListOfRequest import *
from ProductSearch import *
##from navigation import *

def main():
  root = tk.Tk()
  root.title("Welcome To The Shop")
  root.geometry("500x500")

  global customerID
  customerID = 1

  # Redirect to Customer Login Page
  def redirectToCustomer():
    root.destroy()
    customerLogin()

  # Redirect to Admin Login Page
  def redirectToAdmin():
    root.destroy()
    # adminLogin()
    adminMenu()


  def redirectToProductSearch():
    root.destroy()
    productSearch()
  
  def redirectToRequestService():
    root.destroy()
    requestService()
  
  def redirectToListOfRequest():
    root.destroy()
    listOfRequests() 

  def redirectToPurchaseHistory():
    root.destroy()
    purchaseHistory() 
    
  tk.Button(text="Customer", command = redirectToCustomer).place(relx=0.5, rely=0.3, anchor=tk.CENTER)
  tk.Button(text="Admin", command = redirectToAdmin).place(relx=0.5, rely=0.4, anchor=tk.CENTER)
  tk.Button(text="Product Search", command = redirectToProductSearch).place(relx=0.5, rely=0.5, anchor=tk.CENTER)
  tk.Button(text="Request Service", command = redirectToRequestService).place(relx=0.5, rely=0.6, anchor=tk.CENTER)
  tk.Button(text="List of Request", command = redirectToListOfRequest).place(relx=0.5, rely=0.7, anchor=tk.CENTER)
  tk.Button(text="List of Request", command = redirectToPurchaseHistory).place(relx=0.5, rely=0.8, anchor=tk.CENTER)

  root.mainloop()
  
main()