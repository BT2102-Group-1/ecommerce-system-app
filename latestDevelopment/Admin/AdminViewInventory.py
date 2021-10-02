import tkinter as tk
from tkinter import ttk

def adminViewInventory():

  window = tk.Tk()
  window.title("Admin - View Inventory")
  window.geometry("800x800")

 #add frame
  frame = tk.LabelFrame(window, text="Inventory", width=400, height=400, padx=20, pady=20)

  #print welcome message just to show it renders
  tk.Label(frame, text = "Welcome to Inventory Page").pack()

  ###############TABLE#################
  #window['bg']='#fb0'

  tv = ttk.Treeview(frame)
  tv['columns']=('ProductID', 'Number of "SOLD" items', 'Number of "UNSOLD" items')
  tv.column('#0', width=0, stretch=tk.NO)
  tv.column('ProductID', anchor=tk.CENTER, width=110)
  tv.column('Number of "SOLD" items', anchor=tk.CENTER, width=230)
  tv.column('Number of "UNSOLD" items', anchor=tk.CENTER, width=260)

  tv.heading('#0', text='', anchor=tk.CENTER)
  tv.heading('ProductID', text='ProductID', anchor=tk.CENTER)
  tv.heading('Number of "SOLD" items', text='Number of "SOLD" items', anchor=tk.CENTER)
  tv.heading('Number of "UNSOLD" items', text='Number of "UNSOLD" items', anchor=tk.CENTER)

  tv.insert(parent='', index=0, iid=0, text='', values=('1','90','9'))
  tv.insert(parent='', index=1, iid=1, text='', values=('2','136','163'))
  tv.insert(parent='', index=2, iid=2, text='', values=('3','29','74'))
  tv.insert(parent='', index=3, iid=3, text='', values=('4','31','54'))
  tv.insert(parent='', index=4, iid=4, text='', values=('5','46','99'))
  tv.insert(parent='', index=5, iid=5, text='', values=('5','46','99'))
  tv.insert(parent='', index=6, iid=6, text='', values=('6','50','95'))
  tv.insert(parent='', index=7, iid=7, text='', values=('7','43','82'))
  tv.pack()

############################################

  # Redirect to Initialise Database
  def redirectToMenu():
    window.destroy()
    from Admin.AdminMenu import adminMenu
    adminMenu()

  tk.Button(frame, text="Return to Menu", command = redirectToMenu).pack(pady = 5)
  frame.pack()

  window.mainloop()