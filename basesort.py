#!/usr/bin/python
def getSingleNumber(number, positionFromRight):
    baseNumber = 10 ** positionFromRight
    if positionFromRight == 1:
        return number % baseNumber
    else:
        modNumber = number % baseNumber
        baseNumber = 10 ** (positionFromRight - 1)
        return int(modNumber / baseNumber)

def countsort(numberList):
    counterList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for number in numberList:
        counterList[number] += 1

    counter = 0

    for number in counterList:
        numberIndex = counterList.index(number)
        if numberIndex == 0:
            counter = number
        else:
            if number == 0:
                continue
            else:
                counter += number
                counterList[numberIndex] = counter

    print counterList

    numberList.reverse()
    resultNumber = []

    for number in numberList:
        counterList[number] -= 1
        index = counterList[number]
        resultNumber.insert(index, number)

    return resultNumber

data = [2,1,4,3]
print countsort(data)

