def convertListToString(myList, seperator=''):
    return seperator.join(myList)


def setStringOnlyAlphaCharacters(myString, seperator=''):
    return seperator.join(e for e in myString if e.isalnum()).lower()


def setStringFormattedList(formattedString):
    return list(map(str, formattedString))


def setReversedStringList(myList):
    return myList[::-1]


def isPalindrome(originalString):
    formattedString = setStringOnlyAlphaCharacters(originalString)
    formattedStringList = setStringFormattedList(formattedString)

    reversedString = convertListToString(
        setReversedStringList(formattedStringList))

    if reversedString == formattedString:
        return True
    else:
        return False


execucao = int(input())

for i in range(0, execucao):
    myString = input()

    if isPalindrome(myString):
        print('SIM')
    else:
        print('NAO')
