import tkinter as tk
from tkinter import ttk
from main import *

def requestService():
  window = tk.Tk()
  window.title("Request Service")
  window.geometry("500x500")
  request_frame = tk.LabelFrame(window, text="Register Service ", padx=20, pady=20)
  request_frame.pack()

  # itemId, modelName, modelCost, modelWarranty, purchaseDate, DATE_ADD(purchaseDate, INTERVAL modelWarranty MONTH) warrantyDate 

  dummydata = [
    {"itemId": "1001", "modelName": "Lights1", "modelCost": "$100", "modelWarranty": "12 Months", "purchaseDate": "10/10/2020"
    },
    {"itemId": "1002", "modelName": "Lights1", "modelCost": "$120", "modelWarranty": "12 Months", "purchaseDate": "10/10/2020"
    },
    {"itemId": "1284", "modelName": "Lights1", "modelCost": "$150", "modelWarranty": "12 Months", "purchaseDate": "10/10/2020"
    },
    {"itemId": "1001", "modelName": "Lights1", "modelCost": "$200", "modelWarranty": "12 Months", "purchaseDate": "10/10/2020"
    }
  ]
  
  options = [item.get("itemId") for items in dummydata]
  print(options)

  #def nextPage():
    #request_frame.destroy()
    #from listofrequests import ListofRequests

  # Submission 
  def onSubmit():
    response = tk.messagebox.askokcancel("Request Service", "Are you sure you want to request a service for Item #" + dropdown_box.get() + "?")
    #backend method of changing requeststatus -- pass in dropdown_box.get()

    tk.Label(request_frame, text=response)

    if response == 1:
      # update database
      # redirect to list of requests page
      tk.Label(request_frame, text="Request Successful!").pack()
          
      # Button(self.request_frame, text="Proceed to List of Requests Page", command=self.requestlist.show).pack(side="right")

      #nextPage()

    elif response == 0:
      tk.Label(request_frame, text="Request Cancelled").pack()

  # Print more request details for selected item
  def showDetails():
    details = "Selected Item: " + dropdown_box.get() + "\n" + "Warranty: 6 months, Amount Payable: $200"
    #tbh idk which backend method.... (backend)getUnrequestedRequest
    
    selected = tk.Label(request_frame, text=details).pack()
    
    # submit request button
    submit_button = tk.Button(request_frame, text="Submit Request", command=onSubmit).pack()

  def onClick(event):
    showDetails()

  # dropdown menu of purchased item
  dropdown_box = ttk.Combobox(request_frame, state="readonly",value=options)
  dropdown_box.current(0)
  dropdown_box.bind("<<ComboboxSelected>>", onClick)
  dropdown_box.pack()

  def redirectToMenu():
    window.destroy()
    from CustomerMenu import customerMenu
    customerMenu()

  tk.Button(window, text="Return to Menu", command = redirectToMenu).pack()

  window.mainloop()



        