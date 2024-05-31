from tkinter import *
class Uygulama(object):
    def __init__ (self):
        self.etiket = Label(text="sabit diskiniz siliniyor")
        self.etiket.pack()
        self.baslik = pencere.title("çok onemlı uyarı")
pencere = Tk()
uyg=Uygulama()
mainloop()
