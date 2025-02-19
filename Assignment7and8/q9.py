import re

def tokenizer(text):
    tokens = re.findall(r'[\w]+|[.,!?;]', text)
    return tokens
