#[1,2,3,4,5] [3,4,5,6,7] bu iki listenin kesişimini bulan pyton programını bulan kod yaz

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

kesisim = list(set(list1) & set(list2))

print("Liste 1:", list1)
print("Liste 2:", list2)
print("Kesişim:", kesisim)
