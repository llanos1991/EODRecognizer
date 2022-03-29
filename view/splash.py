from tkinter import *
splash= Tk()

#tamaño automatico
splash.geometry("700x500")
splash.configure(background="#4E4B94")
splash.overrideredirect(1) #Remove border
# Set Label
splash_label = Label(splash, text="Imagen Splash", font=18)
splash_label.pack()

# main window function
def main():
    # Create object
  splash.destroy()
  root = Tk()
  root.title('SIDE') 
  root.geometry("700x500")
  root.configure(background="#4E4B94")
splash.after(7000,main)

    # Adjust size
 #   root.geometry("400x400")
   # Set Interval
  #  splash_root.after(100,main)

# Execute tkinter

mainloop()