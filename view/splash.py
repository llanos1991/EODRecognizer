from statistics import mode
from tkinter import *
from tkinter import ttk
from turtle import color
from PIL import ImageTk, Image
from linkButton import *
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
  user = StringVar()
  #variable contraseña
  password = StringVar()
  #crear path de imagen
  path = '../image/2919600.png'
  #redimencionar la imagen
  openImage=Image.open(path).resize((150,150))
  img = ImageTk.PhotoImage(openImage)
  lblImagen = Label(root,image=img)  
  lblImagen.place(x=325,y=30)
  lblImagen.configure(image=img)
  lblImagen.image = img

    
  user_label=Label(root,text="user :",fg="white",bg=cl,font=("AlternateGothic2 BT",15)).place(x=250,y=250)
  password_label=Label(root,text="password :", fg="white", bg=cl,font=("AlternateGothic2 BT",15)).place(x=250,y= 300)

  #noregister_label=Label(root,text="register now..¡", fg="white", bg=cl,font=("AlternateGothic2 BT",9,"italic")).place(x=560,y= 340)
  '''
  def show_info(ev):
    newWindow = tkinter.Toplevel(ventana)
ventana = tkinter.Tk()
etiqueta = tkinter.Label(ventana, text='Ejemplo')
etiqueta.pack()
etiqueta.bind('<Button-1>', show_info)
ventana.mainloop()
  '''
  
  
  #entry text
  user_entry = Entry(root,textvariable=user).place(x=400,y=250)
  password_entry = Entry(root,textvariable=password,show="*").place(x=400,y=300)
  #button
  link = Linkbutton(root,text="Register now ..!",command=Linkbutton.link_clicked).place(x=560, y=340)
  #link.place(width=300, height=200)
  
  button_sigint= Button(root,text="    sigint    ",fg="black",bg="silver",font=("AlternateGothic2 BT",15)).place(x=535,y=400)
  button_register= Button(root,text="    exit   ",fg="black",bg="silver",font=("AlternateGothic2 BT",15),command=root.quit).place(x=150,y=400)

  root.configure(background=cl)
splash.after(7000,login)
mainloop()