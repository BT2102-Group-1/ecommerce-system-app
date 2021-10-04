import tkinter as tk
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
    # call backend function customerSearch(dict) to get items array
    items = []
    displaySearchItems(items)
  
  # Display search items
  def displaySearchItems(items):
    tk.Label(display_frame, text="HELLO TESTING SEARCH").grid(row=0, column=0)

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