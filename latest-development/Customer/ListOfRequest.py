import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import GlobalVariables 

def listOfRequest():
  window = tk.Tk()
  window.title("List Of Request")
  window.geometry("800x800")
  window.configure(bg="#f9f9f8")

  # Add Frame
  frame = tk.LabelFrame(window, text="List Of Service Request ", padx=20, pady=20, bg="#F9FBF2")
  frame.pack()

  # Add Table
  tv = ttk.Treeview(frame)
  tv['columns']=('Request ID', 'Item ID', 'Request Date', 'Service Fee','Request Status', 'Paid', 'Cancelled' )
  ttk.Style().configure("Treeview", background="#d9e9f9", 
  foreground="black", fieldbackground="d9e9f9")
  ttk.Style().configure('Treeview.Heading', background='#84a5ce',   foreground='black')

  # Scroll Bar
  verscrlbar = ttk.Scrollbar(frame, orient="vertical", command = tv.yview)
  verscrlbar.grid(row=0, column=5, sticky ='nes')
  tv.configure(yscrollcommand = verscrlbar.set)


  selectedRowDictionary = {}

  # Binding Selected Item
  def selectItem(a):
    curItem = tv.focus()
    selectedRowDictionary.update(tv.item(curItem))
    print(selectedRowDictionary)
  
  # Construct Table
  tv.column('#0', width=0, stretch=tk.NO)
  tv.column('Request ID', anchor=tk.CENTER, width=140)
  tv.column('Item ID', anchor=tk.CENTER, width=100)
  tv.column('Request Date', anchor=tk.CENTER, width=180)
  tv.column('Service Fee', anchor=tk.CENTER, width=150)
  tv.column('Request Status', anchor=tk.CENTER, width=380)
  tv.column('Paid', anchor=tk.CENTER, width=60)
  tv.column('Cancelled', anchor=tk.CENTER, width=120)

  tv.heading('#0', text='', anchor=tk.CENTER)
  tv.heading('Request ID', text='Request ID', anchor=tk.CENTER)
  tv.heading('Item ID', text='Item ID', anchor=tk.CENTER)
  tv.heading('Request Date', text='Request Date', anchor=tk.CENTER)
  tv.heading('Service Fee', text='Service Fee', anchor=tk.CENTER)
  tv.heading('Request Status', text='Request Status', anchor=tk.CENTER)
  tv.heading('Paid', text='Paid', anchor=tk.CENTER)
  tv.heading('Cancelled', text='Cancelled', anchor=tk.CENTER)
  tv.bind('<ButtonRelease-1>', selectItem)

  # CALL BACKEND --------------------------
  # requestList = retrieveRequest(GlobalVariables.customerID)

  # DUMMY DATA -------
  requestList = [
    {"requestId": "93821", "itemId": 1, "requestDate": "12/06/21", "serviceFee": 9, "requestStatus": "Submitted"},
    {"requestId": "54345", "itemId": 2, "requestDate": "27/06/21", "serviceFee": 400, "requestStatus": "Submitted and Waiting for payment"},
    {"requestId": "23654","itemId": 3, "requestDate": "29/05/21", "serviceFee": 50, "requestStatus": "Completed"},
    {"requestId": "56546", "itemId": 4, "requestDate": "10/10/21", "serviceFee": 250, "requestStatus": "Cancelled"},
    {"requestId": "54287", "itemId": 5, "requestDate": "12/02/21", "serviceFee": 20, "requestStatus": "In Progress"},
    {"requestId": "35624", "itemId": 6, "requestDate": "03/05/21", "serviceFee": 0, "requestStatus": "Approved"}
  ]

  # Populating Table
  for dict in requestList:
    requestId = dict.get('requestId')
    itemId = dict.get('itemId')
    requestDate = dict.get('requestDate')
    serviceFee = dict.get('serviceFee')
    requestStatus = dict.get('requestStatus')

    if requestStatus == "Submitted and Waiting for payment":
      tv.insert(parent='', index=itemId, iid=itemId, text='', values=(requestId, itemId, requestDate, serviceFee, requestStatus, "-", "-")) 

    elif (requestStatus == "Canceled"):
      tv.insert(parent='', index=itemId, iid=itemId, text='', values=(requestId,itemId, requestDate, serviceFee, requestStatus, "-", "Y"))

    else:
      tv.insert(parent='', index=itemId, iid=itemId, text='', values=(requestId,itemId, requestDate, serviceFee, requestStatus, "Y", "-")) 

  tv.grid(row=0, column=0, columnspan=4)

  # Settling Payment
  def payment():
    response = tk.messagebox.askokcancel("Payment", "Are you sure you want to pay $" + str(selectedRowDictionary['values'][3]) + " for Item #" + str(selectedRowDictionary['values'][1]) + " ?")

    if response == 1:
      # CALL BACKEND --------------------------
      # onPay(selectedRowDictionary['values'][0])

      # Not necessary, printing for our reference only
      print("Paid!")

    elif response == 0:
      # Not necessary, printing for our reference only
      print("Canceled")
  
  # Settling Cancellation
  def cancel():
    response = tk.messagebox.askokcancel("Cancel", "Are you sure you want to cancel service request?")

    if response == 1:
      # CALL BACKEND --------------------------
      #onCancelRequest(selectedRowDictionary['values'][0])
      
      # Not necessary, printing for our reference only
      print("Request Cancelled")

    elif response == 0:
      # Not necessary, printing for our reference only
      print("Request Not Cancelled")

  # Check if Request is eligible for Payment
  def canPay():
    if (len(selectedRowDictionary) == 0):
      tk.messagebox.showwarning("Warning", "No Items Selected")
    else:
      if (selectedRowDictionary['values'][5] != 'Y' and selectedRowDictionary['values'][4] != "Cancelled" ):
        payment()
      else:
        tk.messagebox.showerror("Error", "Payment has been made!")

  # Check if Request is eligible for Cancellation
  def canCancel():
    if (len(selectedRowDictionary) == 0):
      tk.messagebox.showwarning("Warning", "No Items Selected")
    else:
      if (selectedRowDictionary['values'][4] == ("Submitted" and "Submitted and Waiting for payment")):
        cancel()
      elif selectedRowDictionary['values'][4] == "Cancelled":
        tk.messagebox.showerror("Error", "Service Request has already been cancelled!")
      else:
        tk.messagebox.showerror("Error", "Service Request cannot be cancelled!")
  
  # Payment Button
  tk.Button(frame, height=1, width=10, text="Pay for Service",command=canPay, bg='#fbf2fa').grid(row=2, column=0, sticky="W")

  # Cancellation Button
  tk.Button(frame, height=1, width=10, bg='#fbf2fa', text="Cancel Request",command=canCancel).grid(row=2, column=1, sticky="W")
  
  # Redirect to Customer Menu
  def redirectToMenu():
    window.destroy()
    from Customer.CustomerMenu import customerMenu
    customerMenu()

  # Redirect to Customer Menu Button
  tk.Button(frame, text="Return to Menu", bg='#fbf2fa', command = redirectToMenu).grid(row=2, column=3, sticky="E")

  # Styling Space 
  tk.Label(frame, text=" ", bg="#F9FBF2").grid(row=1, column=0)

  window.mainloop()