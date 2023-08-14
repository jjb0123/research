import pandas as pd
import csv 

csv_files = ['sentiment_scores_2.csv', 'preprocessed.csv']
df_csv_concat = pd.concat([pd.read_csv(file) for file in csv_files], ignore_index=True)

print(df_csv_concat)