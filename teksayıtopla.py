#soru= 1 den 10 e kadar olan bir liste içineki sayılardan sadece tek sayı olan bir yazilim yaz

liste = list(range(1, 11))
tek_sayilar_toplami = 0
for sayi in liste:
    if sayi % 2 != 0:
        tek_sayilar_toplami += sayi
        print("1'den 10'a kadar olan tek sayıların toplamı:", tek_sayilar_toplami)