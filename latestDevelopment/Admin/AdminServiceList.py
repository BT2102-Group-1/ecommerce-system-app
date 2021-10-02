import tkinter as tk
from tkinter import ttk

def adminUnpaidRequest():

  window = tk.Tk()
  window.title("Admin - Requests with Unpaid Service Fee")
  window.geometry("500x500")

 #add frame
  frame = tk.LabelFrame(window, text="Requests with Unpaid Service Fee", padx=20, pady=20)


  #print welcome message just to show it renders
  tk.Label(frame, text = "Welcome to Requests with Unpaid Service Fee Page").pack()

###TEST METHOD#####
  tempList = [['Jim', '0.33'], ['Dave', '0.67'], ['James', '0.67'], ['Eden', '0.5']]
  tempList.sort(key=lambda e: e[1], reverse=True)

  for i, (name, score) in enumerate(tempList, start=1):
    listBox.insert("", "end", values=(i, name, score))

  label = tk.Label(window, text="High Scores", font=("Arial",30)).grid(row=0, columnspan=3)
  # create Treeview with 3 columns
  cols = ('Position', 'Name', 'Score')
  listBox = ttk.Treeview(window, columns=cols, show='headings')
  # set column headings
  for col in cols:
      listBox.heading(col, text=col)    
  listBox.grid(row=1, column=0, columnspan=2)

  showScores = tk.Button(window, text="Show window", width=15, command=show).grid(row=4, column=0)
  closeButton = tk.Button(window, text="Close", width=15, command=exit).grid(row=4, column=1)
###TEST METHOD#####


  # Redirect to Initialise Database
  def redirectToMenu():
    window.destroy()
    from Admin.AdminMenu import adminMenu
    adminMenu()

  tk.Button(frame, text="Return to Menu", command = redirectToMenu).pack(pady = 5)
  frame.pack()

  window.mainloop()