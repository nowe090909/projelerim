tr_karakter = "şçğüıiö"
parola = input("parolanız: ")
for i in parola:
    if i in tr_karakter:
        raise TypeError("Parolada türkçe karakter kullanılmaz ")
    else:
            pass 
print("parola kabul edildi")