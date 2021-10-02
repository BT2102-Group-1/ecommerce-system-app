from tkinter import *
#from customer.requestservice import RequestService
from customer.productsearchclass import ProductSearch

root = Tk()

#req = RequestService(root)

search = ProductSearch(root)

root.mainloop()