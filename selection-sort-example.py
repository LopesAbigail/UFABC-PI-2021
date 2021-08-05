def convertListToString(myList, seperator=''):
    return seperator.join(myList)


def selectionSort(myList):
    myListLen = len(myList)
    for i in range(myListLen):
        minValue = i
        for j in range(i+1, myListLen):
            if myList[j] < myList[minValue]:
                minValue = j

        (myList[i], myList[minValue]) = (myList[minValue], myList[i])
        print(myList)


times = int(input())

array = []

for i in range(0, times):
    number = int(input())
    array.append(number)
print(array)

selectionSort(array)
