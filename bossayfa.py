#3 ögrenci için 3 sınav notu isteyen ve geçme notu ortalama 60 dan ve büyükse geçti 60 dan küçükse kaldı olarak hesapla, 1. sınavın ortalamaya katkısı % 25 2. sınavın da % 25 3. sınavın %50

sınav1 = float(input("1. sınav notunu girin: "))
sınav2 = float(input("2. sınav notunu girin: "))
sınav3 = float(input("3. sınav notunu girin: "))
ortalama = (sınav1 * 0.25) + (sınav2 * 0.25) + (sınav3 * 0.5)
if ortalama >= 60:
    print("Öğrenci geçti.")
else:
    print("Öğrenci kaldı.")50