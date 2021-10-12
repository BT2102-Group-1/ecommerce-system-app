import tkinter as tk
# from Customer.ListOfRequest import *
# from Customer.ProductSearch import *
# from Customer.PurchaseHistory import *
# from Customer.RequestService import *
# from main import *

def customerMenu():
  window = tk.Tk()
  window.title("Customer Menu")
  window.geometry("800x800")
  window.configure(bg="#f9f9f8")

  # Add Frame
  frame = tk.LabelFrame(window, text="Customer Menu ", bg="#F9FBF2", padx=20, pady=20)
  frame.pack()

  # Redirect to Product Search Page
  def redirectToProductSearch():
    window.destroy()
    from Customer.ProductSearch import productSearch
    productSearch()

  # Redirect to PurchaseHistory Page
  def redirectToPurchaseHistory():
    window.destroy()
    from Customer.PurchaseHistory import purchaseHistory
    purchaseHistory()

  # Redirect to List Of Request
  def redirectToListOfRequest():
    window.destroy()
    from Customer.ListOfRequest import listOfRequest
    listOfRequest()

  # Redirect to Request History Page
  def redirectToRequestService():
    window.destroy()
    from Customer.RequestService import requestService
    requestService()

  # Redirect to Main.py
  def redirectToMain():
    window.destroy()
    from main import main
    main()

  tk.Button(frame, text="Product Search", bg='#fbf2fa', command = redirectToProductSearch, width = 30).pack(pady = 5)

  tk.Button(frame, text="Purchase History", bg='#fbf2fa', command = redirectToPurchaseHistory, width = 30).pack(pady = 5)

  tk.Button(frame, text="Request Service", bg='#fbf2fa', command = redirectToRequestService, width = 30).pack(pady = 5)

  tk.Button(frame, text="List of Request", bg='#fbf2fa', command = redirectToListOfRequest, width = 30).pack(pady = 5)

  tk.Button(frame, text="Logout", bg='#fbf2fa', command = redirectToMain, width = 20).pack(pady = 5)

  window.mainloop()