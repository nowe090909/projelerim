form Tkinter import*
class Uygulama(object):
    def __init__(self):
        self.etiket = label(text= "mustafayı dikmek istediginizden emin misiniz?")
        self.etiket.pack
        pencere=tk()
        uyg = Uygulama
        mainloop()