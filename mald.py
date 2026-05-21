from preprocessing.preprocessor import Preprocessor


# text = "Hello, World! This is a   !!!!test."
# tokens = Tokenizer().tokenize(text)
# vocabulary = Vocabulary()
# index, words = vocabulary.build_vocab([tokens])

preprocessor = Preprocessor('text_data/mald_dataset')
print(preprocessor.preprocess())

# encoded_tokens = vocabulary.encode(tokens)

# print(tokens)
# print(index)
# print(words)
# print(encoded_tokens)

# print(vocabulary.decode(encoded_tokens))