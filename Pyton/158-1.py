faktoriyel=1
sayac=1
sayi=int(input("lutfen bir sayı giriniz.."))
while sayac<=sayi:
    faktoriyel*=sayac
    sayac+=1
    print(sayi,"sayisinin faktoriyeli:",faktoriyel)  