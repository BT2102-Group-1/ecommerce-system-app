import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

def adminServiceList():

  window = tk.Tk()
  window.title("Admin - Services")
  window.geometry("800x800")

 # Add Frame
  frame = tk.LabelFrame(window, text="Requests with Unpaid Service Fee", padx=20, pady=20)
  frame.grid_rowconfigure(0, weight=1)
  frame.grid_columnconfigure(0, weight=1) 

  ###############       CHECK BOXES     ###################

  def approvedIsChecked():
    if approvedState.get() == 1:
        print("Filtering for Approved Request Service")
    elif approvedState.get() == 0:
        print("Removed Filtering for Approved Request Service")

  approvedState = tk.IntVar()
  approvedState.set(0)
  tk.Checkbutton(frame, text="Approved", variable=approvedState, onvalue=1, offvalue=0, command=approvedIsChecked).grid(row = 0, column = 0)

  def unapprovedIsChecked():
    if unapprovedState.get() == 1:
        print("Filtering for Unapproved Request Service")
    elif unapprovedState.get() == 0:
        print("Removed Filtering for Unapproved Request Service")

  unapprovedState = tk.IntVar()
  unapprovedState.set(0)
  tk.Checkbutton(frame, text="Unapproved", variable=unapprovedState, onvalue=1, offvalue=0, command=unapprovedIsChecked).grid(row = 1, column = 0)

   ###############    END OF CHECK BOXES     ###################

  ###############TABLE#################
  #window['bg']='#fb0'

  # def setTextInput(text):
  #   textExample.delete(0,"end")
  #   textExample.insert(0, text)


  tv = ttk.Treeview(frame)
  tv['columns']=('Service ID', 'Item ID', 'Customer ID', 'Service Status', 'Approved', 'Completed' )

  rowDictionary = {}

  def selectItem(a):
    curItem = tv.focus()
    # setTextInput(curItem)
    # print(tv.item(curItem)) 
    rowDictionary.update(tv.item(curItem)) 

  tv.column('#0', width=0, stretch=tk.NO)
  tv.column('Service ID', anchor=tk.CENTER, width=100)
  tv.column('Item ID', anchor=tk.CENTER, width=85)
  tv.column('Customer ID', anchor=tk.CENTER, width=120)
  tv.column('Service Status', anchor=tk.CENTER, width=160)
  tv.column('Approved', anchor=tk.CENTER, width=130)
  tv.column('Completed', anchor=tk.CENTER, width=130)

  tv.heading('#0', text='', anchor=tk.CENTER)
  tv.heading('Service ID', text='Service ID', anchor=tk.CENTER)
  tv.heading('Item ID', text='Item ID', anchor=tk.CENTER)
  tv.heading('Customer ID', text='Customer ID', anchor=tk.CENTER)
  tv.heading('Service Status', text='Service Status', anchor=tk.CENTER)
  tv.heading('Approved', text='Approved', anchor=tk.CENTER)
  tv.heading('Completed', text='Completed', anchor=tk.CENTER)
  tv.bind('<ButtonRelease-1>', selectItem)

  
#[]



  dicts = [
    {"serviceId": 1, "itemId": 2, "customerId": 9, "serviceStatus": "Waiting for approval"},
    {"serviceId": 2, "itemId": 2, "customerId": 9, "serviceStatus": "In progress"},
    {"serviceId": 3, "itemId": 2, "customerId": 9, "serviceStatus": "Completed"},
    {"serviceId": 4, "itemId": 2, "customerId": 9, "serviceStatus": "Waiting for approval"},
    {"serviceId": 5, "itemId": 2, "customerId": 9, "serviceStatus": "Waiting for approval"},
    {"serviceId": 6, "itemId": 2, "customerId": 9, "serviceStatus": "Waiting for approval"},
    {"serviceId": 7, "itemId": 2, "customerId": 9, "serviceStatus": "Waiting for approval"},
    {"serviceId": 8, "itemId": 2, "customerId": 9, "serviceStatus": "Waiting for approval"},
    {"serviceId": 9, "itemId": 2, "customerId": 9, "serviceStatus": "Waiting for approval"},
    {"serviceId": 10, "itemId": 2, "customerId": 9, "serviceStatus": "Waiting for approval"},
    {"serviceId": 11, "itemId": 2, "customerId": 9, "serviceStatus": "Waiting for approval"},
  ]

  for dict in dicts:
    serviceId = dict.get('serviceId')
    itemId = dict.get('itemId')
    customerId = dict.get('customerId')
    serviceStatus = dict.get('serviceStatus')
    if serviceStatus == "Waiting for approval":
      tv.insert(parent='', index=serviceId, iid=serviceId, text='', values=(serviceId, itemId, customerId, serviceStatus, "-", "-")) 
    elif (serviceStatus == "In progress"):
      tv.insert(parent='', index=serviceId, iid=serviceId, text='', values=(serviceId, itemId, customerId, serviceStatus, "Y", "-")) 
    elif (serviceStatus == "Completed"):
      tv.insert(parent='', index=serviceId, iid=serviceId, text='', values=(serviceId, itemId, customerId, serviceStatus, "Y", "Y")) 

  tv.grid(row = 2, column = 0)

  # tv.insert(parent='', index=0, iid=0, text='', values=('1','90','9'))
  # tv.insert(parent='', index=1, iid=1, text='', values=('2','136','163'))
  # tv.insert(parent='', index=2, iid=2, text='', values=('3','29','74'))
  # tv.insert(parent='', index=3, iid=3, text='', values=('4','31','54'))
  # tv.insert(parent='', index=4, iid=4, text='', values=('5','46','99'))
  # tv.insert(parent='', index=5, iid=5, text='', values=('5','46','99'))
  # tv.insert(parent='', index=6, iid=6, text='', values=('6','50','95'))
  # tv.insert(parent='', index=7, iid=7, text='', values=('7','43','82'))
  

###########################################


  # Redirect to Menu
  def redirectToMenu():
    window.destroy()
    from Admin.AdminMenu import adminMenu
    adminMenu()

  tk.Button(frame, text="Return to Menu", command = redirectToMenu).grid(sticky = "", row = 3, column = 0)

  # serviceList = [
  #   {},
  #   {}
  # ]
  
  #.pack(pady = 5)

  def approveService():
    print(rowDictionary.values)


  frame.pack()

  # textExample = tk.Entry(window)
  # textExample.pack()

  

  def completeService():
    print("Completed Service Number ")

  approveBtn = tk.Button(window, height=1, width=10, text="Approve", 
                    command=approveService)
  approveBtn.pack() 
  completeBtn = tk.Button(window, height=1, width=10, text="Complete", 
                    command=completeService)
  completeBtn.pack()
  
  # tk.Entry(window, text = "Email address", width=10, textvariable= "1").pack()

  window.mainloop()