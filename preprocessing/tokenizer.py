import re

class Tokenizer:
    def __init__(self):
        pass

    def clean_text(self, text):
        for row in text:
            row = row.lower()
            row = re.sub(r"[^a-z0-9\s]", "", row)
            row = re.sub(r"\s+", " ", row).strip()
            row = row.strip()

        return text
    
    def tokenize(self, text):
        text = self.clean_text(text)
        tokens = text.split(" ")

        return tokens