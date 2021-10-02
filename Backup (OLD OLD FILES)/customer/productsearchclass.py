import tkinter as tk
from tkinter import ttk

class ProductSearch():
  def __init__(self, master):
        self.master = master
        #title
        master.title("Product Search")

        def check():
          self.dict = {
          "model": [],
          "category": []
          }
          print("Before", self.dict)
          for options in self.modelOptions:
            if options.get() != "0":
              arr = self.dict.get("model")
              arr.append(options.get())
              self.dict["model"] = arr
          # for options in self.categoryOptions:
          #   if options.get("variable").get():
          #     dict["category"] = dict["category"].get().append(options.get("text")) 
          print("After", self.dict)
        
        tk.Button(master,text="test",command=check).grid(row=2,column=1)

        self.light1val, self.light2val, self.safe1val, self.safe2val, self.smarthome1val = (tk.StringVar() for i in range(5))

        self.modelOptions = [
          self.light1val,
          self.light2val,
          self.safe1val,
          self.safe2val,
          self.smarthome1val
        ]   

        for items in self.modelOptions:
          items.set("0")

        #simple search
        self.simple_search = tk.Label(master, text="Simple Search").grid(row=0, column=0)
        #simple search by model
        self.model = tk.Label(master, text="Model:").grid(row=1, column=0)
        #the different model options 
        self.light1 = tk.Checkbutton(master, text = "Light1", variable = self.light1val, onvalue="Light1", offvalue="0").grid(row=1, column=1)
        self.light2 = tk.Checkbutton(master, text = "Light2", variable = self.light2val, onvalue="Light2", offvalue="0").grid(row=1, column=2)
        self.safe1 = tk.Checkbutton(master, text = "Safe1", variable = self.safe1val, onvalue="Safe1", offvalue="0").grid(row=1, column=3)
        self.safe2 = tk.Checkbutton(master, text = "Safe2", variable = self.safe2val, onvalue="Safe2", offvalue="0").grid(row=1, column=4)
        self.smarthome1 = tk.Checkbutton(master, text = "Smart Home1", variable = self.smarthome1val, onvalue="SmartHome1", offvalue="0").grid(row=1, column=5)
        #advance search 
        self.advance = tk.Button(master, text = "Advance Search", command= self.onClick).grid(row=2, column=7)


  def onClick(self): 
      master = self.master

      self.lightsval, self.locksval = (tk.BooleanVar() for i in range(2))

      self.categoryOptions = [
        self.lightsval,
        self.locksval
      ]
    #category
      self.category = tk.Label(master, text="Category").grid(row=3, column=0)
      #the different category options 
      self.lights = tk.Checkbutton(master, text = "Lights", variable = self.lightsval).grid(row=3, column=1)
      self.locks = tk.Checkbutton(master, text = "Locks", variable = self.locksval).grid(row=3, column=2)
      #factory
      self.factory = tk.Label(master, text="Factory").grid(row=3, column=4)
      #different factory
      self.safe1 = tk.Checkbutton(master, text = "Safe1", variable = tk.StringVar()).grid(row=3, column=5)
      self.safe2 = tk.Checkbutton(master, text = "Safe2", variable = tk.StringVar()).grid(row=3, column=6)

        
        
