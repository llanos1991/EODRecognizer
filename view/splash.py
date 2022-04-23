from statistics import mode
from tkinter import *
from tkinter import ttk
from turtle import color

from cv2 import determinant
splash= Tk()
cl = "#603C78"
screenWidth = splash.winfo_screenwidth()  # Obtenga el ancho del área de visualización
screenHeight = splash.winfo_screenheight() 
#tamaño automatico
width = 800
height = 500
left = (screenWidth - width) / 2
top = (screenHeight - height) / 2
splash.geometry("%dx%d+%d+%d" % (width, height, left, top))
splash.configure(background=cl)
splash.overrideredirect(1) # remover bordes
# Set Label
labelA = Label(splash, text = "SIDE", fg="#FFFFFF", bg=cl, font=("AlternateGothic2 BT",45)).place(x=330,y=180)
# Progress bar
progressbar = ttk.Progressbar()
progressbar.place(x=200, y=400, width=400)
progressbar.start(70)

# funcion de la ventana secundaria
def main():
    # Create object
  progressbar.stop()
  splash.destroy()
  root = Tk()
  root.title('SIDE') 
  root.geometry("%dx%d+%d+%d" % (width, height, left, top))
  root.configure(background=cl)
splash.after(7000,main)
mainloop()