from statistics import mode
from tkinter import *
from tkinter import ttk
from turtle import color
from PIL import ImageTk, Image

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
labelB = Label(splash, text = "Sistema Inteligente de Deteccion de Explosivos", fg="#FFFFFF", bg=cl, font=("AlternateGothic2 BT",15)).place(x=170,y=250)
# Progress bar
progressbar = ttk.Progressbar()
progressbar.place(x=200, y=400, width=400)
progressbar.start(70)

# funcion de la ventana secundaria
def login():
    # Create object
  progressbar.stop()
  splash.destroy()
  root = Tk()
  root.title('SIDE') 
  root.geometry("%dx%d+%d+%d" % (width, height, left, top))
  #variable usuario
  user=StringVar()
  #variable contraseña
  password=StringVar()
  '''
  import Tkinter as tk
  from PIL import ImageTk, Image

  path = 'C:/xxxx/xxxx.jpg'

  root = tk.Tk()
  img = ImageTk.PhotoImage(Image.open(path))
  panel = tk.Label(root, image = img)
  panel.pack(side = "bottom", fill = "both", expand = "yes")
  root.mainloop()
  
  '''
  #labels
  user_label=Label(root,text="user :",fg="white",bg=cl,font=("AlternateGothic2 BT",15)).place(x=250,y=250)
  password_label=Label(root,text="password :", fg="white", bg=cl,font=("AlternateGothic2 BT",15)).place(x=250,y= 300)
  #entry text
  user_entry = Entry(root,textvariable=user).place(x=400,y=250)
  password_entry = Entry(root,textvariable=password,show="*").place(x=400,y=300)
  #button
  button_sigint= Button(root,text="    sigint    ",fg="black",bg="silver",font=("AlternateGothic2 BT",15)).place(x=535,y=400)
  button_register= Button(root,text="    register   ",fg="black",bg="silver",font=("AlternateGothic2 BT",15),command=root.quit).place(x=150,y=400)

  root.configure(background=cl)
splash.after(7000,login)
mainloop()