# Find the most frequent word in a text

text = "cat dog cat bird dog cat"
words = text.split()

count_dict = {}

for word in words:
    if word not in count_dict:
        count_dict[word] = 1
    else:
        count_dict[word] += 1

most_common = ""
maxi_values = None

for key in count_dict:
    if maxi_values is None or maxi_values < count_dict[key]:
        maxi_values = count_dict[key]
        most_common = key

print(most_common)