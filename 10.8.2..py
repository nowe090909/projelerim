a=[1,2,3,4,5,6,7,8]
print("Listenin Soldan Başlanarak Dilimlenmesi",a)
for i in range(0,len(a)+1):
print("<",a[0:i], ">",sep="")
print("----------------------------------")
print("",a)
for i in range(0,len(a)+1):
print("<",a[i:len(a)+1], ">",sep="")