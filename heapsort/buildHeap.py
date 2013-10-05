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

def maxHeapify(numberList, index):
    leftIndex = leftChild(index)
    rightIndex = rightChild(index)
    largestIndex = 0

    if leftIndex < len(numberList) and numberList[leftIndex] > numberList[index]:
        largestIndex = leftIndex
    else:
        largestIndex = index

    if rightIndex < len(numberList) and numberList[rightIndex] > numberList[largestIndex]:
        largestIndex = rightIndex

    if largestIndex != index:
        exchange(numberList, index, largestIndex)
        maxHeapify(numberList, largestIndex)

data = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
print data

dataLength = len(data)
for index in range(int(round(dataLength/2)), -1, -1):
    maxHeapify(data, index)

print data
