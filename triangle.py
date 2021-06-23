edges = input()
edges = edges.split(" ")
a = float(edges[0])
b = float(edges[1])
c = float(edges[2])

if (a + b) > c and (a + c) > b and (b + c) > a and a != 0 and b != 0 and c != 0:
    if a == b and a == c:
        print("Triangulo equilatero")
    elif a == b or a == c or b == c:
        print("Triangulo isosceles")
    else:
        print("Triangulo escaleno")
else:
    print("Medidas nao formam um triangulo")
