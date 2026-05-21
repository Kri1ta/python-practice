# Return a string with unique letters only

text1 = "banana"

def unique_letters(text):
    special = ""
    for i in text:
        if i not in special:
            special += i
    return special

print(unique_letters(text1))
