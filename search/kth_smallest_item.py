#!/usr/bin/python
def exchange(numberList, aIndex, bIndex):
    tempData = numberList[aIndex]
    numberList[aIndex] = numberList[bIndex]
    numberList[bIndex] = tempData

def findItem(numberList, startIndex, stopIndex, k):
    pivot = numberList[startIndex]
    i = startIndex
    j = i + 1

    while j < stopIndex:
        if pivot > numberList[j]:
            exchange(numberList, i+1, j)
            i = i + 1
        j = j + 1

    exchange(numberList, startIndex, i)
    if i+1 == k:
        return {"status":"founded","result":numberList[i]}

    elif i+1 < k:
        return {
                "status":"not found",
                "numberList":numberList,
                "startIndex":i+1,
                "stopIndex":stopIndex
                }
    elif i+1 > k:
        return {
                "status":"not found",
                "numberList":numberList,
                "startIndex":startIndex,
                "stopIndex":i
                }


def kthSmallestItem(data, startIndex, stopIndex, k):

    if stopIndex > len(data):
        return "2"
    if k == 0:
        return "3"
    if k > len(data):
        return "4"

    result = findItem(data, startIndex, stopIndex, k)
    if result["status"] == "founded":
        return result
    else:
        return kthSmallestItem(result["numberList"], result["startIndex"], result["stopIndex"], k)


data = [5,4,6,3,7,8]
print kthSmallestItem(data, 0, len(data), 0)
data = [5,4,6,3,7,8]
print kthSmallestItem(data, 0, len(data), 1)
data = [5,4,6,3,7,8]
print kthSmallestItem(data, 0, len(data), 2)
data = [5,4,6,3,7,8]
print kthSmallestItem(data, 0, len(data), 3)
data = [5,4,6,3,7,8]
print kthSmallestItem(data, 0, len(data), 4)
data = [5,4,6,3,7,8]
print kthSmallestItem(data, 0, len(data), 5)
data = [5,4,6,3,7,8]
print kthSmallestItem(data, 0, len(data), 6)
data = [5,4,6,3,7,8]
print kthSmallestItem(data, 0, len(data), 7)

