import pandas as pd 

data = {'adı': ['mehmet', 'hasan', 'kadir', 'murat'],
        'yas': [1, 50, 80, 120],
        'sehir': ['mugla', 'aydın', 'ankara', 'istanbul']}

df = pd.DataFrame(data)

ortalama_yas = df['yas'].mean()
standart_sapma = df['yas'].std()

df['min_yas'] = df['yas'].min()
df['max_yas'] = df['yas'].max()

print("standart sapma:", standart_sapma)
print("ortalama yas:", ortalama_yas)
print("min yas:", df['min_yas'][0])
print("max yas:", df['max_yas'][0]) 
