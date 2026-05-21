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
        data = self.csv_reader.read_csv()
        
        return data

    