from collections import Counter

class Vocabulary:
    def __init__(self):
        self.word_index = {}
        self.index_word = {}
        self.word_counts = Counter()
        self.vocab_size = 0

