import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from controller.controller import Connection

def adminProductCatalogue():
  window = tk.Tk()
  window.title("Admin Product Catalogue")
  window.geometry("800x800")
  window.configure(bg="#f9f9f8")

  #---CODE FOR SCROLLBAR -------#
  main_frame = tk.Frame(window)
  main_frame.configure(bg="#f9f9f8")
  main_frame.pack(fill=tk.BOTH, expand=1)

  my_canvas = tk.Canvas(main_frame)
  my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

  new_frame = tk.LabelFrame(window, bg="#f9f9f8", text="",padx=20, pady=20)

  my_canvas.create_window((0,0), window=new_frame, anchor="nw")
  #------------------------------#

  # Create Frame for Search Options
  search2_frame = tk.LabelFrame(new_frame, bg="#F9FBF2",  text="Search by Item ID",padx=250, pady=20)
  search2_frame.pack()
  search_frame = tk.LabelFrame(new_frame, bg="#F9FBF2", text="Product Search",padx=60, pady=20)
  search_frame.pack()
  display_frame = tk.LabelFrame(new_frame, bg="#F9FBF2", text="Search Results",padx=20, pady=20)
  display_frame.pack()

  # Initialize variables and dictionary
  light1val, light2val, safe1val, safe2val, smarthome1val, locksval, lightsval, whiteval, blueval, yellowval, greenval, blackval, malaysiaval, chinaval, philippinesval, batteryval, usbval, val2020, val2019, val2017, val2016, val2015, val2014, soldval, unsoldval = (tk.StringVar() for i in range(25))

  options = {
    'Model': [light1val, light2val, safe1val, safe2val, smarthome1val],
    'Category': [locksval, lightsval],
    'Color': [whiteval, blueval, yellowval, greenval, blackval],
    'Factory': [malaysiaval, chinaval, philippinesval],
    'PowerSupply': [batteryval, usbval],
    'ProductionYear': [val2020, val2019, val2017, val2016, val2015, val2014],
    'PurchaseStatus': [soldval, unsoldval]
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
      'ProductionYear': [],
      'PurchaseStatus': []
    }

    for key, value in options.items():  
      for i in value:
        if i.get() != "0":
          arr = dict.get(key)
          arr.append(i.get())
          dict[key] = arr
    
    print(dict) 
    # CALL BACKEND -------------------------- 
    productList = Connection().adminSearch(dict)
    if (not bool(productList)):
      tk.messagebox.showerror("Error", "No items matching that search were found.")
    else:
      window.update()
    displaySearchItems(productList)

  # Display search items
  def displaySearchItems(productList):
    count = 2
    for modelDict in productList:     
      tk.Label(display_frame, bg="#F9FBF2", text="Model: " + modelDict['model'] + ", Category: " + modelDict['category'] + ", Price: " + str(modelDict['price'])).grid(row=count, column=0, columnspan=4)
      count += 1
      tk.Label(display_frame, bg="#F9FBF2", text="Cost of Service: $" + str(modelDict['serviceFee']) + ", Warranty: " + str(modelDict['warranty'])).grid(row=count, column=0, columnspan=4)
      count += 1
      tk.Label(display_frame, bg="#F9FBF2", text="Number of Items Sold: " + str(modelDict['numItemsSold']) + ", Number of Items Unsold: " + str(modelDict['numItemsInStock'])).grid(row=count, column=0, columnspan=4)
      count += 1

      product_table = ttk.Treeview(display_frame)
      product_table['columns'] = ("ItemID", "Color", "Factory", "Power Supply", "Production Year", "Purchase Status")
      ttk.Style().configure("Treeview", background="#d9e9f9", foreground="black", fieldbackground="#d9e9f9")
      ttk.Style().configure('Treeview.Heading', background='#84a5ce',   foreground='black')

      product_table.column('#0', width=0, stretch=tk.NO)
      product_table.column('ItemID', anchor=tk.CENTER, width=100)
      product_table.column('Color', anchor=tk.CENTER, width=100)
      product_table.column('Factory', anchor=tk.CENTER, width=120)
      product_table.column('Power Supply', anchor=tk.CENTER, width=150)
      product_table.column('Production Year', anchor=tk.CENTER, width=170)
      product_table.column('Purchase Status', anchor=tk.CENTER, width=170)

      product_table.heading('#0', text='', anchor=tk.CENTER)
      product_table.heading('ItemID', text='ItemID', anchor=tk.CENTER)
      product_table.heading('Color', text='Color', anchor=tk.CENTER)
      product_table.heading('Factory', text='Factory', anchor=tk.CENTER)
      product_table.heading('Power Supply', text='Power Supply', anchor=tk.CENTER)
      product_table.heading('Production Year', text='Production Year', anchor=tk.CENTER)
      product_table.heading('Purchase Status', text='Purchase Status', anchor=tk.CENTER)

      for item in modelDict['items']:
        itemId = item.get('ItemID')
        color = item.get('Color')
        factory = item.get('Factory')
        powerSupply = item.get('PowerSupply')
        productionYear = item.get('ProductionYear')
        purchaseStatus = item.get('PurchaseStatus')
        product_table.insert(parent='', index=itemId, iid=itemId, text='', values=(itemId, color, factory, powerSupply, productionYear, purchaseStatus))
      
      product_table.grid(row = count, column = 0, columnspan=4)
      count += 1
      tk.Label(display_frame, text=" ", bg="#F9FBF2").grid(row=count, column=0)
      count += 1

    #---CODE FOR SCROLLBAR---#
    my_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
    #----------------------#
    
  # Advance Search Options
  def onClick(): 
    tk.Label(search_frame, text="   ", bg="#F9FBF2").grid(row=5, column=0)

    # Category
    tk.Label(search_frame, text="Category", bg="#F9FBF2").grid(sticky="W", row=6, column=0)
    # Category Options
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "Lights", variable = lightsval, onvalue="Lights").grid(sticky="W", row=6, column=1)
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "Locks", variable = locksval, onvalue="Locks").grid(sticky="W", row=6, column=2)

    # Power Supply
    tk.Label(search_frame, bg="#F9FBF2", text="Power Supply").grid(sticky="W", row=6, column=5)
    # Power Supply Options
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "Battery", variable = batteryval, onvalue="Battery").grid(sticky="W", row=6, column=6)
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "USB", variable = usbval, onvalue="USB").grid(sticky="W", row=6, column=7)

    tk.Label(search_frame, bg="#F9FBF2", text="   ").grid(row=7, column=0)

    # Colour
    tk.Label(search_frame, bg="#F9FBF2", text="Colour").grid(sticky="W", row=8, column=0)
    # Colour Options
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "White", variable = whiteval, onvalue="White").grid(sticky="W", row=8, column=1)
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "Black", variable = blackval, onvalue="Black").grid(sticky="W", row=8, column=2)
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "Blue", variable = blueval, onvalue="Blue").grid(sticky="W", row=8, column=3)
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "Yellow", variable = yellowval, onvalue="Yellow").grid(sticky="W", row=9, column=1)
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "Green", variable = greenval, onvalue="Green").grid(sticky="W", row=9, column=2)

    # Production Year
    tk.Label(search_frame, bg="#F9FBF2", text="Production Year").grid(sticky="W", row=8, column=5)
    # Production Year Options
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "2020", variable = val2020, onvalue="2020").grid(sticky="W", row=8, column=6)
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "2019", variable = val2019, onvalue="2019").grid(sticky="W", row=8, column=7)
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "2017", variable = val2017, onvalue="2017").grid(sticky="W", row=8, column=8)
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "2016", variable = val2016, onvalue="2016").grid(sticky="W", row=9, column=6)
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "2015", variable = val2015, onvalue="2015").grid(sticky="W", row=9, column=7)
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "2014", variable = val2014, onvalue="2014").grid(sticky="W", row=9, column=8)

    tk.Label(search_frame, bg="#F9FBF2", text="   ").grid(row=10, column=0)

    # Factory
    tk.Label(search_frame, bg="#F9FBF2", text="Factory").grid(sticky="W", row=11, column=0)
    # Factory Options
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "Malaysia", variable = malaysiaval, onvalue="Malaysia").grid(sticky="W", row=11, column=1)
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "China", variable = chinaval, onvalue="China").grid(sticky="W", row=11, column=2)
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "Philippines", variable = philippinesval, onvalue="Philippines").grid(sticky="W", row=11, column=3)

    # Purchase Status
    tk.Label(search_frame, bg="#F9FBF2", text="Purchase Status").grid(sticky="W", row=11, column=5)
    # Purchase Status Options
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "Sold", variable = soldval, onvalue="Sold").grid(sticky="W", row=11, column=6)
    tk.Checkbutton(search_frame, bg="#F9FBF2", text = "Unsold", variable = unsoldval, onvalue="Unsold").grid(sticky="W", row=11, column=7)
  
  # Simple Search Title
  tk.Label(search_frame, bg="#F9FBF2", text="Simple Search").grid(sticky="W", row=0, column=0)
  
  # Model
  tk.Label(search_frame, bg="#F9FBF2", text="Model").grid(sticky="W", row=2, column=0)
  # Model Options
  tk.Checkbutton(search_frame, bg="#F9FBF2", text = "Light1", variable = light1val, onvalue="Light1").grid(row=2, column=1)
  tk.Checkbutton(search_frame, bg="#F9FBF2", text = "Light2", variable = light2val, onvalue="Light2").grid(row=2, column=2)
  tk.Checkbutton(search_frame, bg="#F9FBF2", text = "Safe1", variable = safe1val, onvalue="Safe1").grid(row=2, column=3)
  tk.Checkbutton(search_frame, bg="#F9FBF2", text = "Safe2", variable = safe2val, onvalue="Safe2").grid(row=2, column=4)
  tk.Checkbutton(search_frame, bg="#F9FBF2", text = "Smart Home1", variable = smarthome1val, onvalue="SmartHome1").grid(sticky="W", row=2, column=5)

  # Advance Search Options Button 
  tk.Button(search_frame, bg='#fbf2fa', text="Advance Search", command=onClick).grid(sticky="W", row=2, column=8)
  # Search Button
  tk.Button(search_frame, bg='#fbf2fa', text="Search", command=onSearch).grid(sticky="W", row=15, column=8)

  # Styling Spaces
  tk.Label(search_frame, text="   ", bg="#F9FBF2").grid(row=1, column=0)
  tk.Label(search_frame, text="   ", bg="#F9FBF2").grid(row=14, column=0)
  tk.Label(search_frame, text="   ", bg="#F9FBF2").grid(row=1, column=7)

  # Search 2 Frame: Search Item by Item ID
  # Text variable
  chosenItemId = tk.StringVar()

  # Find Item
  def findAndDisplayItem():
   
    # CALL BACKEND -------------------------- 
    itemDetails = Connection().findItem(chosenItemId.get())
    print(itemDetails)

    # DUMMY DATA for above method
    # itemDetails = {"ItemID":"1001", "Model": "Lights1", "Category": "Lights", "Price": "$50", "Cost": "$20", "Color":"White", "Factory":"Malaysia", "PowerSupply":"Battery", "ProductionYear":"2014", "PurchaseStatus": "Unsold", "Warranty": "12 Months"}

    if bool(itemDetails):
      itemDetails = itemDetails[0]
      # Display Data
      tk.Label(search2_frame, text=" ", bg="#F9FBF2").grid(row=3)
    
      tk.Label(search2_frame, bg="#F9FBF2", text="Item ID: " + itemDetails.get('ItemID')).grid(row=4, column=0, sticky="W")
      tk.Label(search2_frame, bg="#F9FBF2", text="Model: " + itemDetails.get('Model')).grid(row=5, column=0, sticky="W")
      tk.Label(search2_frame, bg="#F9FBF2", text="Category: " + itemDetails.get('Category')).grid(row=6, column=0, sticky="W")

      tk.Label(search2_frame, bg="#F9FBF2", text="Color: " + itemDetails.get('Color')).grid(row=4, column=1, sticky="W")
      tk.Label(search2_frame, bg="#F9FBF2", text="Factory: " + itemDetails.get('Factory')).grid(row=5, column=1, sticky="W")
      tk.Label(search2_frame, bg="#F9FBF2", text="Power Supply: " + itemDetails.get('PowerSupply')).grid(row=6, column=1, sticky="W")
      tk.Label(search2_frame, bg="#F9FBF2", text="Production Year: " + itemDetails.get('ProductionYear')).grid(row=7, column=1, sticky="W")

      tk.Label(search2_frame, text="          ", bg="#F9FBF2").grid(column=2)
      tk.Label(search2_frame, bg="#F9FBF2", text="Price: $" + str(itemDetails.get('Price'))).grid(row=4, column=3, sticky="W")
      tk.Label(search2_frame, bg="#F9FBF2", text="Service Cost: $" + str(itemDetails.get('Cost'))).grid(row=5, column=3, sticky="W")
      tk.Label(search2_frame, bg="#F9FBF2", text="Warranty: " + str(itemDetails.get('Warranty')) + " Months").grid(row=6, column=3, sticky="W")
      tk.Label(search2_frame, bg="#F9FBF2", text="Purchase Status: " + itemDetails.get('PurchaseStatus')).grid(row=7, column=3, sticky="W")
    else:
      tk.messagebox.showerror("Error", "Wrong Item ID / No Such Item ID")

    #  #---CODE FOR SCROLLBAR---#
    # my_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
    # my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    # my_canvas.configure(yscrollcommand=my_scrollbar.set)
    # my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
    # #----------------------#

  # Choose Item Label
  tk.Label(search2_frame, bg="#F9FBF2", text="Input the Item ID Here: ").grid(row=0, column=0, sticky="W")

  # Input Field for Item ID 
  tk.Entry(search2_frame, text = "itemId", width=10, textvariable= chosenItemId).grid(row=0, column=1, sticky="W")
  
  # Purchase Button
  tk.Button(search2_frame, bg='#fbf2fa', height=1, width=10, text="Search Item", command=findAndDisplayItem).grid(row=2, column=0, sticky="W")

  tk.Label(search2_frame, bg="#F9FBF2", text=" ").grid(row=1)

  # Return to Customer Menu
  def redirectToMenu():
    window.destroy()
    from view.Admin.AdminMenu import adminMenu
    adminMenu()

  # Return to Customer Menu Button
  tk.Button(search_frame, bg='#fbf2fa', text="Return to Menu", command = redirectToMenu).grid(row=0, column=8)
  
  window.mainloop() 