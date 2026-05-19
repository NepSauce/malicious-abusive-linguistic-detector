from collections import Counter

class Vocabulary:
    def __init__(self):
        self.word_index = {}
        self.index_word = {}
        self.word_counts = Counter()
        self.vocab_size = 0

    def build_vocab(self, tokenized_sentences):
        for sentences in tokenized_sentences:
            self.word_counts.update(sentences)

        for word in self.word_counts:
            idx = self.vocab_size
            self.word_index[word] = idx
            self.index_word[idx] = word
            self.vocab_size += 1
        
        return self.word_index, self.index_word

