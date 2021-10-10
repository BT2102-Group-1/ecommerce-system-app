import tkinter as tk
from tkinter import ttk
from RequestService import *
# from main import *
import main as mainpage
from CustomerMenu import *


def customerRegister():
  root = tk.Tk()
  root.geometry("500x500")
  frame = tk.LabelFrame(root, text="Customer Register ", padx=20, pady=20)
  frame.grid(row=0, column=0)

  email_input, pw_input, name_input, address_input, phoneno_input = (tk.StringVar() for i in range(5))

  # Input Email
  tk.Label(frame, text="Email").grid(row=1, column=0)
  tk.Entry(frame, textvariable = email_input).grid(row=1, column=1)

  # Input Password
  tk.Label(frame, text="Password").grid(row=2, column=0)
  tk.Entry(frame, textvariable = pw_input).grid(row=2, column=1)

  # Input Name
  tk.Label(frame, text="Name").grid(row=3, column=0)
  tk.Entry(frame, textvariable = name_input).grid(row=3, column=1)

  # Input Address
  tk.Label(frame, text="Address").grid(row=4, column=0)
  tk.Entry(frame, textvariable = address_input).grid(row=4, column=1)

  # Input Phone Number
  tk.Label(frame, text="Phone Number").grid(row=5, column=0)
  tk.Entry(frame, textvariable = phoneno_input).grid(row=5, column=1)

  # Selection of Gender
  tk.Label(frame, text="Gender").grid(row=6, column=0)

  # Gender Options
  options = [
    " ", "M", "F"
  ]

  # Dropdown Menu of Gender Selections
  gender_dropdown = ttk.Combobox(frame, state="readonly",value=options)
  gender_dropdown.current(0)
  gender_dropdown.bind("<<ComboboxSelected>>")
  gender_dropdown.grid(row=6, column=1)

  # Verify that all fields are filled in
  def registering():
    if not email_input.get() or not pw_input.get() or not name_input.get() or not address_input.get() or not phoneno_input.get() or gender_dropdown.get() == " ":
      tk.messagebox.showerror(" Unsuccessful","Error. Please make sure all fields are filled.")
    else: 
      registernow()

  # Register a customer
  def registernow():
    # Store as global variable
    customerID = mainpage.customerID

    # Backend Registering of Customer
    # customerID = backend(email_input.get(), pw_input.get(), name_input.get(), address_input.get(), phoneno_input.get(), gender_dropdown.get())
    if (customerID >=0):
      root.destroy()
      customerMenu()
    else: 
      tk.messagebox.showerror(" Unsuccessful","Error. Email already has an existing account")

  registerButton = tk.Button(frame, text = "Register", command = registering)
  registerButton.grid(row=7, column=2)

  frame.mainloop()

