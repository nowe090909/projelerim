kelime = input("cümle giriniz: ")
sesliharfsayisi = 0
for c in kelime:
    if c == "A" or c == "a" or c == "E" or c == "e" \
    or c == "I" or c == "1" or c == "İ" or c == "İ" \
    or c == "O" or c == "o" or c == "Ö" or c == "ö" \
    or c == "U" or c == "u" or c == "ü" or c == "ü":
        print(c, ",", sep=" ", end=" ")
        sesliharfsayisi += 1
        print("sesliharfsayisi:",sesliharfsayisi,sep=" ")