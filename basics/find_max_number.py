# Find the maximum number in a list without using max()

numbers1 = [3, 8, 1, 6, 9]

def find_max(numbers):
    maxi = numbers[0]
    for number in numbers:
        if number > maxi:
            maxi = number
    return maxi

print(find_max(numbers1))