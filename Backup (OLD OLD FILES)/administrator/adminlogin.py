import tkinter as tk
from tkinter import ttk

root = tk.Tk()
frame = tk.LabelFrame(root, text="Administrator Log in ", padx=20, pady=20)
frame.pack()

frame.heading = ('Administrator Log in page')


username_label = tk.Label(frame, text = "Email address").pack()
username = tk.Entry(frame, text = "Email address", width=7).pack()
password_label = tk.Label(frame, text = "Password").pack()
password = tk.Entry(frame, text = "Password", width=7).pack()

def loggedin():
  root.destroy()
  import administrator.adminmenu

loginButton = tk.Button(frame, text = "Log In", command = loggedin).pack(pady = 10)

frame.mainloop()