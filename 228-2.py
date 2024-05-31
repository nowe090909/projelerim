v=[0]*100
x=int(input("Bir sayı giriniz: "))
if 0<=x<len(v):
    v[x]=1 
else:
  print("Girdiğiniz değer liste sınırları arasında değil")