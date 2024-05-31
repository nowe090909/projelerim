yükseklik=int(input("çizilecek ağacın yüksekliğini giriniz: "))
satir = 0
while satir < yükseklik:
    sayac=0
    while sayac < yükseklik - satir:
        print(end=" ")
        sayac+=1
    sayac=0
    while sayac < 2*satir + 1:
            print (end="*")
            sayac+=1
    print()
    satir+=1