import datetime 

def yashesapla(dogumtarihi):
    bugun=datetime.datetime.now()
    dogumtarihi=datetime.datetime.strptime(dogumtarihi,"%d.%m.%Y")
    fark=bugun-dogumtarihi
    return fark

def yasgoster(fark):
    yil=fark.days//365
    ay= fark.days%365//30
    gun=fark.days%365%30
    print("Yil",yil,"Ay",ay,"Gun",gun,end=" ")
    
    
print("dogum tarihinizi yaziniz")
fark=yashesapla(input())
yasgoster(fark) 