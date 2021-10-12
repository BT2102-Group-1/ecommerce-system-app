import tkinter as tk
from tkinter import ttk

def adminViewInventory():

  window = tk.Tk()
  window.title("Admin - View Inventory")
  window.geometry("800x800")
  window.configure(bg="#f9f9f8")

  frame = tk.LabelFrame(window, text="Inventory", bg="#F9FBF2", width=400, height=400, padx=20, pady=20)

  # ------------------ Table View -------------------- #
  tv = ttk.Treeview(frame)
  ttk.Style().configure("Treeview", background="#d9e9f9", foreground="black", fieldbackground="#d9e9f9")
  ttk.Style().configure('Treeview.Heading', background='#84a5ce',   foreground='black')

  ##Code for Scrollbar##
  verscrlbar = ttk.Scrollbar(frame, orient="vertical", command = tv.yview)
  verscrlbar.grid(row=1, sticky ='nes')
  tv.configure(yscrollcommand = verscrlbar.set)
  
  tv['columns']=('ProductID', 'Number of "SOLD" items', 'Number of "UNSOLD" items')

  tv.column('#0', width=0, stretch=tk.NO)
  tv.column('ProductID', anchor=tk.CENTER, width=110)
  tv.column('Number of "SOLD" items', anchor=tk.CENTER, width=250)
  tv.column('Number of "UNSOLD" items', anchor=tk.CENTER, width=290)

  tv.heading('#0', text='', anchor=tk.CENTER)
  tv.heading('ProductID', text='ProductID', anchor=tk.CENTER)
  tv.heading('Number of "SOLD" items', text='Number of "SOLD" items', anchor=tk.CENTER)
  tv.heading('Number of "UNSOLD" items', text='Number of "UNSOLD" items', anchor=tk.CENTER)

  dicts = [ #REMOVE HARDCODED DATA, SET IT = controller.viewInventory()
    {"productId": "1", "soldItems": 90, "unsoldItems": 9},
    {"productId": "2", "soldItems": 136, "unsoldItems": 163},
    {"productId": "3", "soldItems": 29, "unsoldItems": 74},
    {"productId": "4", "soldItems": 31, "unsoldItems": 99},
    {"productId": "5", "soldItems": 46, "unsoldItems": 99},
    {"productId": "6", "soldItems": 46, "unsoldItems": 95},
    {"productId": "7", "soldItems": 50, "unsoldItems": 82}
  ]

  ## CALL BACKEND --------------------------
  # remove hardcoded list of dictionaries above under variable "dicts"
  # set "dicts = controller.viewInventory()" [expecting to get a list of dictionaries]
  ## ---------------------------------------

  for dict in dicts:
    productId = dict.get('productId')
    soldItems = dict.get('soldItems')
    unsoldItems = dict.get('unsoldItems')
    tv.insert(parent='', index=productId, iid=productId, text='', values=(productId, soldItems, unsoldItems))
  tv.grid(row=1, column=0)
  # ------------End of Table View -------------------- #

  def redirectToMenu():
    window.destroy()
    from view.Admin.AdminMenu import adminMenu
    adminMenu()

  tk.Button(frame, text="Return to Menu", bg='#fbf2fa', command = redirectToMenu).grid(row=2, pady=15)

  frame.pack()
  
  window.mainloop()