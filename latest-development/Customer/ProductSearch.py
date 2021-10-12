import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import GlobalVariables 
from controller.controller import Connection

def productSearch():
  window = tk.Tk()
  window.title("Product Search")
  window.configure(bg="#f9f9f8")
  window.geometry("800x800")

########CODE FOR SCROLLBAR #########
  main_frame = tk.Frame(window)
  main_frame.configure(bg="#f9f9f8")
  main_frame.pack(fill=tk.BOTH, expand=1)

  my_canvas = tk.Canvas(main_frame)
  my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

  new_frame = tk.LabelFrame(window, bg="#f9f9f8",text="",padx=20, pady=20)

  my_canvas.create_window((0,0), window=new_frame, anchor="nw")
  ########END CODE FOR SCROLLBAR #########

  ######CHANGED SEARCH FRAME AND DISPLAY FRAME TO RENDER IN new_frame (initially was window)

  # Create Frame for Search Options
  search_frame = tk.LabelFrame(new_frame, text="Product Search", bg="#F9FBF2", padx=50, pady=20)
  search_frame.pack()
  display_frame = tk.LabelFrame(new_frame, text="Search Results", bg="#F9FBF2", padx=70, pady=20)
  display_frame.pack()

  # Initialize variables and dictionary
  light1val, light2val, safe1val, safe2val, smarthome1val, locksval, lightsval, whiteval, blueval, yellowval, greenval, blackval, malaysiaval, chinaval, philippinesval, batteryval, usbval, val2020, val2019, val2017, val2016, val2015, val2014 = (tk.StringVar() for i in range(23))

  options = {
    'Model': [light1val, light2val, safe1val, safe2val, smarthome1val],
    'Category': [locksval, lightsval],
    'Color': [whiteval, blueval, yellowval, greenval, blackval],
    'Factory': [malaysiaval, chinaval, philippinesval],
    'PowerSupply': [batteryval, usbval],
    'ProductionYear': [val2020, val2019, val2017, val2016, val2015, val2014]
  }

  for key in options.items():
    for i in key[1]:
      i.set("0")

  # Create dictionary with checked fields and call cusomter search function
  def onSearch():
    dict = {
      'Model': [],
      'Category': [],
      'Color': [],
      'Factory': [],
      'PowerSupply': [],
      'ProductionYear': []
    }

    for key, value in options.items():  
      for i in value:
        if i.get() != "0":
          arr = dict.get(key)
          arr.append(i.get())
          dict[key] = arr
    
    print(dict) 
    # CALL BACKEND --------------------------
    productList = Connection().customerSearch(dict)

    # DUMMY DATA WE DO NOT NEED TO CARE ABOUT EVENTUALLY -----
    # productList = [
    #   ["Light1", "Lights", "$50", "12 Months", [
    #       {"ItemID":"1001", "Color":"White", "Factory":"Malaysia", "PowerSupply":"Battery", "ProductionYear":"2014"
    #       },
    #       {"ItemID":"1002", "Color":"Blue", "Factory":"Malaysia", "PowerSupply":"USB", "ProductionYear":"2016"
    #       },
    #       {"ItemID":"1003", "Color":"White", "Factory":"Philippines", "PowerSupply":"USB", "ProductionYear":"2020"
    #       }
    #     ]
    #   ],
    #   ["Light2", "Lights", "$60", "6 Months", [
    #     {"ItemID":"1283", "Color":"White", "Factory":"Malaysia", "PowerSupply":"Battery", "ProductionYear":"2016"
    #       },
    #       {"ItemID":"1293", "Color":"Yellow", "Factory":"China", "PowerSupply":"USB", "ProductionYear":"2017"
    #       },
    #       {"ItemID":"1296", "Color":"Green", "Factory":"Philippines", "PowerSupply":"Battery", "ProductionYear":"2019"
    #       }
    #     ]
    #   ],
    #   ["SmartHome1", "Lights", "$70", "3 Months", [
    #       {"ItemID":"1374", "Color":"Black", "Factory":"China", "PowerSupply":"Battery", "ProductionYear":"2017"
    #       },
    #       {"ItemID":"1379", "Color":"White", "Factory":"Malaysia", "PowerSupply":"USB", "ProductionYear":"2015"
    #       },
    #       {"ItemID":"1389", "Color":"Yellow", "Factory":"China", "PowerSupply":"USB", "ProductionYear":"2014"
    #       }
    #     ]
    #   ],
    #   ["Safe1", "Locks", "$100", "4 Months", [
    #       {"ItemID":"1423", "Color":"White", "Factory":"China", "PowerSupply":"Battery", "ProductionYear":"2017"
    #       },
    #       {"ItemID":"1436", "Color":"Blue", "Factory":"Malaysia", "PowerSupply":"Battery", "ProductionYear":"2020"
    #       },
    #       {"ItemID":"1493", "Color":"Black", "Factory":"Philippines", "PowerSupply":"USB", "ProductionYear":"2019"
    #       }
    #     ]
    #   ],
    #   ["Safe2", "Locks", "$50", "17 Months", [
    #       {"ItemID":"1542", "Color":"Yellow", "Factory":"Malaysia", "PowerSupply":"Battery", "ProductionYear":"2014"
    #       },
    #       {"ItemID":"1554", "Color":"Blue", "Factory":"Philippines", "PowerSupply":"USB", "ProductionYear":"2016"
    #       },
    #       {"ItemID":"1567", "Color":"Green", "Factory":"Philippines", "PowerSupply":"USB", "ProductionYear":"2020"
    #       }
    #     ]
    #   ],
    #   ["Safe3", "Locks", "$50", "12 Months", [
    #       {"ItemID":"1684", "Color":"White", "Factory":"Malaysia", "PowerSupply":"Battery", "ProductionYear":"2014"
    #         },
    #         {"ItemID":"1693", "Color":"Blue", "Factory":"China", "PowerSupply":"USB", "ProductionYear":"2017"
    #         },
    #         {"ItemID":"1699", "Color":"Black", "Factory":"Philippines", "PowerSupply":"USB", "ProductionYear":"2015"
    #         }
    #     ]
    #   ],
    #   ["SmartHome1", "Locks", "$50", "6 Months", [
    #     {"ItemID":"1783", "Color":"White", "Factory":"Malaysia", "PowerSupply":"Battery", "ProductionYear":"2019"
    #       },
    #       {"ItemID":"1788", "Color":"Blue", "Factory":"Malaysia", "PowerSupply":"USB", "ProductionYear":"2016"
    #       },
    #       {"ItemID":"1790", "Color":"Green", "Factory":"China", "PowerSupply":"Battery", "ProductionYear":"2015"
    #       }
    #     ]
    #   ]
    # ]

    displaySearchResultsandItem(productList)
  
  def displaySearchResultsandItem(productList):
    # Purchase Item
    def purchaseItem():
      # LOOP THROUGH dictionary to see if item exists in the filtered portion
      exists = False 
      for models in productList:
        for item in models[4]:
          if item.get('ItemID') == chosenItemId.get():
            exists = True
            break
        
        if exists: break

      if exists:
        # CALL BACKEND --------------------------
        # successful = purchase(GlobalVariables.customerID, chosenItemId)
        successful = True
        if successful:
          tk.messagebox.showinfo("Success", "Purchase of Item #" + chosenItemId.get() + " is successful!")
        else:
          tk.messagebox.showerror("Error", "Service Request cannot be cancelled!")
      else:
        tk.messagebox.showerror("Error", "Wrong Item ID / No Such Item ID")

    # Text variable
    chosenItemId = tk.StringVar()

    # Choose Item Label
    tk.Label(display_frame, text="Input the Item ID Here: ", bg="#F9FBF2").grid(row=0, column=0, sticky="W")

    # Input Field for Item ID 
    tk.Entry(display_frame, text = "itemId", width=10, textvariable= chosenItemId).grid(row=0, column=1, columnspan=3, sticky="W")
    
    # Purchase Button
    tk.Button(display_frame, height=1, width=10, text="Purchase", bg='#fbf2fa', command=purchaseItem).grid(row=0, column=3, sticky="E")

    tk.Label(display_frame, text=" ", bg="#F9FBF2").grid(row=1)

    print(productList) # DEBUGGING, REMOVE LATER
    displaySearchItems(productList)

  # Display search items
  def displaySearchItems(productList):
    count = 2
    for modelDict in productList:     
      tk.Label(display_frame, bg="#F9FBF2", text="Model: " + modelDict['model'] + ", Category: " + modelDict['category'] + ", Price: " + str(modelDict['price']) + ", Warranty: " + str(modelDict['warranty'])).grid(row=count, column=0, columnspan=4)
      count += 1
      tk.Label(display_frame, bg="#F9FBF2", text="Number of Items In Stock: " + str(len(modelDict['items']))).grid(row=count, column=0, columnspan=4)
      count += 1

      # table = modelDict[0]+modelDict[1]

      product_table = ttk.Treeview(display_frame)
      product_table['columns'] = ("ItemID", "Color", "Factory", "Power Supply", "Production Year")
      ttk.Style().configure("Treeview", background="#d9e9f9", foreground="black", fieldbackground="d9e9f9") 
      ttk.Style().configure('Treeview.Heading', background='#84a5ce', foreground='black')

      product_table.column('#0', width=0, stretch=tk.NO)
      product_table.column('ItemID', anchor=tk.CENTER, width=100)
      product_table.column('Color', anchor=tk.CENTER, width=100)
      product_table.column('Factory', anchor=tk.CENTER, width=120)
      product_table.column('Power Supply', anchor=tk.CENTER, width=150)
      product_table.column('Production Year', anchor=tk.CENTER, width=170)

      product_table.heading('#0', text='', anchor=tk.CENTER)
      product_table.heading('ItemID', text='ItemID', anchor=tk.CENTER)
      product_table.heading('Color', text='Color', anchor=tk.CENTER)
      product_table.heading('Factory', text='Factory', anchor=tk.CENTER)
      product_table.heading('Power Supply', text='Power Supply', anchor=tk.CENTER)
      product_table.heading('Production Year', text='Production Year', anchor=tk.CENTER)

      for item in modelDict['items']:
        itemId = item.get('ItemID')
        color = item.get('Color')
        factory = item.get('Factory')
        powerSupply = item.get('PowerSupply')
        productionYear = item.get('ProductionYear')
        product_table.insert(parent='', index=itemId, iid=itemId, text='', values=(itemId, color, factory, powerSupply, productionYear))
      
      product_table.grid(row = count, column = 0, columnspan=4)
      count += 1
      tk.Label(display_frame, bg="#F9FBF2", text=" ").grid(row=count, column=0)
      count += 1

    # CODE FOR SCROLLAR #
    my_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
    # CODE FOR SCROLLBAR #
    
  # Advance Search Options
  def onClick(): 
    tk.Label(search_frame, text="   ", bg="#F9FBF2").grid(row=5, column=0)

    # Category
    tk.Label(search_frame, text="Category", bg="#F9FBF2").grid(sticky="W", row=6, column=0)
    # Category Options
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "Lights", variable = lightsval, onvalue="Lights").grid(sticky="W", row=6, column=1)
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "Locks", variable = locksval, onvalue="Locks").grid(sticky="W", row=6, column=2)

    # Power Supply
    tk.Label(search_frame, text="Power Supply", bg="#F9FBF2").grid(sticky="W", row=6, column=5)
    # Power Supply Options
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "Battery", variable = batteryval, onvalue="Battery").grid(sticky="W", row=6, column=6)
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "USB", variable = usbval, onvalue="USB").grid(sticky="W", row=6, column=7)

    tk.Label(search_frame, text="   ", bg="#F9FBF2").grid(row=7, column=0)

    # Colour
    tk.Label(search_frame, text="Colour", bg="#F9FBF2").grid(sticky="W", row=8, column=0)
    # Colour Options
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "White", variable = whiteval, onvalue="White").grid(sticky="W", row=8, column=1)
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "Black", variable = blackval, onvalue="Black").grid(sticky="W", row=8, column=2)
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "Blue", variable = blueval, onvalue="Blue").grid(sticky="W", row=8, column=3)
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "Yellow", variable = yellowval, onvalue="Yellow").grid(sticky="W", row=9, column=1)
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "Green", variable = greenval, onvalue="Green").grid(sticky="W", row=9, column=2)

    # Production Year
    tk.Label(search_frame, text="Production Year", bg="#F9FBF2").grid(sticky="W", row=8, column=5)
    # Production Year Options
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "2020", variable = val2020, onvalue="2020").grid(sticky="W", row=8, column=6)
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "2019", variable = val2019, onvalue="2019").grid(sticky="W", row=8, column=7)
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "2017", variable = val2017, onvalue="2017").grid(sticky="W", row=8, column=8)
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "2016", variable = val2016, onvalue="2016").grid(sticky="W", row=9, column=6)
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "2015", variable = val2015, onvalue="2015").grid(sticky="W", row=9, column=7)
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "2014", variable = val2014, onvalue="2014").grid(sticky="W", row=9, column=8)

    tk.Label(search_frame, text="   ", bg="#F9FBF2").grid(row=10, column=0)

    # Factory
    tk.Label(search_frame, text="Factory", bg="#F9FBF2").grid(sticky="W", row=11, column=0)
    # Factory Options
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "Malaysia", variable = malaysiaval, onvalue="Malaysia").grid(sticky="W", row=11, column=1)
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "China", variable = chinaval, onvalue="China").grid(sticky="W", row=11, column=2)
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "Philippines", variable = philippinesval, onvalue="Philippines").grid(sticky="W", row=11, column=3)
  
  # Simple Search Title
  tk.Label(search_frame, text="Simple Search", bg="#F9FBF2").grid(sticky="W", row=0, column=0)
  
  # Model
  tk.Label(search_frame, bg="#F9FBF2", text="Model").grid(sticky="W", row=2, column=0)
  # Model Options
  tk.Checkbutton(search_frame, bg="#F9FBF2", text = "Light1", variable = light1val, onvalue="Light1").grid(row=2, column=1)
  tk.Checkbutton(search_frame, bg="#F9FBF2", text = "Light2", variable = light2val, onvalue="Light2").grid(row=2, column=2)
  tk.Checkbutton(search_frame, bg="#F9FBF2", text = "Safe1", variable = safe1val, onvalue="Safe1").grid(row=2, column=3)
  tk.Checkbutton(search_frame, bg="#F9FBF2", text = "Safe2", variable = safe2val, onvalue="Safe2").grid(row=2, column=4)
  tk.Checkbutton(search_frame, bg="#F9FBF2", text = "Smart Home1", variable = smarthome1val, onvalue="SmartHome1").grid(sticky="W", row=2, column=5)

  # Advance Search Options Button 
  tk.Button(search_frame, text="Advance Search", bg='#fbf2fa', command=onClick).grid(sticky="W", row=2, column=8)
  # Search Button
  tk.Button(search_frame, text="Search", bg='#fbf2fa', command=onSearch).grid(sticky="W", row=15, column=8)

  # Styling Spaces
  tk.Label(search_frame, text="   ", bg="#F9FBF2").grid(row=1, column=0)
  tk.Label(search_frame, text="   ", bg="#F9FBF2").grid(row=14, column=0)
  tk.Label(search_frame, text="   ", bg="#F9FBF2").grid(row=1, column=7)

  # Return to Customer Menu
  def redirectToMenu():
    window.destroy()
    from Customer.CustomerMenu import customerMenu
    customerMenu()

  # Return to Customer Menu Button
  tk.Button(search_frame, text="Return to Menu", bg='#fbf2fa', command = redirectToMenu).grid(row=0, column=8)
  # tk.Label(search_frame, text=" ").grid(row=15,  column=0)
  
  window.mainloop() 