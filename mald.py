from preprocessing.tokenizer import Tokenizer

text = "Hello, World! This is a   !!!!test."
tokens = Tokenizer().tokenize(text)

print(tokens)