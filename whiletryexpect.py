import random

def tahmin_oyunu():
    sayi = random.randint(1, 20)
    print("1 ile 20 arasında bir sayı tuttum. Tahmin et!")

    tahmin = None
    tahmin_hakki = 5

    while tahmin != sayi and tahmin_hakki > 0:
        try:
            tahmin = int(input("Tahmininiz: "))
        except ValueError:
            print("Geçerli bir sayı girin.")
            continue

        if tahmin < sayi:
            print("Daha yüksek bir sayı tahmin edin.")
        elif tahmin > sayi:
            print("Daha düşük bir sayı tahmin edin.")
        else:
            break

        tahmin_hakki -= 1

    if tahmin == sayi:
        print(f"Tebrikler! {sayi} sayısını doğru tahmin ettiniz.")
    else:
        print(f"Maalesef, doğru sayı {sayi} idi. Bir dahaki sefere!")

tahmin_oyunu()
