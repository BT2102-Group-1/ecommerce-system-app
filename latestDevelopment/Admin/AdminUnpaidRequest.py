import tkinter as tk

def adminServiceList():

  window = tk.Tk()
  window.title("Admin - Service List")
  window.geometry("500x500")

 #add frame
  frame = tk.LabelFrame(window, text="Service List", padx=20, pady=20)


  #print welcome message just to show it renders
  tk.Label(frame, text = "Welcome to Service List Page").pack()

  # Redirect to Initialise Database
  def redirectToMenu():
    window.destroy()
    from Admin.AdminMenu import adminMenu
    adminMenu()

  tk.Button(frame, text="Return to Menu", command = redirectToMenu).pack(pady = 5)
  frame.pack()

  window.mainloop()