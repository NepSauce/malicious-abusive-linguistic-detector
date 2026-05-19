import re

class Tokenizer:
    def __init__(self):
        pass

    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r"[^a-z0-9\s]", "", text)
        text = re.sub(r"\s+", " ", text).strip()
        text = text.strip()

        return text
    
    def tokenize(self, text):
        text = self.clean_text(text)
        tokens = text.split(" ")

        return tokens