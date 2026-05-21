from preprocessing.tokenizer import Tokenizer
from preprocessing.vocabulary import Vocabulary

text = "Hello, World! This is a   !!!!test."
tokens = Tokenizer().tokenize(text)
vocabulary = Vocabulary()
index, words = vocabulary.build_vocab([tokens])

encoded_tokens = vocabulary.encode(tokens)

print(tokens)
print(index)
print(words)
print(encoded_tokens)

print(vocabulary.decode(encoded_tokens))