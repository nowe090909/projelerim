from tkinter import *
from tkinter. ttk import* 
import tkinter.messagebox as msj 
gui=Tk()
gui.title ("takımını seç")
gui.geometry ('200x150')
v = StringVar()
def secim():
    msj.showinfo("favori takımın", message=v.get())

rb1 =Radiobutton(text='fetösaray', variable=v, value="oc cimbom",command=secim)
rb1.pack(anchor=W)
rb2 =Radiobutton(text='besiktasak', variable=v, value="nigga kartal",command=secim)
rb2.pack(anchor=W)
rb3 =Radiobutton(text='FENERBAHCE', variable=v, value="SARI BOĞA",command=secim)
rb3.pack(anchor=W)
rb4 =Radiobutton(text='terorist tese', variable=v, value="oclar",command=secim)
rb4.pack(anchor=W)
rb5 =Radiobutton(text='bursa', variable=v, value="tismahlar",command=secim)
rb5.pack(anchor=W)
gui.mainloop()