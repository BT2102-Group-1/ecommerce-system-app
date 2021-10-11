import tkinter as tk
from Admin.AdminMenu import *
from tkinter import messagebox
import GlobalVariables

def adminLogin():

  window = tk.Tk()
  window.title("Admin Login")
  window.geometry("800x800")
  window.configure(bg="#f9f9f8")

  frame = tk.LabelFrame(window, text="Admin Login ", padx=20, pady=20, bg="#F9FBF2")
  frame.pack()

  #for text variable
  username_verification = tk.StringVar() 
  password_verification = tk.StringVar()

  tk.Label(frame, text = "Admin ID", bg="#F9FBF2").pack()
  tk.Entry(frame, text = "Admin ID", width=10, textvariable= username_verification, bg="#F9FBF2").pack()

  tk.Label(frame, bg="#F9FBF2", text = "Password").pack()
  tk.Entry(frame, bg="#F9FBF2", text = "Password", width=10, textvariable = password_verification).pack()

  def redirectToMain():
    window.destroy()
    from main import main
    main()

  def redirectToAdminHome():
    window.destroy()
    adminMenu()
    
  def verifyLogin():
    if (not username_verification.get() or not password_verification.get()):
      tk.messagebox.showerror("Error","Login Unsuccessful. Please ensure all fields are filled.")
    #else:
    ## CALL BACKEND --------------------------
    # remove hardcoded "adminIdVerify = 1"
    # add "GlobalVariables.adminId = controller.adminLogin(username_verification.get(), password_verification.get())""
    ## ---------------------------------------
      
    GlobalVariables.adminId = 1 #HARDCODED DATA [REMOVE when linking to backend!!]
    if (GlobalVariables.adminId >= 0):
      redirectToAdminHome()
    else:
      messagebox.showerror("Login Unsuccessful","Error. Please check Admin ID or password again.")

  tk.Button(frame, text = "Log In", bg='#fbf2fa', command = verifyLogin).pack(pady = 15)

  tk.Button(frame, bg='#fbf2fa', text="Return to main", command = redirectToMain).pack(pady = 5)
  
  window.mainloop()

