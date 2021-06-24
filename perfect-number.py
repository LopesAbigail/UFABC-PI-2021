import fileinput


def isPerfect(n):
    sumDividers = 0
    for i in range(1, n):
        if n % i == 0:
            sumDividers += i
    if sumDividers == n:
        return True
    else:
        return False


for iteration in fileinput.input():
    if isPerfect(int(iteration)):
        print("Perfeito")
    else:
        print("Nao perfeito")
