from tkinter import * 
gui=Tk()
gui.title("sözlük programı")

lbox1 = Listbox(gui)
lbox1.grid(row=0,column=0)

lbox2 = Listbox(gui)
lbox2.grid(roww=0,column=1)

lbox1.instert(END, "ingilizce")
eng=["one", "two", "three","four","five"]
for item in eng:
    lbox1.instert(END, item)

lbox2.instert(END,"turkce")
trk = ["bir","iki", "üç", "dört", "beş"]
for item in trk:
    lbox2.instert(END, item)
gui.mainloop()