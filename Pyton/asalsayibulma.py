asalsayilar=[]
for sayi in range (1,1000):
 for sayi2 in range (2,sayi):
  if sayi%sayi2==0:
   break 
 else:
   asalsayilar.append(sayi)

print (asalsayilar)