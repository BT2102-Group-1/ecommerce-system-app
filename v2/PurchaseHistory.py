from tkinter import *
from tkinter import ttk

def PurchaseHistory():
  window = tk.Tk()
  window.title("Purchase History")
  window.geometry("500x500")
  history_frame = tk.LabelFrame(window, text="Purchase History", padx=20, pady=20)
  frame.pack()
  # Create an object of Style widget
  style = ttk.Style()
  style.theme_use('clam')

  # Add a Treeview widget
  tree = ttk.Treeview(history_frame, column=("FName", "LName", "Roll No"), show='headings', height=5)
  tree.column("# 1", anchor=CENTER)
  tree.heading("# 1", text="FName")
  tree.column("# 2", anchor=CENTER)
  tree.heading("# 2", text="LName")
  tree.column("# 3", anchor=CENTER)
  tree.heading("# 3", text="Roll No")

  # Insert the data in Treeview widget
  tree.insert('', 'end', text="1", values=('Amit', 'Kumar', '17701'))
  tree.insert('', 'end', text="1", values=('Ankush', 'Mathur', '17702'))
  tree.insert('', 'end', text="1", values=('Manisha', 'Joshi', '17703'))
  tree.insert('', 'end', text="1", values=('Shivam', 'Mehrotra', '17704'))

  tree.pack()

  def showInput():
    item_details = tk.Label(history_frame, text=var.get()).pack()

  var = StringVar()
  x = Entry(history_frame, textvariable=var).pack()
  test = Button(history_frame, text="test", command=showInput).pack()

  window.mainloop()