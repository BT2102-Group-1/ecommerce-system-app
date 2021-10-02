import tkinter as tk
from tkinter import ttk


root = tk.Tk()
frame = tk.LabelFrame(root, text="NavBar", padx=20, pady=20)
frame.pack()

notebook = ttk.Notebook(root)
notebook.pack() 
purchase_search = tk.Frame(notebook, width=500, height=500, bg="red")
purchase_history = tk.Frame(notebook, width=500, height=500, bg="blue")

purchase_search.pack(fil = "both",expand=1)
purchase_history.pack(fil = "both",expand=1)
notebook.add(purchase_search, text = "Purchase Search")
notebook.add(purchase_history, text = "Purchase History")

frame.mainloop()


