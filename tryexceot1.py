ilk_sayı   = input("İlk sayı:")
ikinci_sayı= input("İkinci sayı:")

try:
    sayı1 = int("ilk_sayı")
    sayı2 = int("İkinci_sayı")
    print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
except ValueError:
    print("Lütfen sadece sayı girin!")

expect ZeroDivisionError:
print("bir sayıyı 0 a bölemezsin")    


except ValueError:
    print("lütfen sadece sayı giriniz")