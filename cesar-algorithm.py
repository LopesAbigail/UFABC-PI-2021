import array


def codificadorCesar(deslocamento, frase):
    frase = frase.lower()
    fraseCodificada = ''

    for i in range(0, len(frase)):
        if frase[i].isalpha():
            if deslocamento < 122-ord(frase[i]):
                fraseCodificada += chr(ord(frase[i])+deslocamento)
            else:
                if ord(frase[i])+deslocamento-122 == 0:
                    codigo = 122
                else:
                    codigo = ord(frase[i])+deslocamento-122+96
                fraseCodificada += chr(codigo)
        else:
            fraseCodificada += frase[i]
    print(frase + '\n' + fraseCodificada)


def codificadorCesarRefatorado(deslocamento, frase):
    letrasAscii = array.array('i', (i for i in range(97, 123)))
    # print(letrasAscii.tolist())
    posicaoLista = 0

    frase = frase.lower()
    fraseCodificada = ''

    for j in range(0, len(frase)):
        if frase[j].isalpha():
            if deslocamento < 122 - ord(frase[j]):
                fraseCodificada += chr(ord(frase[j])+deslocamento)
            else:
                posicaoLista = letrasAscii.tolist(
                )[(ord(frase[j])+deslocamento-122)]
            fraseCodificada += chr(posicaoLista)
        else:
            fraseCodificada += frase[j]
    print(frase + '\n' + fraseCodificada)


tamanhoDeslocamento = int(input())
fraseOriginal = input()

codificadorCesar(tamanhoDeslocamento, fraseOriginal)
