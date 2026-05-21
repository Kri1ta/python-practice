# Find and print words longer than 5 characters

text = "apple kiwi banana orange"
words = text.split()
words_list = []

for word in words:
    if len(word) > 5:
        words_list.append(word)

print(words_list)
