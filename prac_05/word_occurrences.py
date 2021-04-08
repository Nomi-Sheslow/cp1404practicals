"""
CP1404/CP5632 Practical
Count the occurrences of words (accounting for multiple occurrences of words as well)
get user text input, put words into dictionary, and print dictionary
"""

word_to_count = {}
words = []
max_word_length = 0
text = input("Text: ").lower()
words.append(text)
words = words[0].split(" ")
words.sort()
for word in words:
    if word not in word_to_count:
        word_to_count[word] = 1
    else:
        word_to_count[word] += 1
    if len(word) > max_word_length:
        max_word_length = len(word)
for word, count in word_to_count.items():
    print("{:{}} {}".format((word + " :"), (max_word_length + 1), count))
