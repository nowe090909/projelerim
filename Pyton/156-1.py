# 999 girilene kadar pozitif sayıların toplamını alan program 
# <girilen negatifler işlenmeyevektir
toplam = 0
durum=False
while not durum:
    deger= int(input("lütfen pozitif tam sayı giriniz (çıkış için 999):"))
    if deger < 0 :
        print("negatif deger verildi. ",deger, "degeri işleme alınmadı")
        continue
    if deger != 999:
        print("eklenen deger", deger)
        toplam += deger
    else:
        durum = (deger == 999)
        print("toplam =",toplam)
