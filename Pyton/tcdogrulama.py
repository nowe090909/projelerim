def tcdogrula (tckimlik):
   toplam=0
   tcdogru=False
   if(len(tckimlik)!=11):
    return False
   
   for tc in tckimlik[0:10]:
    toplam+=int(tc)

   if (str(toplam)[-1:]==tckimlik[-1:]):
        tcdogru=True

   return tcdogru

cevap=tcdogrula("22222222221")
if(cevap):
  print("tc kimlik dogru")
else:
  print("tc kimlik yanliş")
