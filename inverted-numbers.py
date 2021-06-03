number = int(input())
inverted_number = ''

while (number > 0):
    current_digit = number % 10
    number = number // 10
    inverted_number += str(current_digit)

print(inverted_number)
