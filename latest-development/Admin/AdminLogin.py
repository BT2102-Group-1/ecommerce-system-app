import tkinter as tk
from Admin.AdminMenu import *

def adminLogin():

  window = tk.Tk()
  window.title("Admin Login")
  window.geometry("500x500")

  #add frame
  frame = tk.LabelFrame(window, text="Admin Login ", padx=20, pady=20)
  frame.pack()

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

  #need change to verification check 
  def redirectToAdminHome():
    window.destroy()
    adminMenu()
    
  # verification
  def verifyLogin():
    #backend(username_verification.get(), password_verification.get())
    # input backend verification, if true 
    verify = True
    if (verify):
      redirectToAdminHome()
    else:
      messagebox.showerror("Login Unsuccessful","Error. Please check your email address or password again.")

  #login button
  loginButton = tk.Button(frame, text = "Log In", command = verifyLogin)
  loginButton.pack()
  
  window.mainloop()