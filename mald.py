from preprocessing.tokenizer import Tokenizer
from utils.vocabulary import Vocabulary

text = "Hello, World! This is a   !!!!test."
tokens = Tokenizer().tokenize(text)
index, words = Vocabulary().build_vocab(tokens)

print(index)
print(words)


