# Read a file and print words longer than 5 characters

with open("words.txt", "r") as f:
    for line in f:
        if len(line.strip()) > 5:
            print(line.strip())