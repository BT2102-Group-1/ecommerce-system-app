import tkinter as tk

def adminProductCatalogue():

  window = tk.Tk()
  window.title("Admin - Product Catalogue")
  window.geometry("500x500")

 #add frame
  frame = tk.LabelFrame(window, text="Product Catalogue", padx=20, pady=20)


  #print welcome message just to show it renders
  tk.Label(frame, text = "Product Catalogue").pack()

  # Redirect to Initialise Database
  def redirectToMenu():
    window.destroy()
    from Admin.AdminMenu import adminMenu
    adminMenu()

  tk.Button(frame, text="Return to Menu", command = redirectToMenu).pack(pady = 5)
  frame.pack()

  window.mainloop()