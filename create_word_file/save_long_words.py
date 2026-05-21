# Read words from one file and save long words into another file

with open("long_words.txt", "w") as f1:
    with open("words.txt", "r") as f:
        for line in f:
            if len(line.strip()) > 5:
                f1.write(line)
