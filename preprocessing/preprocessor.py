from preprocessing.tokenizer import Tokenizer
from preprocessing.vocabulary import Vocabulary
from utils.csv_reader import CSVReader

class Preprocessor:
    def __init__(self, file_path):
        self.tokenizer = Tokenizer()
        self.vocabulary = Vocabulary()
        self.csv_reader = CSVReader(file_path)
        self.file_path = file_path

    def preprocess(self):
        processed_data = []
        data = self.csv_reader.read_csv()
        clean_text = self.tokenizer.clean_text(data)

        for sequence in clean_text:
            label = sequence[1]
            tokens = self.tokenizer.tokenize(sequence[0])
            self.vocabulary.build_vocab([tokens])
            encoded_tokens = self.vocabulary.encode(tokens)

            processed_data.append((encoded_tokens, label))

        # tokens = self.tokenizer.tokenize(clean_text)
        # self.vocabulary.build_vocab(tokens)
        # encoded_tokens = [self.vocabulary.encode(token) for token in tokens]

        return processed_data
    