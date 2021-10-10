import tkinter as tk
from tkinter import ttk

def adminUnpaidRequest():

  window = tk.Tk()
  window.title("Admin - Service List")
  window.geometry("800x800")

  # Create Frame for Table of Customers
  frame = tk.LabelFrame(window, text="Customers with Unpaid Request", padx=20, pady=20)
  frame.pack()
  
  # DUMMY DATA THAT"LL BE DELETED>.. -----
  dummydata = [
    {
      "requestId": "84930293",
      "requestDate": "10/10/2021",
      "customerId": "3",
      "itemId": "1001"
    },
    {
      "requestId": "43923231",
      "requestDate": "6/10/2021",
      "customerId": "2",
      "itemId": "1431"
    },
    {
      "requestId": "32939203",
      "requestDate": "1/10/2021",
      "customerId": "4",
      "itemId": "1342"
    }
  ]

  # Table View 
  table = ttk.Treeview(frame)
  table['columns'] = ("Request ID", "Request Date", "Customer ID", "Item ID")

  table.column('#0', width=0, stretch=tk.NO)
  table.column('Request ID', anchor=tk.CENTER, width=150)
  table.column('Request Date', anchor=tk.CENTER, width=190)
  table.column('Customer ID', anchor=tk.CENTER, width=190)
  table.column('Item ID', anchor=tk.CENTER, width=150)

  table.heading('#0', text='', anchor=tk.CENTER)
  table.heading('Request ID', text='Request ID', anchor=tk.CENTER)
  table.heading('Request Date', text='Request Date', anchor=tk.CENTER)
  table.heading('Customer ID', text='Customer ID', anchor=tk.CENTER)
  table.heading('Item ID', text='Item ID', anchor=tk.CENTER)

  for item in dummydata:
    requestId = item.get('requestId')
    requestDate = item.get('requestDate')
    customerId = item.get('customerId')
    itemId = item.get('itemId')
    table.insert(parent='', index=requestId, iid=requestId, text='', values=(requestId, requestDate, customerId, itemId))

  table.grid(row=1, column=0)

  # Redirect to Initialise Database
  def redirectToMenu():
    window.destroy()
    from Admin.AdminMenu import adminMenu
    adminMenu()

  tk.Button(frame, text="Return to Menu", command = redirectToMenu).grid(row=2, column=0)

  window.mainloop()