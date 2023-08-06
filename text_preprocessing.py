# High Level Pipeline
import torch 
from transformers import pipeline 

pipe = pipeline("text-generation",model="distilgpt2")


#Direct Model Load 
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer= AutoTokenizer.from_pretrained("distilgpt2")
model=AutoModelForCausalLM.from_pretrained("distilgpt2")

inputs = tokenizer("Hello my dog is cute", return_tensors="pt")

print(inputs)