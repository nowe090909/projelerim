giris = 0
toplam = 0 
print ("lutfen bir sayı giriniz,negatif sayılar donguyu sonlandırır:") 
while True:
 giris = int(input())
 if giris < 0: 
    break
 toplam += giris

print("toplam=",toplam)