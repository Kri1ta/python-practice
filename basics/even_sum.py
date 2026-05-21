# Calculate the sum of all even numbers in a list

numbers = [4, 11, 2, 9, 6, 15]

total = 0

for number in numbers:
    if number % 2 == 0:
        total += number

print(total)