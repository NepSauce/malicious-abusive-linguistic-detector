import re

class Tokenizer:
    def __init__(self):
        pass

    def clean_text(self, text):
        cleaned_text = []

        for row in text:
            label = row[1]
            row = row[0].lower()
            row = re.sub(r"[^a-z0-9\s]", "", row)
            row = re.sub(r"\s+", " ", row).strip()
            row = row.strip()

            cleaned_text.append((row, label))

        return cleaned_text
    
    def tokenize(self, sequence):
        return sequence.split()
  