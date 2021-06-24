import fileinput


def ehPrimo(num):
    aux = num
    numDivisores = 0

    while (0 < aux and aux <= num):
        if(num % aux == 0):
            numDivisores = numDivisores + 1
        aux = aux - 1

    if (numDivisores == 2):
        return True
    else:
        return False


for line in fileinput.input():
    intervalo = line.strip().split(" ")
    for numero in range(int(intervalo[0]), int(intervalo[1])+1):
        if ehPrimo(numero):
            print(numero)
