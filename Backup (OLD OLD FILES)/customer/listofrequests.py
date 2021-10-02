from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class ListofRequests:
  def __init__(self, master):
        self.master = master
        master.title("List of Requests")

        self.label = Label(master, text="THIS FKING WORKS")

  # def show(self):
  #   Label(self.master, text="THIS IS WORKING")

        