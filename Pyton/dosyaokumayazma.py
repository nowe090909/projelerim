d1=open("deneme.txt","w",encoding="utf-8")
d1.close()

with open("deneme.txt","r+",encoding="utf-8") as dosya:
    dosya.write("rafinin anasini dino kovaliyor hd izle")
    dosya.seek(0)
    deger=dosya.read()
    print(deger)
    dosya.close()       