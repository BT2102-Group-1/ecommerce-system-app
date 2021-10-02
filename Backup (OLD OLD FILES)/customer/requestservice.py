from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from customer.listofrequests import ListofRequests

class RequestService:
    # list of purchased items
    options = [
      "1001", "1002", "1284", "1529"
    ]
    
    def __init__(self, master):
        self.master = master
        master.title("Request Service")
        self.requestlist = ListofRequests(self.master)

        self.request_frame = LabelFrame(master, text="Request A Service Here", padx=20, pady=20)
        self.request_frame.pack()

        # dropdown menu of purchased item
        self.dropdown_box = ttk.Combobox(self.request_frame, value=self.options)
        self.dropdown_box.current(0)
        self.dropdown_box.bind("<<ComboboxSelected>>", self.onClick)
        self.dropdown_box.pack()

    # print more request details for selected item
    def onClick(self, event):
        self.showDetails()

    def showDetails(self):
        details = "Selected Item: " + self.dropdown_box.get() + "\n" + "Warranty: 6 months, Amount Payable: $200"

        selected = Label(self.request_frame, text=details).pack()

        # submit request button
        submit_button = Button(self.request_frame, text="Submit Request", command=self.onSubmit).pack()

    # submission 
    def onSubmit(self):
      response = messagebox.askokcancel("Request Service", "Are you sure you want to request a service for Item #" + self.dropdown_box.get() + "?")

      Label(self.request_frame, text=response)

      if response == 1:
        # update database
        # redirect to list of requests page
        Label(self.request_frame, text="Request Successful!").pack()
        
        # Button(self.request_frame, text="Proceed to List of Requests Page", command=self.requestlist.show).pack(side="right")

        self.nextPage()

      elif response == 0:
        Label(self.request_frame, text="Request Cancelled").pack()

    def nextPage(self):
      self.master.destroy()
      from customer.listofrequests import ListofRequests
        