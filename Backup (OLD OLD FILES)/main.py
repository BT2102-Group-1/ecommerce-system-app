import tkinter as tk
from administrator.test import MyFirstGUI

root = tk.Tk()

def adminLoginPage():
  root.destroy()
  import administrator.adminlogin

def customerLoginPage():
  root.destroy()
  import customer.customerlogin

def requestService():
  root.destroy()
  import customer.requestservice

def purchaseHistory():
  root.destroy()
  import customer.purchasehistory

def NavBar():
  root.destroy()
  import customer.navbar

def productSearch():
  root.destroy()
  import customer.productsearch

#my_first_gui = MyFirstGUI(root)

def test():
  root.destroy()
  import customer.test

customerButton = tk.Button(root, text="Customer", command = customerLoginPage).pack()

administratorButton = tk.Button(root, text="Administrator", command=adminLoginPage).pack()

#purchase_history_button = tk.Button(root, text="Purchase History", command=purchaseHistory).pack()

navbar_button = tk.Button(root, text="NavBar", command=NavBar).pack()

product_search_button = tk.Button(root, text="Product Search", command=productSearch).pack()

test_button = tk.Button(root, text="Test", command=test).pack()

root.mainloop()