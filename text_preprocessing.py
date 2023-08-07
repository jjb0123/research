import pandas as pd

df = pd.read_csv('mergeddataset.csv', on_bad_lines='skip')


# Check Datasets have merged 
# print(df.to_string())