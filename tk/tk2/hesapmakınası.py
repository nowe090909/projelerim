from tkinter import *
from tkinter.font import BOLD

gui = Tk()
gui.title("hesap makinesi")
#gui.configure(bg="red")  # Set background color of the GUI to red

sayi = StringVar()
sayi.set("sıfırlamak için CE ye bas)")
hesapla = Entry(gui, textvariable=sayi)
hesapla.grid(row=2, columnspan=10)

def btnBas(num):
    global snc
    snc = snc + str(num)
    sayi.set(snc)

def EsitrBas():
    global snc
    total = str(eval(snc))
    sayi.set(total)

def CEBas():
    global snc
    snc = ""
    sayi.set("")

Btn0 = Button(gui, text="0", command=lambda: btnBas(0), bg="red", fg="white")
Btn0.grid(row=6, column=2, padx=10, pady=10)
Btn1 = Button(gui, text="1", command=lambda: btnBas(1), bg="red", fg="white")
Btn1.grid(row=3, column=1, padx=10, pady=10)
Btn2 = Button(gui, text="2", command=lambda: btnBas(2), bg="red", fg="white")
Btn2.grid(row=3, column=2, padx=10, pady=10)
Btn3 = Button(gui, text="3", command=lambda: btnBas(3), bg="red", fg="white")
Btn3.grid(row=3, column=3, padx=10, pady=10)
Btn4 = Button(gui, text="4", command=lambda: btnBas(4), bg="red", fg="white")
Btn4.grid(row=4, column=1, padx=10, pady=10)
Btn5 = Button(gui, text="5", command=lambda: btnBas(5), bg="red", fg="white")
Btn5.grid(row=4, column=2, padx=10, pady=10)
Btn6 = Button(gui, text="6", command=lambda: btnBas(6), bg="red", fg="white")
Btn6.grid(row=4, column=3, padx=10, pady=10)
Btn7 = Button(gui, text="7", command=lambda: btnBas(7), bg="red", fg="white")
Btn7.grid(row=5, column=1, padx=10, pady=10)
Btn8 = Button(gui, text="8", command=lambda: btnBas(8), bg="red", fg="white")
Btn8.grid(row=5, column=2, padx=10, pady=10)
Btn9 = Button(gui, text="9", command=lambda: btnBas(9), bg="red", fg="white")
Btn9.grid(row=5, column=3, padx=10, pady=10)

btnTop = Button(gui, text="+", command=lambda: btnBas("+"), font=BOLD, bg="red", fg="white")
btnTop.grid(row=3, column=4, padx=10, pady=10)
btnEks = Button(gui, text="-", command=lambda: btnBas("-"), font=BOLD, bg="red", fg="white")
btnEks.grid(row=4, column=4, padx=10, pady=10)
btnCarp = Button(gui, text="*", command=lambda: btnBas("*"), font=BOLD, bg="red", fg="white")
btnCarp.grid(row=5, column=4, padx=10, pady=10)
btnBol = Button(gui, text="/", command=lambda: btnBas("/"), font=BOLD, bg="red", fg="white")
btnBol.grid(row=6, column=4, padx=10, pady=10)
btnEst = Button(gui, text="=", command=EsitrBas, bg="red", fg="white")
btnEst.grid(row=6, column=3, padx=10, pady=10)
btnCE = Button(gui, text="CE", command=CEBas, bg="red", fg="white")
btnCE.grid(row=6, column=1, padx=10, pady=10)

gui.mainloop()
