#kullanıcıdan alınan bir metnın ıcınde kac tane a harfının kac kez gectıgını bulan pyton kodu yaz

metin = input("Lütfen bir metin girin: ")
sayac = 0

for harf in metin:
    if harf == 'a':
        sayac +=1
print("'a' harfi {} kez geçiyor.".format(sayac))