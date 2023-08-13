# # High Level Pipeline
# import torch 
# from transformers import pipeline 
import pandas as pd

# pipe = pipeline("text-generation",model="distilgpt2")


# #Direct Model Load 
# from transformers import AutoTokenizer, AutoModelForCausalLM

# tokenizer= AutoTokenizer.from_pretrained("distilgpt2")
# model=AutoModelForCausalLM.from_pretrained("distilgpt2")

# inputs = tokenizer("Hello my dog is cute", return_tensors="pt")


import requests

API_URL = "https://api-inference.huggingface.co/models/distilgpt2"
API_TOKEN=""
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
# Don't expect conversation
output = query({
	"inputs": "Tell me how the knight moves in chess",
})

# Sentiment classifier 
API_URL = "https://api-inference.huggingface.co/models/siebert/sentiment-roberta-large-english"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "I like you. I love you",
})



#Instead of asking questions, prompt in a way that you want it to complete the rest of the sentence. 
# Try to take the beginning of a review for example, or take the skeleton of a review 
# To prompt a new review, give a data enrichment eg. "This is a 5 star review. Food was amazing"



# Don't focus on the perceivable quality of output 

# Come up with an automated metric to see how well the model is doing. 

# Start with DistilGPT2. Doesn't have to be the only model we use. Almost infinite room for expansion

# Need a different model for sentiment classification. Generating a text subject to a constraint 

# Talk to Zach about Fine-Tuning DistilGPT2 