import tkinter as tk
from Admin.AdminViewInventory import *
from Admin.AdminServiceList import *
from Admin.AdminUnpaidRequest import *

def adminMenu():
  window = tk.Tk()
  window.title("Admin Menu")
  window.geometry("500x500")

  #Function to Initialise Database (NO REDIRECT)
  def redirectToInitialiseDatabase():
    window.destroy()
    initialiseDatabase()

  # Redirect to View Inventory Page
  def redirectToViewInventory():
    window.destroy()
    adminViewInventory()

  # Redirect to Product Catalogue Page
  def redirectToProductCatalogue():
    window.destroy()
    adminProductCatalogue()

  # Redirect to View Service List Page
  def redirectToViewServiceList():
    window.destroy()
    adminServiceList()

  # Redirect to View Requests with Unpaid Service Fee Page
  def redirectToViewRequests():
    window.destroy()
    adminUnpaidRequest()

  # Redirect to Main.py
  def redirectToMain():
    window.destroy()
    from main import main
    main()

  tk.Button(text="Initialise Database", command = redirectToInitialiseDatabase, width = 30).pack(pady = 5)

  tk.Button(text="View Inventory", command = redirectToViewInventory, width = 30).pack(pady = 5)

  tk.Button(text="Product Catalogue", command = redirectToProductCatalogue, width = 30).pack(pady = 5)

  tk.Button(text="View Service List", command = redirectToViewServiceList, width = 30).pack(pady = 5)

  tk.Button(text="View Requests (Unpaid Service Fee)", command = redirectToViewRequests, width = 30).pack(pady = 5)

  tk.Button(text="Logout", command = redirectToMain, width = 20).pack(pady = 5)

  window.mainloop()