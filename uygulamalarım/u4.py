# 1 den 100e kadar çift sayıları toplayıp ekrana yazdıran kod yaz

toplam = 0
for sayi in range(2, 101, 2):
    toplam += sayi
print("1 ile 100 arasındaki çift sayıların toplamı:", toplam)