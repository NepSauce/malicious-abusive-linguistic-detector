from collections import Counter

class Vocabulary:
    def __init__(self):
        self.word_index = {}
        self.index_word = {}
        self.word_counts = Counter()
        self.vocab_size = 0
        self.PAD_TOKEN = "<PAD>"
        self.UNK_TOKEN = "<UNK>"
        self.add_special_tokens(self.PAD_TOKEN)
        self.add_special_tokens(self.UNK_TOKEN)

    def add_special_tokens(self, token):
        idx = self.vocab_size
        self.word_index[token] = idx
        self.index_word[idx] = token
        self.vocab_size += 1

    def build_vocab(self, tokenized_sentences):
        for sentences in tokenized_sentences:
            self.word_counts.update(sentences)

        for word in self.word_counts:
            idx = self.vocab_size
            self.word_index[word] = idx
            self.index_word[idx] = word
            self.vocab_size += 1
        
        return self.word_index, self.index_word

    def encode(self, tokens):
        encoded = []

        for token in tokens:
            index = self.word_index.get(token, self.word_index[self.UNK_TOKEN])
            encoded.append(index)
            
        return encoded
