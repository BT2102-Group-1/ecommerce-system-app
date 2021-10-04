import tkinter as tk
from tkinter import ttk
from RequestService import *
from main import *

def customerRegister():
  root = tk.Tk()
  root.geometry("500x500")
  frame = tk.LabelFrame(root, text="Customer Register ", padx=20, pady=20)
  frame.grid(row=0, column=0)

  email_input, pw_input, name_input, address_input, phoneno_input = (tk.StringVar() for i in range(5))

  #input email
  tk.Label(frame, text="Email").grid(row=1, column=0)
  tk.Entry(frame, textvariable = email_input).grid(row=1, column=1)

  #input password
  tk.Label(frame, text="Password").grid(row=2, column=0)
  tk.Entry(frame, textvariable = pw_input).grid(row=2, column=1)

  #input name
  tk.Label(frame, text="Name").grid(row=3, column=0)
  tk.Entry(frame, textvariable = name_input).grid(row=3, column=1)

  #input address
  address = tk.Label(frame, text="Address").grid(row=4, column=0)
  address1 = tk.Entry(frame, textvariable = address_input).grid(row=4, column=1)

  #input phone no
  phoneno = tk.Label(frame, text="Phone Number").grid(row=5, column=0)
  phoneno1 = tk.Entry(frame, textvariable = phoneno_input).grid(row=5, column=1)

  #drop down gender
  tk.Label(frame, text="Gender").grid(row=6, column=0)
  # Gender Options
  options = [
    " ", "M", "F"
  ]

  # Dropdown menu of gender item
  gender_dropdown = ttk.Combobox(frame, state="readonly",value=options)
  gender_dropdown.current(0)
  gender_dropdown.bind("<<ComboboxSelected>>")
  gender_dropdown.grid(row=6, column=1)

  #check if all fields are field  
  def registering():
    if not email_input.get() or not pw_input.get() or not name_input.get() or not address_input.get() or not phoneno_input.get() or gender_dropdown.get() == " ":
      tk.messagebox.showerror(" Unsuccessful","Error. Please make sure all fields are filled.")
    else: 
      registernow()

  
  #def onSuccess():
    #successful = tk.Label(frame, text="Registered!")
    #successful.grid(row=8, column=1)
  def registernow():
    #customerID = backend(email_input.get(), pw_input.get(), name_input.get(), address_input.get(), phoneno_input.get(), gender_dropdown.get())
    if (customerID >=0):
      frame.destroy()
      requestService()
    else: 
      tk.messagebox.showerror(" Unsuccessful","Error. Email already has an existing account")

  registerButton = tk.Button(frame, text = "Register", command = registering)
  registerButton.grid(row=7, column=2)

  frame.mainloop()

