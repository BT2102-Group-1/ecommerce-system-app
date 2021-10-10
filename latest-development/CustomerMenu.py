import tkinter as tk
from ListOfRequest import *
from ProductSearch import *
from PurchaseHistory import *
from RequestService import *
from main import *

def customerMenu():
  window = tk.Tk()
  window.title("Customer Menu")
  window.geometry("500x500")

  # Redirect to Product Search Page
  def redirectToProductSearch():
    window.destroy()
    productSearch()

  # Redirect to PurchaseHistory Page
  def redirectToPurchaseHistory():
    window.destroy()
    purchaseHistory()

  # Redirect to List Of Request
  def redirectToListOfRequest():
    window.destroy()
    listOfRequest()

  # Redirect to Request History Page
  def redirectToRequestService():
    window.destroy()
    requestService()

  # Redirect to Main.py
  def redirectToMain():
    window.destroy()
    from main import main
    main()

  tk.Button(text="Product Search", command = redirectToProductSearch, width = 30).pack(pady = 5)

  tk.Button(text="Purchase History", command = redirectToPurchaseHistory, width = 30).pack(pady = 5)

  tk.Button(text="Request Service", command = redirectToRequestService, width = 30).pack(pady = 5)

  tk.Button(text="List of Request", command = redirectToListOfRequest, width = 30).pack(pady = 5)

  tk.Button(text="Logout", command = redirectToMain, width = 20).pack(pady = 5)

  window.mainloop()