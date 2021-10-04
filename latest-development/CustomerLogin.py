import tkinter as tk
from tkinter import messagebox
from CustomerRegister import *
from main import *
from PurchaseHistory import *

def customerLogin():

  window = tk.Tk()
  window.title("Customer Login")
  window.geometry("500x500")
  #add frame
  frame = tk.LabelFrame(window, text="Customer Login ", padx=20, pady=20)
  frame.pack()
  #frame heading
  #frame.heading = ('Customer Log in page')
  #title = tk.Label(frame, text = "Customer Login")
  #title.pack()

  #for text variable
  username_verification = tk.StringVar() 
  password_verification = tk.StringVar()

  #print email address
  username_label = tk.Label(frame, text = "Email address").pack()
  #input box for email
  username = tk.Entry(frame, text = "Email address", width=10, textvariable= username_verification).pack()

  #print password 
  password_label = tk.Label(frame, text = "Password").pack()
  #input box for password
  password = tk.Entry(frame, text = "Password", width=10, textvariable = password_verification).pack()


  # verification - need change this 
  def verifyLogin():
    if (not username_verification.get() or not password_verification.get()):
      tk.messagebox.showerror("Login Unsuccessful","Error. Please ensure all fields are filled.")
    #customerID = backend(username_verification.get(), password_verification.get())
    #customerID = 1
    if (customerID >= 0):
      redirectToCustomerHome()
    else:
      tk.messagebox.showerror("Login Unsuccessful","Error. Please check your email address or password again.")

  #need redirect to product search page 
  def redirectToCustomerHome():
    root.destroy()
    productSearch()

  #login button
  loginButton = tk.Button(frame, text = "Log In", command = verifyLogin)
  loginButton.pack()

  #register button
  register = tk.Label(frame,text = "No Account? Register now!")
  register.pack()

  def registernow():
    window.destroy()
    customerRegister()

  registerButton = tk.Button(frame, text = "Register Here", command = registernow)
  registerButton.pack()
  
  window.mainloop()

