import string

def word_frequency(sentence):
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))

    sentence = sentence.lower()

    words = sentence.split()

    frequency_dict = {}

    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    return frequency_dict