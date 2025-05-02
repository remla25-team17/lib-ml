import re

def preprocessing(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text