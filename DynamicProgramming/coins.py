#!/usr/bin/python
# -*- coding: utf-8 -*-

coins = [1, 2, 5, 10]
resultList = []

def cointCountForValue(value):
    tempResultList = []
    if len(resultList[value]) > value:
        return resultList[value]
    else:
        for index, coin in enumerate(coins):
