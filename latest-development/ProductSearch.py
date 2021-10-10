import tkinter as tk
from tkinter import ttk
from main import *

def productSearch():
  window = tk.Tk()
  window.title("Product Search")
  window.geometry("700x700")

  # Create Frame for Search Options
  search_frame = tk.LabelFrame(window, text="Product Search", padx=20, pady=20)
  search_frame.pack()
  display_frame = tk.LabelFrame(window, text="Search Results", padx=20, pady=20)
  display_frame.pack()

  # DUMMY DATA WE DO NOT NEED TO CARE ABOUT EVENTUALLY -----
  # RETURN VALUE: arr = [[productNameVar, price, # of items in stock, warranty, [list of items objects]],[[productNameVar, price, # of items in stock, warranty, [list of items objects]],[[productNameVar, price, # of items in stock, warranty, [list of items objects]] etc ..
  dummydata = [
    ["Light1", "Lights", "$50", "96", [
        {"ItemID":"1001", "Color":"White", "Factory":"Malaysia", "PowerSupply":"Battery", "ProductionYear":"2014"
        },
        {"ItemID":"1002", "Color":"Blue", "Factory":"Malaysia", "PowerSupply":"USB", "ProductionYear":"2016"
        },
        {"ItemID":"1003", "Color":"White", "Factory":"Philippines", "PowerSupply":"USB", "ProductionYear":"2020"
        }
      ]
    ],
    ["Light2", "Lights", "$60", "96", [
      {"ItemID":"1283", "Color":"White", "Factory":"Malaysia", "PowerSupply":"Battery", "ProductionYear":"2016"
        },
        {"ItemID":"1293", "Color":"Yellow", "Factory":"China", "PowerSupply":"USB", "ProductionYear":"2017"
        },
        {"ItemID":"1296", "Color":"Green", "Factory":"Philippines", "PowerSupply":"Battery", "ProductionYear":"2019"
        }
      ]
    ]
    # ["SmartHome1", "Lights", "$70", "96", [
    #     {"ItemID":"1374", "Color":"Black", "Factory":"China", "PowerSupply":"Battery", "ProductionYear":"2017"
    #     },
    #     {"ItemID":"1379", "Color":"White", "Factory":"Malaysia", "PowerSupply":"USB", "ProductionYear":"2015"
    #     },
    #     {"ItemID":"1389", "Color":"Yellow", "Factory":"China", "PowerSupply":"USB", "ProductionYear":"2014"
    #     }
    #   ]
    # ],
    # ["Safe1", "Locks", "$100", "96", [
    #     {"ItemID":"1423", "Color":"White", "Factory":"China", "PowerSupply":"Battery", "ProductionYear":"2017"
    #     },
    #     {"ItemID":"1436", "Color":"Blue", "Factory":"Malaysia", "PowerSupply":"Battery", "ProductionYear":"2020"
    #     },
    #     {"ItemID":"1493", "Color":"Black", "Factory":"Philippines", "PowerSupply":"USB", "ProductionYear":"2019"
    #     }
    #   ]
    # ],
    # ["Safe2", "Locks", "$50", "96", [
    #     {"ItemID":"1542", "Color":"Yellow", "Factory":"Malaysia", "PowerSupply":"Battery", "ProductionYear":"2014"
    #     },
    #     {"ItemID":"1554", "Color":"Blue", "Factory":"Philippines", "PowerSupply":"USB", "ProductionYear":"2016"
    #     },
    #     {"ItemID":"1567", "Color":"Green", "Factory":"Philippines", "PowerSupply":"USB", "ProductionYear":"2020"
    #     }
    #   ]
    # ],
    # ["Safe3", "Locks", "$50", "96", [
    #     {"ItemID":"1684", "Color":"White", "Factory":"Malaysia", "PowerSupply":"Battery", "ProductionYear":"2014"
    #       },
    #       {"ItemID":"1693", "Color":"Blue", "Factory":"China", "PowerSupply":"USB", "ProductionYear":"2017"
    #       },
    #       {"ItemID":"1699", "Color":"Black", "Factory":"Philippines", "PowerSupply":"USB", "ProductionYear":"2015"
    #       }
    #   ]
    # ],
    # ["SmartHome1", "Locks", "$50", "96", [
    #   {"ItemID":"1783", "Color":"White", "Factory":"Malaysia", "PowerSupply":"Battery", "ProductionYear":"2019"
    #     },
    #     {"ItemID":"1788", "Color":"Blue", "Factory":"Malaysia", "PowerSupply":"USB", "ProductionYear":"2016"
    #     },
    #     {"ItemID":"1790", "Color":"Green", "Factory":"China", "PowerSupply":"Battery", "ProductionYear":"2015"
    #     }
    #   ]
    # ]
  ]
  # Initialize variables and dictionary
  light1val, light2val, safe1val, safe2val, smarthome1val, locksval, lightsval, whiteval, blueval, yellowval, greenval, blackval, malaysiaval, chinaval, philippinesval, batteryval, usbval, val2020, val2019, val2017, val2016, val2015, val2014 = (tk.StringVar() for i in range(23))

  options = {
    'Model': [light1val, light2val, safe1val, safe2val, smarthome1val],
    'Category': [locksval, lightsval],
    'Colour': [whiteval, blueval, yellowval, greenval, blackval],
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
      'Colour': [],
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
    # Call backend function customerSearch(dict) to get items array
    items = []
    displaySearchItems(dummydata)
  
  # Display search items
  def displaySearchItems(items):
    # tk.Button(display_frame, height=1, width=10, text="Purchase").grid(row=0, column=0)

    count = 1
    index = 0
    dict = {}
    for modelDict in items:
      tableIndex = "product_table"
      tableIndex += str(index)
      index+=1 
      print(tableIndex)    
    
      tk.Label(display_frame, text="Model: " + modelDict[0] + ", Category: " + modelDict[1] + ", Price: " + modelDict[2]).grid(row=count, column=0)
      count += 1
      tk.Label(display_frame, text="Number of Items In Stock: " + str(len(modelDict[4]))).grid(row=count, column=0)
      count += 1

      # table = modelDict[0]+modelDict[1]

      dict[tableIndex]=ttk.Treeview(display_frame)
      print(dict[tableIndex])
      dict[tableIndex]['columns'] = ("ItemID", "Color", "Factory", "Power Supply", "Production Year")

      def selectItem(a):
        curItem = dict[tableIndex].focus()
        print(curItem)
        print(dict[tableIndex].item(curItem)) 


      dict[tableIndex].column('#0', width=0, stretch=tk.NO)
      dict[tableIndex].column('ItemID', anchor=tk.CENTER, width=100)
      dict[tableIndex].column('Color', anchor=tk.CENTER, width=100)
      dict[tableIndex].column('Factory', anchor=tk.CENTER, width=120)
      dict[tableIndex].column('Power Supply', anchor=tk.CENTER, width=150)
      dict[tableIndex].column('Production Year', anchor=tk.CENTER, width=170)

      dict[tableIndex].heading('#0', text='', anchor=tk.CENTER)
      dict[tableIndex].heading('ItemID', text='ItemID', anchor=tk.CENTER)
      dict[tableIndex].heading('Color', text='Color', anchor=tk.CENTER)
      dict[tableIndex].heading('Factory', text='Factory', anchor=tk.CENTER)
      dict[tableIndex].heading('Power Supply', text='Power Supply', anchor=tk.CENTER)
      dict[tableIndex].heading('Production Year', text='Production Year', anchor=tk.CENTER)
      dict[tableIndex].bind('<ButtonRelease-1>', selectItem)

      for item in modelDict[4]:
        itemId = item.get('ItemID')
        color = item.get('Color')
        factory = item.get('Factory')
        powerSupply = item.get('PowerSupply')
        productionYear = item.get('ProductionYear')
        dict[tableIndex].insert(parent='', index=itemId, iid=itemId, text='', values=(itemId, color, factory, powerSupply, productionYear))
      
      dict[tableIndex].grid(row = count, column = 0)
      count += 1
      tk.Label(display_frame, text=" ").grid(row=count, column=0)
      count += 1

    print(dict)
  
      
  # Advance Search Options
  def onClick(): 
    tk.Label(search_frame, text="   ").grid(row=4, column=0)

    # Category
    tk.Label(search_frame, text="Category").grid(sticky="W", row=5, column=0)
    # Category Options
    tk.Checkbutton(search_frame, text = "Lights", variable = lightsval, onvalue="Lights").grid(sticky="W", row=5, column=1)
    tk.Checkbutton(search_frame, text = "Locks", variable = locksval, onvalue="Locks").grid(sticky="W", row=5, column=2)

    # Power Supply
    tk.Label(search_frame, text="Power Supply").grid(sticky="W", row=5, column=5)
    # Power Supply Options
    tk.Checkbutton(search_frame, text = "Battery", variable = batteryval, onvalue="Battery").grid(sticky="W", row=5, column=6)
    tk.Checkbutton(search_frame, text = "USB", variable = usbval, onvalue="USB").grid(sticky="W", row=5, column=7)

    tk.Label(search_frame, text="   ").grid(row=6, column=0)

    # Colour
    tk.Label(search_frame, text="Colour").grid(sticky="W", row=7, column=0)
    # Colour Options
    tk.Checkbutton(search_frame, text = "White", variable = whiteval, onvalue="White").grid(sticky="W", row=7, column=1)
    tk.Checkbutton(search_frame, text = "Black", variable = blackval, onvalue="Black").grid(sticky="W", row=7, column=2)
    tk.Checkbutton(search_frame, text = "Blue", variable = blueval, onvalue="Blue").grid(sticky="W", row=7, column=3)
    tk.Checkbutton(search_frame, text = "Yellow", variable = yellowval, onvalue="Yellow").grid(sticky="W", row=8, column=1)
    tk.Checkbutton(search_frame, text = "Green", variable = greenval, onvalue="Green").grid(sticky="W", row=8, column=2)

    # Production Year
    tk.Label(search_frame, text="Production Year").grid(sticky="W", row=7, column=5)
    # Production Year Options
    tk.Checkbutton(search_frame, text = "2020", variable = val2020, onvalue="2020").grid(sticky="W", row=7, column=6)
    tk.Checkbutton(search_frame, text = "2019", variable = val2019, onvalue="2019").grid(sticky="W", row=7, column=7)
    tk.Checkbutton(search_frame, text = "2017", variable = val2017, onvalue="2017").grid(sticky="W", row=7, column=8)
    tk.Checkbutton(search_frame, text = "2016", variable = val2016, onvalue="2016").grid(sticky="W", row=8, column=6)
    tk.Checkbutton(search_frame, text = "2015", variable = val2015, onvalue="2015").grid(sticky="W", row=8, column=7)
    tk.Checkbutton(search_frame, text = "2014", variable = val2014, onvalue="2014").grid(sticky="W", row=8, column=8)

    tk.Label(search_frame, text="   ").grid(row=9, column=0)

    # Factory
    tk.Label(search_frame, text="Factory").grid(sticky="W", row=10, column=0)
    # Factory Options
    tk.Checkbutton(search_frame, text = "Malaysia", variable = malaysiaval, onvalue="Malaysia").grid(sticky="W", row=10, column=1)
    tk.Checkbutton(search_frame, text = "China", variable = chinaval, onvalue="China").grid(sticky="W", row=10, column=2)
    tk.Checkbutton(search_frame, text = "Philippines", variable = philippinesval, onvalue="Philippines").grid(sticky="W", row=10, column=3)
  
  # Simple Search Title
  tk.Label(search_frame, text="Simple Search").grid(sticky="W", row=0, column=0)
  
  # Model
  tk.Label(search_frame, text="Model").grid(sticky="W", row=1, column=0)
  # Model Options
  tk.Checkbutton(search_frame, text = "Light1", variable = light1val, onvalue="Light1").grid(row=1, column=1)
  tk.Checkbutton(search_frame, text = "Light2", variable = light2val, onvalue="Light2").grid(row=1, column=2)
  tk.Checkbutton(search_frame, text = "Safe1", variable = safe1val, onvalue="Safe1").grid(row=1, column=3)
  tk.Checkbutton(search_frame, text = "Safe2", variable = safe2val, onvalue="Safe2").grid(row=1, column=4)
  tk.Checkbutton(search_frame, text = "Smart Home1", variable = smarthome1val, onvalue="SmartHome1").grid(sticky="W", row=1, column=5)

  # Advance Search Options Button 
  tk.Button(search_frame, text="Advance Search", command=onClick).grid(sticky="W", row=1, column=8)
  # Search Button
  tk.Button(search_frame, text="Search", command=onSearch).grid(sticky="W", row=14, column=8)

  # Styling Spaces
  tk.Label(search_frame, text="   ").grid(row=13, column=0)
  tk.Label(search_frame, text="   ").grid(row=1, column=7)
  
  window.mainloop() 