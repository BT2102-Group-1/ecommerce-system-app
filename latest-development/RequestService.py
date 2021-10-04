import tkinter as tk
from tkinter import ttk
from main import *

def requestService():
  window = tk.Tk()
  window.title("Request Service")
  window.geometry("500x500")
  request_frame = tk.LabelFrame(window, text="Register Service ", padx=20, pady=20)
  request_frame.pack()

  #(backend)getUnrequestedRequest(customerID) -> returned frame 
  # list of purchased items -- backend method to find 
  #iterate through column with requestID, put in array and equate options
  options = [
    "1001", "1002", "1284", "1529"
    ]
  
  #redirect to listofrequest page -- need 
  #requestlist = ListofRequests(self.master)

  #def nextPage():
    #request_frame.destroy()
    #from listofrequests import ListofRequests

  # submission 
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

  # print more request details for selected item
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

  window.mainloop()



        