import tkinter as tk
from tkinter import messagebox
import main as mainpage
from CustomerRegister import *
from CustomerMenu import *

def customerLogin():
  window = tk.Tk()
  window.title("Customer Login")
  window.geometry("500x500")

  # Add Frame
  frame = tk.LabelFrame(window, text="Customer Login ", padx=20, pady=20)
  frame.pack()

  # Text variable
  username_verification = tk.StringVar() 
  password_verification = tk.StringVar()

  customerID = mainpage.customerID

  # Print email address
  username_label = tk.Label(frame, text = "Email address").pack()

  # Input box for email
  username = tk.Entry(frame, text = "Email address", width=10, textvariable= username_verification).pack()

  # Print password 
  password_label = tk.Label(frame, text = "Password").pack()

  # Input box for password
  password = tk.Entry(frame, text = "Password", width=10, textvariable = password_verification).pack()

  # Verification - need change this 
  def verifyLogin():
    # if (not username_verification.get() or not password_verification.get()):
    #   tk.messagebox.showerror("Login Unsuccessful","Error. Please ensure all fields are filled.")
    if (customerID >= 0):
      redirectToCustomerHome()
    elif(not username_verification.get() or not password_verification.get()):
      tk.messagebox.showerror("Login Unsuccessful","Error. Please check your email address or password again.")

  # Redirect to Menu Page 
  def redirectToCustomerHome():
    #customerID = backend(username_verification.get(), password_verification.get())
    # print(customerID)
    window.destroy()
    customerMenu()
    
  # Login button
  loginButton = tk.Button(frame, text = "Log In", command = verifyLogin)
  loginButton.pack()

  tk.Label(frame,text = " ").pack()

  # Register button
  register = tk.Label(frame,text = "No Account? Register now!")
  register.pack()

  # Redirect to Register Page 
  def registernow():
    window.destroy()
    customerRegister()

  registerButton = tk.Button(frame, text = "Register Here", command = registernow)
  registerButton.pack()
  
  window.mainloop()

