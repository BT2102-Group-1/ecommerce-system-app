import tkinter as tk
from tkinter import ttk

from view import GlobalVariables 

from controller.controller import Connection

def customerRegister():
  root = tk.Tk()
  root.geometry("800x800")
  root.configure(bg="#F9FBF2")

  # Add Frame 
  frame = tk.LabelFrame(root, text="Customer Register ", padx=20, pady=20, bg="#F9FBF2")
  frame.grid(row=0, column=0, )

  # Variable for Input
  email_input, pw_input, name_input, address_input, phoneno_input = (tk.StringVar() for i in range(5))

  # Input Email
  tk.Label(frame, bg="#F9FBF2", text="Email").grid(row=1, column=0, sticky="W")
  tk.Entry(frame, textvariable = email_input).grid(row=1, column=1, sticky="W")
  tk.Label(frame, text=" ", bg="#F9FBF2").grid(row=2, column=0)

  # Input Password
  tk.Label(frame, text="Password", bg="#F9FBF2").grid(row=3, column=0, sticky="W")
  tk.Entry(frame, textvariable = pw_input).grid(row=3, column=1, sticky="W")
  tk.Label(frame, text=" ", bg="#F9FBF2").grid(row=4, column=0)

  # Input Name
  tk.Label(frame, text="Name", bg="#F9FBF2").grid(row=5, column=0, sticky="W")
  tk.Entry(frame, textvariable = name_input).grid(row=5, column=1, sticky="W")
  tk.Label(frame, text=" ", bg="#F9FBF2").grid(row=6, column=0)

  # Input Address
  tk.Label(frame, text="Address", bg="#F9FBF2").grid(row=7, column=0, sticky="W")
  tk.Entry(frame, textvariable = address_input).grid(row=7, column=1, sticky="W")
  tk.Label(frame, text=" ", bg="#F9FBF2").grid(row=8, column=0)

  # Input Phone Number
  tk.Label(frame, text="Phone Number", bg="#F9FBF2").grid(row=9, column=0, sticky="W")
  tk.Entry(frame, textvariable = phoneno_input).grid(row=9, column=1, sticky="W")
  tk.Label(frame, text=" ", bg="#F9FBF2").grid(row=10, column=0)

  # Selection of Gender
  tk.Label(frame, text="Gender", bg="#F9FBF2").grid(row=11, column=0, sticky="W")

  # Gender Options
  options = [
    " ", "M", "F"
  ]

  # Dropdown Menu of Gender Selections
  gender_dropdown = ttk.Combobox(frame, state="readonly",value=options)
  gender_dropdown.current(0)
  gender_dropdown.bind("<<ComboboxSelected>>")
  gender_dropdown.grid(row=11, column=1)
  tk.Label(frame, text=" ", bg="#F9FBF2").grid(row=12, column=0)

  # Verify that all fields are filled in
  def registering():
    if not email_input.get() or not pw_input.get() or not name_input.get() or not address_input.get() or not phoneno_input.get() or gender_dropdown.get() == " ":
      tk.messagebox.showerror(" Error","Register Unsuccessful. Please make sure all fields are filled.")
    else: 
      registernow()

  # Register a customer
  def registernow():
    # CALL BACKEND --------------------------
    # Register Customer --> method below
    GlobalVariables.customerID = Connection().registerCustomer(email_input.get(), pw_input.get(), name_input.get(), address_input.get(), phoneno_input.get(), gender_dropdown.get())

    if (GlobalVariables.customerID >=0):
      root.destroy()
      from view.Customer.CustomerMenu import customerMenu
      customerMenu()
    else: 
      tk.messagebox.showerror(" Error","Register Unsuccessful. Email already has an existing account")

  # Register Button
  tk.Button(frame, text = "Register", bg='#fbf2fa', command = registering).grid(row=13, column=1, sticky="E")

  frame.mainloop()

