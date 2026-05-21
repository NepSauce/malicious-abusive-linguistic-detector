from preprocessing.tokenizer import Tokenizer
from preprocessing.vocabulary import Vocabulary

class Preprocessor:
    def __init__(self):
        self.tokenizer = Tokenizer()
        self.vocabulary = Vocabulary()

    def preprocess(self, dataset):
        