import pandas as pd 
df=pd.read_csv("https://apsidat.com/ornekdata.csv")
print("Average monthly income of Ankara residents:", df[(df["sehir"]=="Ankara")]["aylik_gelir"].mean())
