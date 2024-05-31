import pandas as pd
s=pd.Series([10, 20, 30, 40, 50,60])
data = {'Name': ['Alice', 'bob', 'charlie', 'Utkan'],
'Age': [25, 30, 22, 40]}
df = pd.DataFrame(data)

Age = df ['Age']
above_25 = df[df['Age'] > 30]

sorted_df = df.sort_values('Age')
print(sorted_df)
