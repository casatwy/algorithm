#!/usr/bin/python
# -*- coding: utf-8 -*-

coins = [1, 5, 10]
resultList = [0]

def minimalCount(countList):
    minimal = countList[0]
    for count in countList:
        if count < minimal:
            minimal = count
    return minimal

def coinCountForValue(value):
    tempResultList = []

    if value == 0:
        return resultList[0]

    if len(resultList) > value:
        return resultList[value]
    else:
        for coin in coins:
            if coin < value:
                result = coinCountForValue(value-coin) + 1
                tempResultList.append(result)
            if coin == value:
                tempResultList.append(1)
                return 1

        result = minimalCount(tempResultList)
        resultList.append(result)
        return result

print coins
summary = 0
for value in range(0, 11):
    result = coinCountForValue(value)
    summary = summary + result
    print "value is %d, and coin count is %d" % (value, result)
print "summary is %d" % summary
