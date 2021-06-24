import math

first_number = float(input())
second_number = float(input())
third_number = float(input())
fourth_number = float(input())

count_numbers = 4

mean = 0
variance = 0
standard_deviation = 0

mean = (first_number + second_number +
        third_number + fourth_number) / count_numbers
variance = ((first_number - mean) ** 2 + (second_number - mean) ** 2 +
            (third_number - mean) ** 2 + (fourth_number - mean) ** 2) / (count_numbers - 1)
standard_deviation = math.sqrt(variance)

print('media = %.2f' % (mean))
print('variancia = %.2f' % (variance))
print('desvio = %.2f' % (standard_deviation))
