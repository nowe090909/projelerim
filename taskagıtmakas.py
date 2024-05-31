import random

def kazanan(secim1, secim2):
    if secim1 == secim2:
        return "Berabere!"
    elif (secim1 == "tas" and secim2 == "makas") or (secim1 == "kagıt" and secim2 == "tas") or (secim1 == "makas" and secim2 == "kagıt"):
        return "Sen kazandın!"
    else:
        return "Bilgisayar kazandı!"

while True:
    secim = input("tas, kagıt, makas? (Çıkmak için 'q' basın): ").lower()
    if secim == 'q':
        break
    elif secim not in ['tas', 'kagıt', 'makas']:
        print("Geçersiz seçim. Lütfen 'tas', 'kagıt' veya 'makas' seçin.")
        continue
    
    bilgisayar_secim = random.choice(['tas', 'kagıt', 'makas'])
    sonuc = kazanan(secim, bilgisayar_secim)
    
    print(f"Senin seçimin: {secim}, Bilgisayarın seçimi: {bilgisayar_secim}")
    print(sonuc)
