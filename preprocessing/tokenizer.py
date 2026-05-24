import re

class Tokenizer:
    def __init__(self):
        pass

    def clean_text(self, text):
        cleaned_text = []

        for row in text:
            row = row.lower()
            row = re.sub(r"[^a-z0-9\s]", "", row)
            row = re.sub(r"\s+", " ", row).strip()
            row = row.strip()

            cleaned_text.append(row)

        return cleaned_text
    
    def tokenize(self, text):
        return text.split()
