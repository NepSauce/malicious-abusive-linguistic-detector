def pad_sequence(sequence, max_length, pad_value=0):
    sequence = sequence[:max_length]
    padding_length = max_length - len(sequence)
    padding = [pad_value] * padding_length
    padded_sequence = sequence + padding

    return padded_sequence