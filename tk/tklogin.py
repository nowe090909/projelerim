import tkinter as tk
from tkinter import messagebox
import sqlite3 as sql

class Kullanici:
    def __init__(self, id, kadi, sifre):
        self.id = id
        self.kadi = kadi
        self.sifre = sifre

def login():
    kadi = entry_username.get()
    sifre = entry_password.get()

    if (len(kadi)<1):
        messagebox.showerror("Hata", "Kullaıcı adını doldurmaısınız !")
        entry_username.focus()
        return

    if (len(sifre)<1):
        messagebox.showerror("Hata", "Kullanıcı Şifresini doldurmaısınız !")
        entry_password.focus()
        return

    kullaniciarr=kullanici_bul(kadi,sifre)
    if (len(kullaniciarr)<1):
        messagebox.showerror("Hata", "Geçersiz Kullanıcı Adı veya Şifre!")
    else:
        #messagebox.showinfo("Başarılı", "Giriş Başarılı!")
        #root.iconify()
        open_main_window(kullaniciarr)

def open_main_window(kullaniciarr):
    # Ana pencere oluştur
    main_window = tk.Toplevel(root)
    main_window.title("Ana Pencere")
    main_window.attributes('-fullscreen', True)
    main_window.attributes('-toolwindow', True)
    # Ana pencere içeriği
    k=kullaniciarr[0]
    label = tk.Label(main_window, text="Kullanıc :"+k.kadi)
    label.pack(padx=20, pady=20)

def close_window():
    root.destroy()

def db_connect():
    conn = sql.connect('okul11.db')
    return conn

def kullanici_table_kontrol():
    conn=db_connect()
    cursor = conn.cursor()
    cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='kullanici'")
    if cursor.fetchone()[0] == 0:
       cursor.execute('''CREATE TABLE kullanici 
                      (id INTEGER PRIMARY KEY, 
                      kadi TEXT,
                      sifre TEXT
                      )
                      ''')
       conn.commit()
       conn.close()

def kullanici_bul(kadi,sifre):
    conn=db_connect()
    cursor=conn.cursor()
    cursor.execute("select * from kullanici where kadi='"+kadi+"' and sifre='"+sifre+"'")
    rows = cursor.fetchall()
    kullaniciarr = []  
    for row in rows:
        ogrenci = Kullanici(row[0],row[1], row[2])
        kullaniciarr.append(ogrenci)
    conn.close()
    return kullaniciarr

# Ana pencere oluştur
root = tk.Tk()
root.title("Giriş Formu")

#root.resizable(width=False,height=False)
#root.attributes('-toolwindow', True)
root.geometry("300x150")


root.configure(bg="lightblue")
# Kullanıcı adı etiketi ve giriş kutusu
label_username = tk.Label(root, text="Kullanıcı Adı:")
label_username.grid(row=0, column=0, padx=10, pady=5)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=5)
entry_username.focus()

# Şifre etiketi ve giriş kutusu
label_password = tk.Label(root, text="Şifre:")
label_password.grid(row=1, column=0, padx=10, pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=5)

# Giriş düğmesi
btn_login = tk.Button(root, text="Giriş Yap", command=login,bg="green", fg="white")
btn_login.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

btn_kapat = tk.Button(root, text="Kapat", command=close_window,bg="red", fg="white")
btn_kapat.grid(row=2, column=1, padx=20, pady=5)

kullanici_table_kontrol()
# Ekranın ortasına yerleştir

# Pencere oluşturulduktan sonra güncelle ve ortala
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Pencereyi göster
root.mainloop()

