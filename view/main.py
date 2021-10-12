import tkinter as tk
from view.Customer.CustomerLogin import customerLogin
from view.Admin.AdminLogin import *

def main():
  root = tk.Tk()
  root.title("Welcome To The Shop")
  root.geometry("800x800")
  root.configure(bg="#f9f9f8")

  global customerID
  customerID = 1

  # Redirect to Customer Login Page
  def redirectToCustomer():
    root.destroy()
    # from Customer.CustomerLogin import customerLogin
    customerLogin()

  # Redirect to Admin Login Page
  def redirectToAdmin():
    root.destroy()
    adminLogin()
    
  tk.Button(text="Customer", bg='#fbf2fa', command = redirectToCustomer, width = 20).place(relx=0.5, rely=0.3, anchor=tk.CENTER)
  tk.Button(text="Admin", bg='#fbf2fa', command = redirectToAdmin, width = 20).place(relx=0.5, rely=0.4, anchor=tk.CENTER)

  root.mainloop()
  
main()