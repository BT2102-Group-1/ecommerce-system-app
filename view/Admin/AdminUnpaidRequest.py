import tkinter as tk
from tkinter import ttk

from controller.controller import Connection

def adminUnpaidRequest():

  window = tk.Tk()
  window.title("Admin - Customers with Unpaid Requests")
  window.geometry("800x800")
  window.configure(bg="#f9f9f8")

  frame = tk.LabelFrame(window, bg="#F9FBF2", text="Customers with Unpaid Requests", padx=20, pady=20)
  frame.pack()
  
  # unpaidRequests = [ #HARD CODED DATA, REMOVE DATA and SET IT = controller.getUnpaidServiceCustomers()
  #   {
  #     "requestId": "84930293",
  #     "requestDate": "10/10/2021",
  #     "customerId": "3",
  #     "itemId": "1001"
  #   },
  #   {
  #     "requestId": "43923231",
  #     "requestDate": "6/10/2021",
  #     "customerId": "2",
  #     "itemId": "1431"
  #   },
  #   {
  #     "requestId": "32939203",
  #     "requestDate": "1/10/2021",
  #     "customerId": "4",
  #     "itemId": "1342"
  #   },
  #     {
  #     "requestId": "84932393",
  #     "requestDate": "10/10/2021",
  #     "customerId": "3",
  #     "itemId": "1001"
  #   },
  #   {
  #     "requestId": "43914231",
  #     "requestDate": "6/10/2021",
  #     "customerId": "2",
  #     "itemId": "1431"
  #   },
  #   {
  #     "requestId": "329329203",
  #     "requestDate": "1/10/2021",
  #     "customerId": "4",
  #     "itemId": "1342"
  #   },
  #   {
  #     "requestId": "8426493",
  #     "requestDate": "10/10/2021",
  #     "customerId": "3",
  #     "itemId": "1001"
  #   },
  #   {
  #     "requestId": "439233231",
  #     "requestDate": "6/10/2021",
  #     "customerId": "2",
  #     "itemId": "1431"
  #   },
  #   {
  #     "requestId": "239233",
  #     "requestDate": "1/10/2021",
  #     "customerId": "4",
  #     "itemId": "1342"
  #   },
  #   {
  #     "requestId": "32923203",
  #     "requestDate": "1/10/2021",
  #     "customerId": "4",
  #     "itemId": "1342"
  #   },
  #   {
  #     "requestId": "8414393",
  #     "requestDate": "10/10/2021",
  #     "customerId": "3",
  #     "itemId": "1001"
  #   },
  #   {
  #     "requestId": "43912231",
  #     "requestDate": "6/10/2021",
  #     "customerId": "2",
  #     "itemId": "1431"
  #   },
  #   {
  #     "requestId": "329323233",
  #     "requestDate": "1/10/2021",
  #     "customerId": "4",
  #     "itemId": "1342"
  #   }
  # ]

  ## CALL BACKEND --------------------------
  # remove hardcoded list of dictionaries above under variable "unpaidRequests"
  unpaidRequests = Connection().getUnpaidServiceCustomers()
  ## ---------------------------------------


  # ------------------ Table View -------------------- #
  table = ttk.Treeview(frame)
  ttk.Style().configure("Treeview", background="#d9e9f9", foreground="black", fieldbackground="d9e9f9")
  ttk.Style().configure('Treeview.Heading', background='#84a5ce',   foreground='black')

  ##Code for Scrollbar##
  verscrlbar = ttk.Scrollbar(frame, orient="vertical", command = table.yview)
  verscrlbar.grid(row=1, sticky ='nes')
  table.configure(yscrollcommand = verscrlbar.set)

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

  for item in unpaidRequests:
    requestId = item.get('requestId')
    requestDate = item.get('requestDate')
    customerId = item.get('customerId')
    itemId = item.get('itemId')
    table.insert(parent='', index=requestId, iid=requestId, text='', values=(requestId, requestDate, customerId, itemId))

  table.grid(row=1, column=0)
  # ------------End of Table View -------------------- #

  def redirectToMenu():
    window.destroy()
    from view.Admin.AdminMenu import adminMenu
    adminMenu()

  tk.Button(frame, text="Return to Menu", bg="#F9FBF2", command = redirectToMenu).grid(row=2, column=0, pady=15)

  window.mainloop()