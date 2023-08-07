# High Level Pipeline
import torch 
from transformers import pipeline 

pipe = pipeline("text-generation",model="distilgpt2")


#Direct Model Load 
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer= AutoTokenizer.from_pretrained("distilgpt2")
model=AutoModelForCausalLM.from_pretrained("distilgpt2")

inputs = tokenizer("Hello my dog is cute", return_tensors="pt")


import requests

API_URL = "https://api-inference.huggingface.co/models/distilgpt2"
API_TOKEN="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"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Can you please let us know more details about your ",
})
