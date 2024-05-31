import time
toplam = 0 # Toplam değişkeni tanımlanıp ilk değer olarak 0 veriliyor
basla = time.time() # İşlem süresinin hesaplanması için süre başlatılıyor
for n in range(1, 100001): # Toplamı alınacak sayılar için 1.000.000’e kadar döngü kuruluyor
 toplam += n
gecenZaman = time.time() - basla # Geçen zaman hesaplanıyor
print  ("Toplam:", toplam, "Geçen Süre:", gecenZaman) # Sonuçlar yazdırılıyor