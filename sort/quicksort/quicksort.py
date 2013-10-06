#!/usr/bin/python

def exchange(numberList, aIndex, bIndex):
    tempData = numberList[aIndex]
    numberList[aIndex] = numberList[bIndex]
    numberList[bIndex] = tempData

def partition(numberList, startIndex, endIndex):
    pivot = numberList[startIndex]
    i = startIndex
    j = i+1
    while j <= endIndex:
        if pivot > numberList[j]:
            exchange(numberList, i+1, j)
            i=i+1
        j=j+1
    exchange(numberList, startIndex, i)
    return i

def quicksort(numberList, startIndex, endIndex):
    if startIndex < endIndex:
        middleIndex = partition(numberList, startIndex, endIndex)
        quicksort(numberList, 0, middleIndex-1)
        quicksort(numberList, middleIndex+1, endIndex)

data = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
quicksort(data, 0, len(data)-1)
print data

