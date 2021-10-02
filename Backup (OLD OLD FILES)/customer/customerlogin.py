import tkinter as tk
from tkinter import ttk

root = tk.Tk()
frame = tk.LabelFrame(root, text="Customer Log in ", padx=20, pady=20)
frame.pack()

frame.heading = ('Customer Log in page')
title = tk.Label(frame, text = "Customer Login")
title.pack()

username_verification = password_verification = tk.StringVar()

username_label = tk.Label(frame, text = "Email address").pack()
username = tk.Entry(frame, text = "Email address", width=10, textvariable= username_verification).pack()
password_label = tk.Label(frame, text = "Password", textvariable= username_verification).pack()
password = tk.Entry(frame, text = "Password", width=10, textvariable = password_verification).pack()

def loggedin():
  correct = tk.Label(frame, text = "Hello, " + username_verification.get() + " You are logged in!")
  correct.pack()

loginButton = tk.Button(frame, text = "Log In", command = loggedin)
loginButton.pack()

register = tk.Label(frame,text = "No Account? Register now!")
register.pack()

def registernow():
  root.destroy()
  import customer.customerregistration

registerButton = tk.Button(frame, text = "Register Here", command = registernow)
registerButton.pack()

frame.mainloop()