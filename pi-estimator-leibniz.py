import fileinput


def formula_leibniz_pi(n):
    pi = 0
    for contador in range(0, n):
        pi += 4 * (((-1) ** contador) / (2*contador + 1))
    return pi


for numero in fileinput.input():
    print("pi({iteracao}) = {pi: .4f}".format(
        iteracao=numero, pi=formula_leibniz_pi(int(numero))))
