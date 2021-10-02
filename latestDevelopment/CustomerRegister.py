import tkinter as tk
from RequestService import *

def customerRegister():
  root = tk.Tk()
  root.geometry("500x500")
  frame = tk.LabelFrame(root, text="Customer Register ", padx=20, pady=20)
  frame.grid(row=0, column=0)

  email_input, pw_input, name_input, address_input, phoneno_input = (tk.StringVar() for i in range(5))

  #input email
  email = tk.Label(frame, text="Email").grid(row=1, column=0)
  email1 = tk.Entry(frame, textvariable = email_input).grid(row=1, column=1)

  #input password
  password = tk.Label(frame, text="Password").grid(row=2, column=0)
  password1 = tk.Entry(frame, textvariable = pw_input).grid(row=2, column=1)

  #input name
  name = tk.Label(frame, text="Name").grid(row=3, column=0)
  name1 = tk.Entry(frame, textvariable = name_input).grid(row=3, column=1)

  #input address
  address = tk.Label(frame, text="Address").grid(row=4, column=0)
  address1 = tk.Entry(frame, textvariable = address_input).grid(row=4, column=1)

  #input phone no
  phoneno = tk.Label(frame, text="Phone Number").grid(row=5, column=0)
  phoneno1 = tk.Entry(frame, textvariable = phoneno_input).grid(row=5, column=1)

  #drop down gender
  gender = tk.Label(frame, text="Gender").grid(row=6, column=0)
  # dropdown menu for gender items
  options = [
    "M", "F"
  ]
  clicked = tk.StringVar()
  clicked.set(options[0])
  dropdown = tk.OptionMenu(frame, clicked, *options)
  dropdown.grid(row=6, column=1)

  #check if all fields are field  
  def registering():
    if not email_input.get() or pw_input.get() or name_input.get() or address_input.get() or phoneno_input.get():
      messagebox.showerror(" Unsuccessful","Error. Please make sure all fields are filled.")
    else: 
      verifythis()

  
  #def onSuccess():
    #successful = tk.Label(frame, text="Registered!")
    #successful.grid(row=8, column=1)
  def registernow():
    frame.destroy()
    RequestService()

  registerButton = tk.Button(frame, text = "Register", command = registernow)
  registerButton.grid(row=7, column=2)

  frame.mainloop()

