#!/usr/bin/python
def getSingleNumber(number, positionFromRight):
    baseNumber = 10 ** positionFromRight
    if positionFromRight == 1:
        return number % baseNumber
    else:
        modNumber = number % baseNumber
        baseNumber = 10 ** (positionFromRight - 1)
        return int(modNumber / baseNumber)

def countsort(numberList, offset):

    counterList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    shouldEnd = True

    for number in numberList:
        singleNumber = getSingleNumber(number, offset)
        if singleNumber != 0:
            shouldEnd = False
        counterList[singleNumber] += 1

    if shouldEnd and offset != 1:
        return False

    for index in range(0, 10):
        if index == 0:
            continue
        counterList[index] = counterList[index-1] + counterList[index]

    resultList = numberList
    for number in numberList[::-1]:
        singleNumber = getSingleNumber(number, offset)
        position = counterList[singleNumber]
        position = position - 1
        resultList[position] = number
        counterList[singleNumber] = position

    return resultList

def basesort(numberList):

    offset = 0

    while True:
        offset = offset + 1
        result = countsort(numberList, offset)

        if not result:
            break
        else:
            numberList = result

    return numberList

data = [11231230,312341234120,223412340,123412342333550,624512423460,1435670,4676598660,465760,57880,9765670, 79235879245890]
print basesort(data)

