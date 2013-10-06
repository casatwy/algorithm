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

    print "largest index is %d" % largestIndex
    print "index is %d" % index

    if largestIndex != index:
        exchange(numberList, index, largestIndex)
        maxHeapify(numberList, largestIndex)

def buildHeap(numberList):
    dataLength = len(data)
    for index in range(int(round(dataLength/2)), -1, -1):
        maxHeapify(data, index)


data = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
result = []

buildHeap(data)
while len(data):
    result.append(data[0])
    exchange(data, 0, len(data)-1)
    data.remove(data[len(data)-1])
    maxHeapify(data, 0)
print result
