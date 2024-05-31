import math

# Kullanıcıdan yarıçapı al
yaricap = float(input("Dairenin yarıçapını girin: "))

# Dairenin alanını hesapla
alan = math.pi * yaricap**2

# Sonucu ekrana yazdır
print(f"Dairenin alanı: {alan}")