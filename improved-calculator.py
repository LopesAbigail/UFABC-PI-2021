import math
import fileinput


def soma(numero1, numero2):
    print("%.2f" % (numero1 + numero2))


def subtracao(numero1, numero2):
    print("%.2f" % (numero1 - numero2))


def multiplicacao(numero1, numero2):
    print("%.2f" % (numero1 * numero2))


def divisao(numero1, numero2):
    print("%.2f" % (numero1 / numero2))


def potencializacao(numero1, numero2):
    print("%.2f" % (numero1 ** numero2))


def raizQuadrada(numero):
    print("%.2f" % (math.sqrt(numero)))


def log10(numero):
    print("%.2f" % (math.log10(numero)))


for line in fileinput.input():
    operacao = line.replace("\n", "").split(" ")

    if operacao[0] == "SUM":
        a = float(operacao[1])
        b = float(operacao[2])
        soma(a, b)
    elif operacao[0] == "DIF":
        a = float(operacao[1])
        b = float(operacao[2])
        subtracao(a, b)
    elif operacao[0] == "MULT":
        a = float(operacao[1])
        b = float(operacao[2])
        multiplicacao(a, b)
    elif operacao[0] == "DIV":
        if(float(operacao[2]) != 0):
            a = float(operacao[1])
            b = float(operacao[2])
            divisao(a, b)
        else:
            print("Operacao Invalida")
    elif operacao[0] == "POT":
        a = float(operacao[1])
        b = float(operacao[2])
        potencializacao(a, b)
    elif operacao[0] == "RAIZ":
        a = float(operacao[1])
        raizQuadrada(a)
    elif operacao[0] == "LOG10":
        a = float(operacao[1])
        log10(a)
    else:
        print("Operacao Invalida")
