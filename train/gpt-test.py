from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Load pre-trained GPT-2 and tokenizer
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# OPTIONAL: Set pad_token to eos_token to avoid errors
tokenizer.pad_token = tokenizer.eos_token
model.config.pad_token_id = tokenizer.pad_token_id

# Your prompt
prompt = "Original: I want the process to run on Mondays at Midnight.\nReworded:"

# Tokenize with attention mask
inputs = tokenizer(prompt, return_tensors="pt", padding=True)
input_ids = inputs["input_ids"]
attention_mask = inputs["attention_mask"]

# Generate text
output_ids = model.generate(
    input_ids=input_ids,
    attention_mask=attention_mask,
    max_length=100,
    num_return_sequences=1,
    do_sample=True,
    temperature=0.7,
    top_p=0.95,
    top_k=50,
    pad_token_id=tokenizer.pad_token_id,
)

# Decode and print output
generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
print(generated_text)

