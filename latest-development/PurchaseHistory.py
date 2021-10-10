import tkinter as tk
from tkinter import ttk
from main import *

def purchaseHistory():
  window = tk.Tk()
  window.title("Purchase History")
  window.geometry("700x700")

  # Create Frame for List of Purchase History
  frame = tk.LabelFrame(window, text="Purchase History", padx=20, pady=20)
  frame.grid(row=0, column=0)

  # DUMMY DATA THAT"LL BE DELETED>.. -----
  dummydata = [
    {"itemId":"1001", "purchaseDate": "10/10/2021", "modelPrice": "$60", "modelName": "Light2", "categoryName": "Lights", "color":"White", "factory":"Malaysia", "powerSupply":"Battery", "productionYear":"2014"
    },
    {"itemId":"4523", "purchaseDate": "10/10/2021", "modelPrice": "$50", "modelName": "Light1", "categoryName": "Lights", "color":"White", "factory":"Malaysia", "powerSupply":"Battery", "productionYear":"2014"
    },
    {"itemId":"4368", "purchaseDate": "10/10/2021", "modelPrice": "$100", "modelName": "SmartHome1", "categoryName": "Lights", "color":"White", "factory":"Malaysia", "powerSupply":"Battery", "productionYear":"2014"
    },
    {"itemId":"2597", "purchaseDate": "10/10/2021", "modelPrice": "$50", "modelName": "Light1", "categoryName": "Lights", "color":"White", "factory":"Malaysia", "powerSupply":"Battery", "productionYear":"2014"
    },
    {"itemId":"6364", "purchaseDate": "10/10/2021", "modelPrice": "$50", "modelName": "Light1", "categoryName": "Lights", "color":"White", "factory":"Malaysia", "powerSupply":"Battery", "productionYear":"2014"
    }
  ]

  # Table View 
  table = ttk.Treeview(frame)
  table['columns'] = ("Item ID", "Purchase Date", "Category Name", "Model Name", "Model Price", "Color", "Factory", "Power Supply", "Production Year")

  table.column('#0', width=0, stretch=tk.NO)
  table.column('Item ID', anchor=tk.CENTER, width=150)
  table.column('Purchase Date', anchor=tk.CENTER, width=300)
  table.column('Category Name', anchor=tk.CENTER, width=300)
  table.column('Model Name', anchor=tk.CENTER, width=250)
  table.column('Model Price', anchor=tk.CENTER, width=250)
  table.column('Color', anchor=tk.CENTER, width=130)
  table.column('Factory', anchor=tk.CENTER, width=120)
  table.column('Power Supply', anchor=tk.CENTER, width=280)
  table.column('Production Year', anchor=tk.CENTER, width=400)

  table.heading('#0', text='', anchor=tk.CENTER)
  table.heading('Item ID', text='Item ID', anchor=tk.CENTER)
  table.heading('Purchase Date', text='Purchase Date', anchor=tk.CENTER)
  table.heading('Category Name', text='Category Name', anchor=tk.CENTER)
  table.heading('Model Name', text='Model Name', anchor=tk.CENTER)
  table.heading('Model Price', text='Model Price', anchor=tk.CENTER)
  table.heading('Color', text='Color', anchor=tk.CENTER)
  table.heading('Factory', text='Factory', anchor=tk.CENTER)
  table.heading('Power Supply', text='Power Supply', anchor=tk.CENTER)
  table.heading('Production Year', text='Production Year', anchor=tk.CENTER)

  # Displaying Data  
  for item in dummydata:
    itemId = item.get('itemId')
    purchaseDate = item.get('purchaseDate')
    categoryName = item.get('categoryName')
    modelName = item.get('modelName')
    modelPrice = item.get('modelPrice')
    color = item.get('color')
    factory = item.get('factory')
    powerSupply = item.get('powerSupply')
    productionYear = item.get('productionYear')

    table.insert(parent='', index=itemId, iid=itemId, text='', values=(itemId, purchaseDate, categoryName, modelName, modelPrice, color, factory, powerSupply, productionYear))

  table.grid(row=1, column=0)

  def redirectToMenu():
    window.destroy()
    from CustomerMenu import customerMenu
    customerMenu()

  tk.Button(window, text="Return to Menu", command = redirectToMenu).grid(row=2, column=0)

  window.mainloop()