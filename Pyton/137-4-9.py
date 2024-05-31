deger = int(input("lütfen 0 yada 5 tam sayi değerlerinden birini girin:"))
if deger < 0:
 print("çok küçük")
else:
  if (deger==0):
   print("sifir")
  else:
   if deger ==1:
    print("bir")
   else:
    if deger ==5:
     print("beş")
    else:
     print("çok büyük")
print ("tamamnlandi")