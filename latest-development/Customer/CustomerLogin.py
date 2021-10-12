import tkinter as tk
# from Customer.CustomerMenu import customerMenu
from tkinter import messagebox
import GlobalVariables 
# import main as mainpage

def customerLogin():
  window = tk.Tk()
  window.title("Customer Login")
  window.geometry("800x800")
  window.configure(bg="#f9f9f8")

  #print(GlobalVariables.customerID)

  # Add Frame
  frame = tk.LabelFrame(window, text="Customer Login ", bg="#F9FBF2", padx=20, pady=20)
  frame.pack()

  # Text variable
  username_verification = tk.StringVar() 
  password_verification = tk.StringVar()

  # Email Address Label
  tk.Label(frame, text = "Email address", bg="#F9FBF2").pack()

  # Input box for email
  tk.Entry(frame, text = "Email address", width=10, textvariable= username_verification).pack()

  # Password Label
  tk.Label(frame, text = "Password", bg="#F9FBF2").pack()

  # Input box for password
  tk.Entry(frame, text = "Password", width=10, textvariable = password_verification).pack()

  # Verification - need change this 
  def verifyLogin():

    if (not username_verification.get() or not password_verification.get()):
      tk.messagebox.showerror("Error","Login Unsuccessful. Please ensure all fields are filled.")

    
    # Method below
    else:
      GlobalVariables.customerID = 5; #HARDCODED
      # CALL BACKEND --------------------------
      # remove hardcoded
      # GlobalVariables.customerID = customerLogin(username_verification.get(), password_verification.get())
      

    if (GlobalVariables.customerID >= 0): 
      redirectToCustomerHome()
    elif (not username_verification.get() or not password_verification.get()):
      tk.messagebox.showerror("Error","Login Unsuccessful. Please check your email address or password again.")


  # Redirect to Menu Page 
  def redirectToCustomerHome():
    window.destroy()
    from Customer.CustomerMenu import customerMenu
    customerMenu()    
  # Login button
  loginButton = tk.Button(frame, text = "Log In", bg='#fbf2fa', command = verifyLogin)
  loginButton.pack(pady=10)

  tk.Label(frame,text = " ", bg="#F9FBF2").pack()

  # Register button
  register = tk.Label(frame,text = "No Account? Register now!", bg="#F9FBF2")
  register.pack()

  # Redirect to Register Page 
  def registernow():
    window.destroy()
    from Customer.CustomerRegister import customerRegister
    customerRegister()

  registerButton = tk.Button(frame, text = "Register Here", bg='#fbf2fa', command = registernow)
  registerButton.pack()

  # Redirect to Main
  def redirectToMain():
    window.destroy()
    from main import main
    main()

  # Redirect to Main Button
  tk.Button(frame, text="Return to main", bg='#fbf2fa', command = redirectToMain).pack(pady = 20)
  
  window.mainloop()

