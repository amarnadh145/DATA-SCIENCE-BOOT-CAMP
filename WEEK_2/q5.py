import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

filtered_rows = df.iloc[::20, [0, 1, 5]]  
print(filtered_rows)
