from tkinter import *
from tkinter import ttk
from main import *
from tkinter import messagebox

def listOfRequests():
  window = tk.Tk()
  window.title("Request Service")
  window.geometry("500x500")
  frame = tk.LabelFrame(window, text="List Of Service ", padx=20, pady=20)
  frame.pack()
  
  tree = ttk.Treeview(frame)

  #Define Columns
  tree['columns'] = ("Item ID", "Request Date", "Service Fee", "Request Status")

  #Format Column and create headings 
  tree.column("#0", width=0)
  tree.column("Item ID", anchor=CENTER)
  tree.heading("Item ID", text = "Item ID")
  tree.column("Request Date", anchor=CENTER)
  tree.heading("Request Date", text = "Request Date")
  tree.column("Service Fee", anchor=CENTER)
  tree.heading("Service Fee", text = "Service Fee")
  tree.column("Request Status", anchor=CENTER)
  tree.heading("Request Status", text = "Request Status")
  #tree.column("Action", anchor=CENTER)
  #tree.heading("Action", text = "Action")
  #tree.column(" ", anchor=CENTER)

  tree.insert('', 'end', values=('1001', '1st June', '$300', "Pending"))
  
  tree.pack()