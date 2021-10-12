import tkinter as tk
from tkinter import ttk

from view import GlobalVariables 
from view.Customer.ListOfRequest import listOfRequest
from controller.controller import Connection

def requestService():
  window = tk.Tk()
  window.title("Request Service")
  window.geometry("800x800")
  window.configure(bg="#f9f9f8")
  
  # Create Frame for Request Service
  request_frame = tk.LabelFrame(window, text="Request Service ", padx=20, pady=20, bg="#F9FBF2")
  request_frame.grid(row=0)

  # CALL BACKEND -------------------------- 
  # unrequestedList = getUnrequestedItems(GlobalVariables.customerID)
  # format should be the same as the dummy data format

  # DUMMY DATA TO BE DELETED 
  unrequestedList = [
    {"itemId": "1001", "modelName": "Lights1", "modelCost": "$100", "modelWarranty": "12 Months", "purchaseDate": "10/10/2020"
    },
    {"itemId": "1002", "modelName": "Lights1", "modelCost": "$120", "modelWarranty": "12 Months", "purchaseDate": "10/10/2020"
    },
    {"itemId": "1284", "modelName": "Lights1", "modelCost": "$150", "modelWarranty": "12 Months", "purchaseDate": "10/10/2020"
    },
    {"itemId": "1001", "modelName": "Lights1", "modelCost": "$200", "modelWarranty": "12 Months", "purchaseDate": "10/10/2020"
    }
  ]
  
  # Drop Down Box Options
  options = []
  for item in unrequestedList:
    options.append(item.get('itemId'))
  print(options)

  # Redirect to List Of Request
  def redirectToListOfRequest():
    window.destroy()
    listOfRequest()

  # Submission 
  def onSubmit():
    response = tk.messagebox.askokcancel("Request Service", "Are you sure you want to request a service for Item #" + dropdown_box.get() + "?")

    if response == 1:
      # CALL BACKEND -------------------------- 
      successful = Connection().submitRequest(GlobalVariables.customerID, dropdown_box.get())
      if not successful:
        tk.messagebox.showerror("Error","Unable to Request Service. Item was not purchased or Item already has a existing request")
      else:
        # Not necessary, printing for our reference only
        print("Request Successful")
        redirectToListOfRequest()

    elif response == 0:
      # Not necessary, printing for our reference only
      print("Request Canceled")

  # Print more request details for selected item
  def showDetails():
    # Retrieve Data
    for item in unrequestedList:
      if item.get('itemId') == dropdown_box.get():
        details = "Selected Item: " + item.get('itemId') + "\n" + "Warranty: " + item.get('modelWarranty') + "\n" + "Amount Payable: " + item.get('modelCost')
        break
    
    # Print out Data
    tk.Label(request_frame, text=details, bg="#F9FBF2").grid(row=5, column=0, sticky="W")
    
    # Submit request button
    tk.Button(request_frame, text="Submit Request", command=onSubmit, bg='#fbf2fa').grid(row=7, column=1, sticky="E")

  def onClick(event):
    showDetails()

  # Dropdown Menu of Purchased Item
  dropdown_box = ttk.Combobox(request_frame, state="readonly",value=options)
  dropdown_box.current(0)
  dropdown_box.bind("<<ComboboxSelected>>", onClick)
  dropdown_box.grid(row=3, column=0, sticky="W")
  
  tk.Label(request_frame, text="Choose Item to Request for Service", bg="#F9FBF2").grid(row=1, column=0, sticky="W")

  # Styling Spaces
  tk.Label(request_frame, text=" ", bg="#F9FBF2").grid(row=2, column=0)
  tk.Label(request_frame, text=" ", bg="#F9FBF2").grid(row=4, column=0)
  tk.Label(request_frame, text=" ", bg="#F9FBF2").grid(row=6, column=0)
  tk.Label(request_frame, text=" ", bg="#F9FBF2").grid(row=8, column=0)

  def redirectToMenu():
    window.destroy()
    from view.Customer.CustomerMenu import customerMenu
    customerMenu()

  tk.Button(request_frame, text="Return to Menu", bg='#fbf2fa', command = redirectToMenu).grid(row=9, column=1, sticky="E")


  window.mainloop()



        