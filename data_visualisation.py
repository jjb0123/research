import pandas as pd

files = ['sentiment_scores_2.csv', 'preprocessed.csv']

df = pd.DataFrame()
for file in files:
    data = pd.read_csv(file)
    df = pd.concat([df, data], axis=1)
df.to_csv('merged_files.csv', index=False)