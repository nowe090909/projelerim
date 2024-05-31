# Kullanıcı seçimine göre Toplama ve Çıkarma işlemi yapan program kodları
def Yardim():
 print("Topla : Girilen iki sayıyı toplar")
 print("Fark Al : Girilen iki sayının farkını alır")
 print("Yazdır : İşlem yapılan en son değeri ekrana yazdırır")
 print("Yardım : Bu ekranı görüntüler")
 print("Çıkış : Programdan çıkışı sağlar")

def Menu():
 return input("=== (T)opla (F)ark Al (Y)azdır Y(A)rdım yuzd(e) al (Ç)ıkış ===")
# Programda kullanılmak üzere global değişken tanımlanması
sonuc = 0.0
sayi1 = 0.0
sayi2 = 0.0

def SayiGir():
 global sayi1, sayi2 # sayi1 ve sayi2 nin global değişken olarak bildirilmesi
 sayi1 = float(input("Sayı Giriniz #1:"))
 sayi2 = float(input("Sayı Giriniz #2:"))

def Yazdir():
 print(sonuc)

def Topla():
 global sonuc 
 sonuc = sayi1 + sayi2
def Farkal():
 global sonuc
sonuc = sayi1 - sayi2

def bolme():
     global sonuc
     sonuc = sayi1 / sayi2

def carpma():
  global sonuc
  sonuc = sayi1 * sayi2

def Ual():
    global sonuc
    sonuc = sayi1*sayi2/100

def main ():
 global sonuc 
durum = False
while not durum:
 seçim = Menu () #işlem yapılacak menü tasarımı 
 if seçim == "T" or seçim == "t": #toplama 
  SayiGir()
  Topla()
  Yazdir()
 elif seçim == "F" or seçim == "f": #çıkarma
  SayiGir()
  Farkal()
  Yazdir()
 elif seçim == "Y" or seçim == "y": #yazdırma
  Yazdir()
 elif seçim == "A" or seçim == "a": # yardım
  Yardim()
 elif seçim == "Ç" or seçim == "ç": #çıkış
    durum = True
 elif seçim == "M" or seçim == "m": #bölme 
   SayiGir()
   bolme()
   Yazdir()
 elif seçim == "X" or seçim == "x": #çarpma    
   SayiGir()
   carpma()
   Yazdir()
 elif seçim == "E" or seçim == "e": #çarpma    
   SayiGir()
   Ual()
   Yazdir()
    
 main()

    