# pc nin 1 ile 100 arasında rasgele bir sayı secmesını saglar ve ardından kullanıcıdan bu sayıyı tahmin etmesini ister, kullanıcı her tahminde pc nin sectigi sayıya yaklasması durumunda hangi yonde tahmin yapması gerektigini bildirir, kullanıcının 5 tahmin hakkı vardır, eger kullanıcı dogru tahmin yaparsa tebrik mesaji goruntulenir eger tahmin hakkı biterse dogru cevabı gosteren pyton kodu yazınız

import random

def yon_bildir(gercek_sayi, tahmin):
    if tahmin < gercek_sayi:
        return "Daha büyük bir sayı tahmin edin."
    elif tahmin > gercek_sayi:
        return "Daha küçük bir sayı tahmin edin."
    else:
        return "Tebrikler, doğru tahmin ettiniz!"

def main():
 
    gercek_sayi = random.randint(1, 100)
    tahmin_hakki = 5

    print("PC bir sayı seçti, tahmin etmeye başlayın!")

    while tahmin_hakki > 0:
        tahmin = int(input("Tahmininiz: "))
        tahmin_hakki -= 1

        if tahmin == gercek_sayi:
            print(yon_bildir(gercek_sayi, tahmin))
            break
        else:
            print(yon_bildir(gercek_sayi, tahmin))
            if tahmin_hakki == 0:
                print(f"Tahmin hakkınız bitti! Doğru cevap: {gercek_sayi}")

if __name__ == "__main__":
    main()
