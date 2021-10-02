from tkinter import *

class Inventory():
    def __init__(self, master):
        self.master = master
        master.title("View Inventory")

        self.inventory_frame = Frame(master, text="View Inventory", padx=50, pady=50)
        self.inventory_frame.pack(padx=10, pady=10)
