import tkinter as tk
from tkinter import ttk
from tkinter import messagebox




def listOfRequest():
  window = tk.Tk()
  window.title("Request Service")
  window.geometry("500x500")
  frame = tk.LabelFrame(window, text="List Of Service ", padx=20, pady=20)
  frame.pack()
  tv = ttk.Treeview(frame)
  tv['columns']=('Item ID', 'Request Date', 'Service Fee', 'Request Status', 'Paid', 'Cancelled' )

  def selectItem(a):
    global curItem 
    curItem = tv.focus()
    print(tv.item(curItem))
    

  tv.column('#0', width=0, stretch=tk.NO)
  tv.column('Item ID', anchor=tk.CENTER, width=100)
  tv.column('Request Date', anchor=tk.CENTER, width=85)
  tv.column('Service Fee', anchor=tk.CENTER, width=160)
  tv.column('Request Status', anchor=tk.CENTER, width=120)
  tv.column('Paid', anchor=tk.CENTER, width=130)
  tv.column('Cancelled', anchor=tk.CENTER, width=130)

  tv.heading('#0', text='', anchor=tk.CENTER)
  tv.heading('Item ID', text='Item ID', anchor=tk.CENTER)
  tv.heading('Request Date', text='Request Date', anchor=tk.CENTER)
  tv.heading('Service Fee', text='Service Fee', anchor=tk.CENTER)
  tv.heading('Request Status', text='Request Status', anchor=tk.CENTER)
  tv.heading('Paid', text='Paid', anchor=tk.CENTER)
  tv.heading('Cancelled', text='Cancelled', anchor=tk.CENTER)
  tv.bind('<ButtonRelease-1>', selectItem)

  # DUMMY DATA -------
  dummydata = [
    {"itemId": 1, "requestDate": "12/06/21", "serviceFee": 9, "requestStatus": "Submitted"},
    {"itemId": 2, "requestDate": "27/06/21", "serviceFee": 400, "requestStatus": "Submitted and Waiting for payment"}, {"itemId": 3, "requestDate": "29/05/21", "serviceFee": 50, "requestStatus": "Completed"}, {"itemId": 4, "requestDate": "10/10/21", "serviceFee": 250, "requestStatus": "Canceled"},
    {"itemId": 5, "requestDate": "12/02/21", "serviceFee": 20, "requestStatus": "In Progress"}, {"itemId": 6, "requestDate": "03/05/21", "serviceFee": 0, "requestStatus": "Approved"}
  ]

  for dict in dummydata:
    itemId = dict.get('itemId')
    requestDate = dict.get('requestDate')
    serviceFee = dict.get('serviceFee')
    requestStatus = dict.get('requestStatus')
    if requestStatus == "Submitted and Waiting for payment":
      tv.insert(parent='', index=itemId, iid=itemId, text='', values=(itemId, requestDate, serviceFee, requestStatus, "-", "-")) 
    elif (requestStatus == "Canceled"):
      tv.insert(parent='', index=itemId, iid=itemId, text='', values=(itemId, requestDate, serviceFee, requestStatus, "-", "Y"))
    else:
      tv.insert(parent='', index=itemId, iid=itemId, text='', values=(itemId, requestDate, serviceFee, requestStatus, "Y", "-")) 

  tv.pack()

  def payment():
    response = tk.messagebox.askokcancel("Payment", "Are you sure you want to pay $" + str(tv.item(curItem).get('values')[2]) + " for Item #" + str(tv.item(curItem).get('values')[0]) + " ?")
    tk.Label(frame, text=response)

    if response == 1:
      #update database
      tk.Label(frame, text="Paid!").pack()

    elif response == 0:
      tk.Label(frame, text="Payment Cancelled").pack()
  
  def cancel():
    response = tk.messagebox.askokcancel("Cancel", "Are you sure you want to cancel service request?")

    tk.Label(frame, text=response)

    if response == 1:
      # update database
      tk.Label(frame, text="Service Request Canceled").pack()

    elif response == 0:
      tk.Label(frame, text="Service Request Not Canceled").pack()

  def canPay():
    if (tv.item(curItem).get('values')[4] != 'Y' and tv.item(curItem).get('values')[3] != "Canceled" ):
      payment()
    else:
      tk.messagebox.showerror("Payment", "Payment has been made!")

  def canCancel():
    if (tv.item(curItem).get('values')[3] != "Canceled"):
      cancel()
    else:
      tk.messagebox.showerror("Cancel", "Service Request has already been cancelled!")
  
  tk.Button(frame, height=1, width=10, text="Payment",command=canPay).pack()

  tk.Button(frame, height=1, width=10, text="Cancel Request",command=canCancel).pack
  
  def redirectToMenu():
    window.destroy()
    from CustomerMenu import customerMenu
    customerMenu()

  tk.Button(window, text="Return to Menu", command = redirectToMenu).pack()()


  window.mainloop()