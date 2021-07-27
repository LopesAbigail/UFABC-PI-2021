def setStringOnlyAlphaCharacters(myString, seperator=''):
    return seperator.join(e for e in myString if e.isalnum()).lower()


def encodeNucleotide(nucleotide):
    if nucleotide == 'a':
        return 't'

    if nucleotide == 't':
        return 'a'

    if nucleotide == 'c':
        return 'g'

    if nucleotide == 'g':
        return 'c'


def listToString(myList):
    myString = ''

    for element in myList:
        myString += element

    return myString


dnaInfos = input()

dnaSequencesNumber = int(setStringOnlyAlphaCharacters(dnaInfos))
dnasReceivedList = []
dnaEncoded = ''

for sequence in range(0, dnaSequencesNumber):
    dnaReceived = input()
    dnaReceived = setStringOnlyAlphaCharacters(dnaReceived)
    dnasReceivedList.append(dnaReceived)

nucleotidesAmount = str(len(listToString(dnasReceivedList)))
print('> '+nucleotidesAmount)

for received in dnasReceivedList:
    dnaEncoded = ''
    for nucleotide in received:

        dnaEncoded += encodeNucleotide(nucleotide)

    print(dnaEncoded)
