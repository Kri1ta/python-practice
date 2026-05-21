# Count how many times each word appears in a text

text = "cat dog cat bird dog cat"
words = text.split()

count_dict = {}

for word in words:
    if word not in count_dict:
        count_dict[word] = 1
    else:
        count_dict[word] += 1

print(count_dict)