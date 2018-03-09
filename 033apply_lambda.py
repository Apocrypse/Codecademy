import pandas as pd

df = pd.read_csv('employees.csv')

get_last_name = lambda name: name.split()[-1]

df['last_name'] = df.name.apply(get_last_name)

print(df)
