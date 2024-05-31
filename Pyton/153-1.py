print("yardim edin! bilgisayarim calismiyor")
cozum = False
while not cozum:
    print("bilgisayarindan herhangi bir ses geliuor mu(fans vb) ")
    secim = input("veya herhangi bir ısık yaniyormu? (y/n):")
    if secim == "n":
        secim = input("fise takili (y/n):")
        if secim == "n":
            print ("fişe takın")
        else:
            secim = input ("acma dugmesine bastınız mı (y/n):")
            if secim == "n":
                print ("açma dügmesine basın.")
            else:
                secim = input ("sigorta atmış mı?(y/n):")
                if secim =="n":
                    secim = input ("şalyer inmiş mi?(y/n): ")
                    if secim =="n":
                        print ("şalsteri kontrol edin veya yenisi ile degistirin:")
                    else:
                        print("teknik servise başvurun.")
                        cozum = True
                else:
                    print ("sigortyı kontrol edin.")
    else:
        print ("teknil servise başvurun.")
        cozum = True