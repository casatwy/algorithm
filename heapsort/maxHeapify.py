#!/usr/bin/python
def leftChild(index):
    return 2*index

def rightChild(index):
    return 2*index+1

def parent(index):
    return round(index/2)

def exchange(numberList, aIndex, bIndex):
    tempData = numberList[aIndex]
    numberList[aIndex] = numberList[bIndex]
    numberList[bIndex] = tempData
    return numberList

def maxHeapify(numberList, index):
    leftIndex = leftChild(index)
    rightIndex = rightChild(index)
    largestIndex = 0

    if leftIndex <= numberList.count and numberList[leftIndex] > numberList[index]:
        largestIndex = leftIndex
    else:
        largestIndex = index

    if rightIndex <= numberList.count and numberList[rightIndex] > numberList[largestIndex]:
        largestIndex = rightIndex

    if largestIndex != index:
        numberList = exchange(numberList, index, largest)
        maxHeapify(numberList, largest)
    else:
        return numberList

data = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
print maxHeapify(data, 3)
