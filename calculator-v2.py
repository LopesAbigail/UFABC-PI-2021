import math


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
    print("%.2f" % (math.log(numero)))


operacao = input()
opcoes = operacao.split()

if opcoes[0] == 'SUM':
    a = float(opcoes[1])
    b = float(opcoes[2])
    soma(a, b)
elif opcoes[0] == "DIF":
    a = float(opcoes[1])
    b = float(opcoes[2])
    subtracao(a, b)
elif opcoes[0] == "MULT":
    a = float(opcoes[1])
    b = float(opcoes[2])
    multiplicacao(a, b)
elif opcoes[0] == "DIV":
    a = float(opcoes[1])
    b = float(opcoes[2])
    divisao(a, b)
elif opcoes[0] == "POT":
    a = float(opcoes[1])
    b = float(opcoes[2])
    potencializacao(a, b)
elif opcoes[0] == "RAIZ":
    a = float(opcoes[1])
    raizQuadrada(a)
elif opcoes[0] == "LOG10":
    a = float(opcoes[1])
    log10(a)
