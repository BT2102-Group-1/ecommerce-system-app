import tkinter as tk
from CustomerLogin import *
from Admin.AdminLogin import *
from ProductSearch import *

def main():
  root = tk.Tk()
  root.title("Welcome To The Shop")
  root.geometry("500x500")

  # Redirect to Customer Login Page
  def redirectToCustomer():
    root.destroy()
    customerLogin()

  # Redirect to Admin Login Page
  def redirectToAdmin():
    root.destroy()
    adminLogin()

  def redirectToProductSearch():
    root.destroy()
    productSearch()
    
  tk.Button(text="Customer", command = redirectToCustomer).place(relx=0.5, rely=0.3, anchor=tk.CENTER)
  tk.Button(text="Admin", command = redirectToAdmin).place(relx=0.5, rely=0.4, anchor=tk.CENTER)
  tk.Button(text="Product Search", command = redirectToProductSearch).place(relx=0.5, rely=0.5, anchor=tk.CENTER)

  root.mainloop()
  
main()