from tkinter import*
gui = Tk()
gui.title("sözlük programı")
 
deg1 = StringVar()
deg1.set("ingilizce")
deg2 = StringVar()
deg2.set ("türkçe")

menu1 = OptionMenu(gui,deg1,"one","two","three")
menu1.pack (side=LEFT)
menu2=OptionMenu(gui,deg2,"bir","iki","üç")
menu2.pack(side=LEFT)
def cevir():
    print (deg1.get(),"=", deg2.get())

    Button = Button (gui, text="OK", command=cevir)
    button.pack(side=LEFFT)
gui.mainloop()