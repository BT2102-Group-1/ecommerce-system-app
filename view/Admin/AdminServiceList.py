import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from view import GlobalVariables

from controller.controller import Connection

def adminServiceList():

  window = tk.Tk()
  window.title("Admin - Services")
  window.geometry("800x800")
  window.configure(bg="#f9f9f8")

  frame = tk.LabelFrame(window, bg="#F9FBF2", text="Admin Service List", padx=20, pady=20)
  frame.grid_rowconfigure(0, weight=1)
  frame.grid_columnconfigure(0, weight=1) 

  #---------------------CHECK BOXES-------------------#

  def approvedIsChecked():
    if approvedState.get() == 1:
        print("Filtering for Approved Request Service")
    elif approvedState.get() == 0:
        print("Removed Filtering for Approved Request Service")

  tk.Label(frame, text="Filter: ", bg="#F9FBF2").grid(row=0, column=0, sticky="E")

  approvedState = tk.IntVar()
  approvedState.set(0)
  tk.Checkbutton(frame, bg="#F9FBF2", text="Approved", variable=approvedState, onvalue=1, offvalue=0, command=approvedIsChecked).grid(row = 0, column = 1)

  def unapprovedIsChecked():
    if unapprovedState.get() == 1:
        print("Filtering for Unapproved Request Service")
    elif unapprovedState.get() == 0:
        print("Removed Filtering for Unapproved Request Service")

  unapprovedState = tk.IntVar()
  unapprovedState.set(0)
  tk.Checkbutton(frame, bg="#F9FBF2", text="Unapproved", variable=unapprovedState, onvalue=1, offvalue=0, command=unapprovedIsChecked).grid(row = 0, column = 2)

   #----------------END OF CHECK BOXES--------------#


  # ------------------ Table View -------------------- #
  tv = ttk.Treeview(frame)
  ttk.Style().configure("Treeview", background="#d9f1ff", foreground="black", fieldbackground="d9f1ff")
  ttk.Style().configure('Treeview.Heading', background='#84a5ce',   foreground='black')
  ttk.Style().configure('Treeview', rowheight=30)

  ##Code for Scrollbar##
  verscrlbar = ttk.Scrollbar(frame, orient="vertical", command = tv.yview)
  verscrlbar.grid(row=2, column=6, sticky ='nes')
  tv.configure(yscrollcommand = verscrlbar.set)
  tv['columns']=('Service ID', 'Item ID', 'Customer ID', 'Service Status', 'Approved', 'Completed' )

  rowDictionary = {}

  def selectItem(a):
    curItem = tv.focus()
    # print(tv.item(curItem))
    rowDictionary.update(tv.item(curItem))
    # print(rowDictionary['values'][0])

  tv.column('#0', width=0, stretch=tk.NO)
  tv.column('Service ID', anchor=tk.CENTER, width=100)
  tv.column('Item ID', anchor=tk.CENTER, width=85)
  tv.column('Customer ID', anchor=tk.CENTER, width=120)
  tv.column('Service Status', anchor=tk.CENTER, width=200)
  tv.column('Approved', anchor=tk.CENTER, width=130)
  tv.column('Completed', anchor=tk.CENTER, width=140)

  tv.heading('#0', text='', anchor=tk.CENTER)
  tv.heading('Service ID', text='Service ID', anchor=tk.CENTER)
  tv.heading('Item ID', text='Item ID', anchor=tk.CENTER)
  tv.heading('Customer ID', text='Customer ID', anchor=tk.CENTER)
  tv.heading('Service Status', text='Service Status', anchor=tk.CENTER)
  tv.heading('Approved', text='Approved', anchor=tk.CENTER)
  tv.heading('Completed', text='Completed', anchor=tk.CENTER)
  tv.bind('<ButtonRelease-1>', selectItem)

  # dicts = [ #HARD CODED DATA, REMOVE DATA and SET IT = controller.requestServices()
  #   {"serviceId": 1, "itemId": 2, "customerId": 9, "serviceStatus": "Waiting for approval"},
  #   {"serviceId": 2, "itemId": 2, "customerId": 9, "serviceStatus": "In progress"},
  #   {"serviceId": 3, "itemId": 2, "customerId": 9, "serviceStatus": "Completed"},
  #   {"serviceId": 4, "itemId": 2, "customerId": 9, "serviceStatus": "Waiting for approval"},
  #   {"serviceId": 5, "itemId": 2, "customerId": 9, "serviceStatus": "Waiting for approval"},
  #   {"serviceId": 6, "itemId": 2, "customerId": 9, "serviceStatus": "Waiting for approval"},
  #   {"serviceId": 7, "itemId": 2, "customerId": 9, "serviceStatus": "Waiting for approval"},
  #   {"serviceId": 8, "itemId": 2, "customerId": 9, "serviceStatus": "Waiting for approval"},
  #   {"serviceId": 9, "itemId": 2, "customerId": 9, "serviceStatus": "Waiting for approval"},
  #   {"serviceId": 10, "itemId": 2, "customerId": 9, "serviceStatus": "Waiting for approval"},
  #   {"serviceId": 11, "itemId": 2, "customerId": 9, "serviceStatus": "Waiting for approval"},
  #   {"serviceId": 12, "itemId": 2, "customerId": 9, "serviceStatus": "Waiting for approval"},
  #   {"serviceId": 13, "itemId": 2, "customerId": 9, "serviceStatus": "Waiting for approval"},
  #   {"serviceId": 14, "itemId": 2, "customerId": 9, "serviceStatus": "Waiting for approval"},
  #   {"serviceId": 15, "itemId": 2, "customerId": 9, "serviceStatus": "Waiting for approval"}
  # ]

  ## CALL BACKEND --------------------------
  # remove hardcoded list of dictionaries above under variable "dicts"
  dicts = Connection().requestServices()
  ## ---------------------------------------

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

  tv.grid(row = 2, columnspan=6, pady=5)
  # ------------End of Table View -------------------- #

  def approveService():
    if (len(rowDictionary) == 0):
      tk.messagebox.showerror("Error", "No row selected!")
    else:
      serviceStatusofRowSelected = rowDictionary['values'][3]
      if (serviceStatusofRowSelected == "Waiting for approval"):
        response = tk.messagebox.askokcancel("Approve Service", "Are you sure you want to approve this service request?")
        if response == 1:
            
            ## CALL BACKEND --------------------------
            serviceId = rowDictionary['values'][0]
            Connection().approveServiceRequest(GlobalVariables.adminId, serviceId)
            window.destroy()
            adminServiceList()
            print("Approved service")
            ## ---------------------------------------
        else:
            print("Cancelled approve process")
      elif(serviceStatusofRowSelected == "In progress"):
        tk.messagebox.showerror("Error", "Service has already been approved!")
      elif(serviceStatusofRowSelected == "Completed"):
        tk.messagebox.showerror("Error", "Service has already been completed, there's nothing to approve for!")
  
  def completeService():
    if (len(rowDictionary) == 0):
      tk.messagebox.showerror("Error", "No row selected!")
    else:
      serviceStatusofRowSelected = rowDictionary['values'][3]
      if (serviceStatusofRowSelected == "In progress"):
        response = tk.messagebox.askokcancel("Complete Service", "Are you sure you want indicate that this service is completed?")
        if response == 1:
            print("Completed service")
            ## CALL BACKEND --------------------------
            serviceId = rowDictionary['values'][0]
            # Might need try catch for this if update fails
            Connection().completeServiceRequest(serviceId)
            window.destroy()
            adminServiceList()
            ## ---------------------------------------
        else:
            print("Cancelled process")
      elif(serviceStatusofRowSelected == "Waiting for approval"):
        tk.messagebox.showerror("Error", "Service needs to be approved first and 'In progress' in order to complete it!")
      elif(serviceStatusofRowSelected == "Completed"):
        tk.messagebox.showerror("Error", "Service has already been completed!")

  tk.Button(frame, height=1, bg='#fbf2fa', width=10, text="Approve", command=approveService).grid(row=4, column=0, sticky="W", pady= 10)

  tk.Button(frame, height=1, bg='#fbf2fa', width=10, text="Complete", command=completeService).grid(row=4, column=1, sticky="W", pady= 10)

  # Redirect to Menu
  def redirectToMenu():
    window.destroy()
    from view.Admin.AdminMenu import adminMenu
    adminMenu()

  tk.Button(frame, text="Return to Menu", bg='#fbf2fa', command = redirectToMenu).grid(row=4, column=5, sticky="E", pady= 10)

  frame.pack()

  window.mainloop()