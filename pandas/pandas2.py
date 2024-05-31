import pandas as pd
data ={'adı':['mehmet','hasan','kadir','murat'],
'yas':[100,100,100,100],
'sehir':['mugla','aydın','ankara','istanbul']}
df=pd.DataFrame(data)
standart_sapma=df['yas'].std()
print("standart sapma:",standart_sapma)
