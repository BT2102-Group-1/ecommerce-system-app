import tkinter as tk
from tkinter import ttk

root = tk.Tk()
frame = tk.LabelFrame(root, text="Product Search", padx=20, pady=20)
frame.grid(row=0, column=0)

frame.heading = ('Product Search page')
title = tk.Label(frame, text = "Product Search")
title.grid(row=0, column=0)

simple_search = tk.Label(frame, text="Simple Search").grid(row=0, column=0)
#simple search by model
model = tk.Label(frame, text="Model:").grid(row=1, column=0)
#the different model options 
light1 = tk.Checkbutton(frame, text = "Light1", variable = tk.StringVar(), onvalue=1, offvalue=0).grid(row=1, column=1)
light2 = tk.Checkbutton(frame, text = "Light2", variable = tk.StringVar()).grid(row=1, column=2)
safe1 = tk.Checkbutton(frame, text = "Safe1", variable = tk.StringVar()).grid(row=1, column=3)
safe2 = tk.Checkbutton(frame, text = "Safe2", variable = tk.StringVar()).grid(row=1, column=4)
smarthome1 = tk.Checkbutton(frame, text = "Smart Home1", variable = tk.StringVar()).grid(row=1, column=5)
def onClick(): 
  new_frame = tk.LabelFrame(root, text="Advance Search", padx=20, pady=520).grid(row=3, column=0)
  #new_frame.heading = ('Advance Search page')
  title = tk.Label(new_frame, text = "Advance Search").grid(row=3, column=0)
  #category
  category = tk.Label(new_frame, text="Category").grid(row=3, column=0)
  #the different category options 
  lights = tk.Checkbutton(new_frame, text = "Lights", variable = tk.StringVar()).grid(row=3, column=1)
  locks = tk.Checkbutton(new_frame, text = "Locks", variable = tk.StringVar()).grid(row=3, column=2)
  #factory
  factory = tk.Label(new_frame, text="Factory").grid(row=3, column=4)
  #different factory
  safe1 = tk.Checkbutton(new_frame, text = "Safe1", variable = tk.StringVar()).grid(row=3, column=5)
  safe2 = tk.Checkbutton(new_frame, text = "Safe2", variable = tk.StringVar()).grid(row=3, column=6)
        
#advance search 
advance = tk.Button(frame, text = "Advance Search", command= onClick).grid(row=2, column=7)


        
