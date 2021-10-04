import tkinter as tk

def productSearch():
  window = tk.Tk()
  window.title("Product Search")
  window.geometry("500x500") 
  
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

  for key, value in options:
    for i in value:
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

    for key, value in options:
      for i in value:
        if i.get() != "0":
          dict[key] = dict.get(key).append(i.get())
    
    print(dict) 
    # call backend function customerSearch(dict) to get items array
    items = []
    displaySearchItems(items)
  
  # Display search items
  def displaySearchItems(items):
    pass

  # Advance Search Options
  def onClick(): 
  # Category
    category = tk.Label(window, text="Category").grid(row=3, column=0)
    #the different category options 
    lights = tk.Checkbutton(window, text = "Lights", variable = lightsval, onvalue="Lights").grid(row=3, column=1)
    locks = tk.Checkbutton(window, text = "Locks", variable = locksval, onvalue="Locks").grid(row=3, column=2)
    #factory
    factory = tk.Label(window, text="Factory").grid(row=3, column=4)
    #different factory
    safe1 = tk.Checkbutton(window, text = "Safe1", variable = tk.StringVar()).grid(row=3, column=5)
    safe2 = tk.Checkbutton(window, text = "Safe2", variable = tk.StringVar()).grid(row=3, column=6)
  
  # Simple Search
  simple_search = tk.Label(window, text="Simple Search").grid(row=0, column=0)
  #simple search by model
  model = tk.Label(window, text="Model:").grid(row=1, column=0)
  #the different model options 
  light1 = tk.Checkbutton(window, text = "Light1", variable = light1val, onvalue="Light1").grid(row=1, column=1)
  light2 = tk.Checkbutton(window, text = "Light2", variable = light2val, onvalue="Light2").grid(row=1, column=2)
  safe1 = tk.Checkbutton(window, text = "Safe1", variable = safe1val, onvalue="Safe1").grid(row=1, column=3)
  safe2 = tk.Checkbutton(window, text = "Safe2", variable = safe2val, onvalue="Safe2").grid(row=1, column=4)
  smarthome1 = tk.Checkbutton(window, text = "Smart Home1", variable = smarthome1val, onvalue="SmartHome1").grid(row=1, column=5)
  #advance search 
  advance = tk.Button(window, text = "Advance Search", command= onClick).grid(row=2, column=7)


  
  
  window.mainloop() 

