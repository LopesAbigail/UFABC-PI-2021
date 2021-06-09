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

if operacao == "SUM":
    a = float(input())
    b = float(input())
    soma(a, b)
elif operacao == "DIF":
    a = float(input())
    b = float(input())
    subtracao(a, b)
elif operacao == "MULT":
    a = float(input())
    b = float(input())
    multiplicacao(a, b)
elif operacao == "DIV":
    a = float(input())
    b = float(input())
    divisao(a, b)
elif operacao == "POT":
    a = float(input())
    b = float(input())
    potencializacao(a, b)
elif operacao == "RAIZ":
    a = float(input())
    raizQuadrada(a)
elif operacao == "LOG10":
    a = float(input())
    log10(a)
