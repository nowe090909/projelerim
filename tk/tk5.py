from tkinter import *
class Uygulama(object):
    def __init__ (self):
        self.araclar()
    def araclar(self):
        self.etiket = Label(text="dosyayı silmek istediginizden emin misiniz")
        self.etiket.pack()
pencere = Tk()
uyg=Uygulama()
mainloop()
