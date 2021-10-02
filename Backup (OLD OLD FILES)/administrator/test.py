from tkinter import *
from administrator.viewinventory import Inventory

class MyFirstGUI:

    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.initialise_database_button = Button(master, text="Initialise Database", command=self.initialiseDatabase, width = 30)
        self.initialise_database_button.pack(pady = 5)

        self.view_inventory_button = Button(master, text="View Inventory", command=self.viewInventory, width = 30)
        self.view_inventory_button.pack(pady = 5)

        self.view_product_catalogue_button = Button(master, text="Product Catalogue", command=self.viewProductCatalogue, width = 30)
        self.view_product_catalogue_button.pack(pady = 5)

        self.view_service_list_button = Button(master, text="View Service List", command=self.viewServiceList, width = 30)
        self.view_service_list_button.pack(pady = 5)

        self.view_unpaid_requests_button = Button(master, text="View Requests (Unpaid Service Fees)", command=self.viewUnpaidRequests, width = 30)
        self.view_unpaid_requests_button.pack(pady = 5)

    def initialiseDatabase(self):
      print("Initialising Database")


    def viewProductCatalogue(self):
      print("View Product Catalogue")

    def viewServiceList(self):
      print("View service list")  

    def viewUnpaidRequests(self):
      print("View requests with unpaid service fees") 

