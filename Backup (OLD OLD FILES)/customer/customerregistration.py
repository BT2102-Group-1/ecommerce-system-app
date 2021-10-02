import tkinter as tk
from tkinter import ttk

root = tk.Tk()
frame = tk.LabelFrame(root, text="Customer Log in ", padx=20, pady=20)
frame.grid(row=0, column=0)

frame.heading = ('Customer Registeration page')
title = tk.Label(frame,text = "Register now!")
title.grid(row=0, column=0)

email = tk.Label(frame, text="Email").grid(row=1, column=0)
email1 = tk.Entry(frame).grid(row=1, column=1)

password = tk.Label(frame, text="Password").grid(row=2, column=0)
password1 = tk.Entry(frame).grid(row=2, column=1)

name = tk.Label(frame, text="Name").grid(row=3, column=0)
name1 = tk.Entry(frame).grid(row=3, column=1)

address = tk.Label(frame, text="Address").grid(row=4, column=0)
address1 = tk.Entry(frame).grid(row=4, column=1)

phoneno = tk.Label(frame, text="Phone Number").grid(row=5, column=0)
phoneno1 = tk.Entry(frame).grid(row=5, column=1)

gender = tk.Label(frame, text="Gender").grid(row=6, column=0)
# dropdown menu for gender items
options = [
  " ", "M", "F"
]
clicked = tk.StringVar()
clicked.set(options[0])
dropdown = tk.OptionMenu(frame, clicked, *options)
dropdown.grid(row=6, column=1)

def registered():
  successful = tk.Label(frame, text="Registered!")
  successful.grid(row=8, column=1)

registerButton = tk.Button(frame, text = "Register", command = registered)
registerButton.grid(row=7, column=2)

frame.mainloop()