#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

# Provided function 
def is_sentence(text):
    if not isinstance(text, str) or not text.strip():
        return False
    if not text[0].isupper():
        return False
    if not re.search(r'[.!?]$', text):
        return False
    if not re.search(r'\w+', text):
        return False
    return True

def get_sentence():
    # Ask user for a valid sentence
    user_sentence = input("Enter a sentence: ")
    while not is_sentence(user_sentence):
        print("This does not meet the criteria for a sentence.")
        user_sentence = input("Enter a sentence: ")
    return user_sentence

def calculate_frequencies(sentence):
    # make lowercase and remove punctuation
    sentence = sentence.lower()
    sentence = sentence.replace(".", "")
    sentence = sentence.replace("!", "")
    sentence = sentence.replace("?", "")
    sentence = sentence.replace(",", "")

    words = sentence.split()
    unique_words = []
    frequencies = []

    for word in words:
        if word in unique_words:
            i = unique_words.index(word)
            frequencies[i] += 1
        else:
            unique_words.append(word)
            frequencies.append(1)
    return unique_words, frequencies

def print_frequencies(words, frequencies):
    # print results in readable format
    print("\nWord Frequencies:")
    for i in range(len(words)):
        print(words[i] + ":", frequencies[i])

def main():
    sentence = get_sentence()
    words, freqs = calculate_frequencies(sentence)
    print_frequencies(words, freqs)

# TA said this lol
if __name__ == "__main__":
    main()

