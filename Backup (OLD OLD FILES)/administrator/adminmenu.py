import tkinter as tk

admin_menu_main = tk.Tk()
admin_menu_main.title("Admin Menu")

menu_frame = tk.LabelFrame(admin_menu_main, text="Admin Menu", padx=50, pady=50)
menu_frame.pack(padx=10, pady=10)

def initialiseDatabase():
  print("Initialising Database")

def viewInventory():
  admin_menu_main.destroy()
  import administrator.viewinventory

def viewProductCatalogue():
  print("View Product Catalogue")

def viewServiceList():
  print("View service list")  

def viewUnpaidRequests():
  print("View requests with unpaid service fees") 

initialise_database_button = tk.Button(menu_frame, text = "Initialise Database", command = initialiseDatabase, width = 30).pack(pady = 5)

view_inventory_button = tk.Button(menu_frame, text = "View Inventory", command = viewInventory, width = 30).pack(pady = 5)

view_product_catalogue = tk.Button(menu_frame, text = "Product Catalogue", command = viewProductCatalogue, width = 30).pack(pady = 5)

view_service_list_button = tk.Button(menu_frame, text = "View Service List", command = viewServiceList, width = 30).pack(pady = 5)

view_unpaid_requests_button = tk.Button(menu_frame, text = "View Requests (Unpaid Service Fees)", command = viewUnpaidRequests, width = 30).pack(pady = 5)

admin_menu_main.mainloop()