import pandas as pd
data ={'adı':['mehmet','hasan','kadir','murat'],
'yas':[100,100,100,100],
'sehir':['mugla','aydın','ankara','istanbul']}
df=pd.DataFrame(data)
df.sort_values("yas", ascending=False,inplace=True)
print(df)
