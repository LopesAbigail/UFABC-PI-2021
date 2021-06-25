import math
import fileinput

numbersList = []
mean = 0
sum = 0
sub = 0
variance = 0
standard_deviation = 0

for iteration in fileinput.input():

    numbersList.append(float(iteration.strip()))

for i in range(0, len(numbersList)):
    sum += numbersList[i]
mean = sum/len(numbersList)

for j in range(0, len(numbersList)):
    sub += (numbersList[j]-mean) ** 2
if len(numbersList) > 1:
    variance = sub / (len(numbersList)-1)
else:
    variance = 0

standard_deviation = math.sqrt(variance)

print("media = %.2f" % mean)
print("variancia = %.2f" % variance)
print("desvio = %.2f" % standard_deviation)
