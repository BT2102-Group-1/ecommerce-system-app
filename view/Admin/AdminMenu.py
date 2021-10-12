import tkinter as tk
from tkinter import messagebox

from view.Admin.AdminViewInventory import adminViewInventory
from view.Admin.AdminProductCatalogue import adminProductCatalogue
from view.Admin.AdminServiceList import adminServiceList
from view.Admin.AdminUnpaidRequest import adminUnpaidRequest

from controller.controller import Connection

def adminMenu():
  window = tk.Tk()
  window.title("Admin Menu")
  window.geometry("800x800")
  window.configure(bg="#f9f9f8")

  # Add Frame
  frame = tk.LabelFrame(window, text="Admin Menu ", bg="#F9FBF2", padx=20, pady=20)
  frame.pack()

  def redirectToInitialiseDatabase():
    ## CALL BACKEND -------------------------- 
    outcome = Connection().initialiseDatabase()
    
    if (outcome == True): 
      messagebox.showinfo("Success", "Successfully initialised database. Please click 'View Inventory' to see newly added items.")
    else:
      messagebox.showerror("Error", "Failed to initialise database.")

  # Redirect to View Inventory Page
  def redirectToViewInventory():
    window.destroy()
    adminViewInventory()

  # Redirect to Product Catalogue Page
  def redirectToProductCatalogue():
    window.destroy()
    adminProductCatalogue()

  # Redirect to View Service List Page
  def redirectToViewServiceList():
    window.destroy()
    adminServiceList()

  # Redirect to View Requests with Unpaid Service Fee Page
  def redirectToViewRequests():
    window.destroy()
    adminUnpaidRequest()

  # Redirect to Main.py
  def redirectToMain():
    window.destroy()
    from view.main import main
    main()

  tk.Button(frame, text="Initialise Database", bg='#fbf2fa', command = redirectToInitialiseDatabase, width = 30).pack(pady = 5)

  tk.Button(frame, text="View Inventory", bg='#fbf2fa', command = redirectToViewInventory, width = 30).pack(pady = 5)

  tk.Button(frame, text="Product Catalogue", bg='#fbf2fa', command = redirectToProductCatalogue, width = 30).pack(pady = 5)

  tk.Button(frame, text="View Service List", bg='#fbf2fa', command = redirectToViewServiceList, width = 30).pack(pady = 5)

  tk.Button(frame, text="View Requests (Unpaid Service Fee)", bg='#fbf2fa', command = redirectToViewRequests, width = 30).pack(pady = 5)

  tk.Button(frame, text="Logout", bg='#fbf2fa', command = redirectToMain, width = 20).pack(pady = 5)

  window.mainloop()