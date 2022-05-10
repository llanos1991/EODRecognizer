from tkinter import *
from PIL import Image
from PIL import ImageTk
import cv2
import imutils

'''
import cv2

#print("Before URL")
cap = cv2.VideoCapture('rtsp://admin:[email protected]/H264?ch=1&subtype=0')
#print("After URL")

while True:

    #print('About to start the Read command')
    ret, frame = cap.read()
    #print('About to show frame of Video.')
    cv2.imshow("Capturing",frame)
    #print('Running..')

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows(

'''


def iniciar():
    global cap
    #cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap = cv2.VideoCapture('rtsp://admin:raptor2021@192.168.1.66:554/1')
 #   cap = cv2.VideoCapture('http://admin:raptor2021@192.168.1.66:8080')
    visualizar()
    
def visualizar():
    global cap
    if cap is not None:
        ret, frame = cap.read()
        if ret == True:
            frame = imutils.resize(frame, width=640)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)

            lblVideo.configure(image=img)
            lblVideo.image = img
            lblVideo.after(10, visualizar)

        else:
            lblVideo.image = ""
            cap.release()

def finalizar():
    global cap
    cap.release()
    
cap = None
root = Tk()

btnIniciar = Button(root, text="Iniciar", width=45, command=iniciar)
btnIniciar.grid(column=0, row=0, padx=5, pady=5)

btnFinalizar = Button(root, text="Finalizar", width=45, command=finalizar)
btnFinalizar.grid(column=1, row=0, padx=5, pady=5)

lblVideo = Label(root)
lblVideo.grid(column=0, row=1, columnspan=2)

root.mainloop()

##https://omes-va.com/tkinter-opencv-video/
