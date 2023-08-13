import csv
import pandas as pd
# Using SiEBert Language Sentiment Classification Model
from transformers import pipeline
sentiment_analysis = pipeline("sentiment-analysis",model="siebert/sentiment-roberta-large-english")


with open ('preprocessed.csv', 'r') as file:
    sentiment_score_array=[]
    csvreader=csv.reader(file)
    for row in csvreader:
        #print(sentiment_analysis(row))
        sentiment_score_array.append(sentiment_analysis(row))


pd.DataFrame(sentiment_score_array).to_csv('sentiment_scores_2.csv')

