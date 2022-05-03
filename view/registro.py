from tkinter import *
import tkinter as tk

class Ventana:
    cl="#603C78"
    
    def __init__(self,root):
        self.inicializar_gui(root)
    
    def inicializar_gui(self,root):
        width = 800
        height = 500
        screenWidth = root.winfo_screenwidth()  # Obtenga el ancho del área de visualización
        screenHeight = root.winfo_screenheight()
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        root.title("SIDE REGISTRO")
        root.geometry("%dx%d+%d+%d" % (width,height, left, top))
        root.configure(background=Ventana.cl)
        
def main():
    app=Tk()
    app1=Ventana(app)
    app=mainloop()
    
if __name__ == '__main__':
    main()

'''
import tkinter as tk
import subprocess
from tkinter import PhotoImage
class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.inicializar_gui()

    def inicializar_gui(self):
        self.title("APAGAR PC")
#       self.geometry("600x200")
        self.resizable(0,0)

        frm_izquierdo=tk.Frame(self,bg="red")
    

        imagen=PhotoImage(file="avion.gif")
        lbl_imagen=tk.Label(frm_izquierdo,image=imagen)
        lbl_imagen.grid(row=0,column=1)
   #    lbl_imagen['command']=self.Apagar

        frm_izquierdo.grid(row=0,column=0)
        frm_izquierdo.config(width=520,height=320)
     def Apagar(self):
        pass

def main():
    app=Ventana()
    app.mainloop()

if __name__ == '__main__':
    main()
'''

'''
window = Tk()
colorFondo="black"

window.geometry("600x400")
window.configure(background = colorFondo)
etiqueta = Label(window,text="Registro de Usuario ",fg="white",bg="black",font=("AlternateGothic2 BT",45)).place(x=5,y=10)

nombre=StringVar()
apellido=StringVar()
usuario=StringVar()
codigo=StringVar()

etiqueta1 =Label(window,text="Nombre",fg="white",bg="black").place(x=140,y=120)
etiqueta2 =Label(window,text="Apellido",fg="white",bg="black").place(x=140,y=160)
etiqueta3 =Label(window,text="Usuario",fg="white",bg="black").place(x=140,y=200)
etiqueta4 =Label(window,text="Codigo",fg="white",bg="black").place(x=140,y=240)
eti_log_emp=Label(window,text="Dev@cpp",fg="white",bg="black",font=("Monotype Corsiva",)).place(x=500,y=360)

nombreCaja = Entry(window,textvariable=nombre).place(x=300,y=120)
apellidoCaja = Entry(window,textvariable=apellido).place(x=300,y=160)
usuarioCaja = Entry(window,textvariable=usuario).place(x=300,y=200)
codigoCaja = Entry(window,textvariable=codigo,show="*").place(x=300,y=240)

botonC= Button(window,text="Cancelar",fg="black").place(x=120,y=300)
botonA= Button(window,text=" Aceptar ",fg="black").place(x=400,y=300)
window.mainloop()
'''