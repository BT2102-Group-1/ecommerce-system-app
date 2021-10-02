import tkinter as tk
from tkinter import messagebox
from CustomerRegister import *

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

  # verification
  def verifyLogin():
    #backend(username_verification.get(), password_verification.get())
    # input backend verification, if true 
    verify = True
    if (verify):
      redirectToCustomerHome()
    else:
      messagebox.showerror("Login Unsuccessful","Error. Please check your email address or password again.")

  #need change to verification check 
  def redirectToCustomerHome():
    correct = tk.Label(frame, text = "Hello, " + username_verification.get() + "!  You are logged in!")
    correct.pack()

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

