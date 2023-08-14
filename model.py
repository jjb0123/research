# # High Level Pipeline
# import torch 
# from transformers import pipeline 
import pandas as pd
import creds
import csv 



import requests

API_URL = "https://api-inference.huggingface.co/models/distilgpt2"
headers = {"Authorization": f"Bearer {creds.API_KEY_DGPT2}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

	
# Don't expect conversation

output_array=[]
with open('horizontallyappended.csv', 'r') as file:
	csvreader=csv.reader(file)
	for line in file:
		output=query({
			"inputs": 'Tell me how the knight moves in Chess',
			# f"inputs: Here is a review and a sentiment score. Finish the sentence for me: {line}"
		 })
		output_array.append(output)

pd.DataFrame(output_array).to_csv('ssdata1.csv')


# output = query({
# 	"inputs": "Tell me how the knight moves in chess",
# })

# print(output)




#Instead of asking questions, prompt in a way that you want it to complete the rest of the sentence. 
# Try to take the beginning of a review for example, or take the skeleton of a review 
# To prompt a new review, give a data enrichment eg. "This is a 5 star review. Food was amazing"



# Don't focus on the perceivable quality of output 

# Come up with an automated metric to see how well the model is doing. 

# Start with DistilGPT2. Doesn't have to be the only model we use. Almost infinite room for expansion

# Need a different model for sentiment classification. Generating a text subject to a constraint 

# Talk to Zach about Fine-Tuning DistilGPT2 