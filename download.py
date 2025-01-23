from datasets import load_dataset

# Load the cached dataset
dataset = load_dataset("openwebtext", name="plain_text", trust_remote_code=True)

# Access some data
print(dataset["train"][0])  # First example in the training split
