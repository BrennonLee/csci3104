#!/usr/bin/python
#question 3 part e
def Maxprof(a):
    i = len(a)
    index =  0
    maxprofit = 0
    Min = 10000000
    while (index <= i-1 ):
        if (Min > a[index]):
            Min = a[index]
        prof = a[index] - Min
        if (prof > maxprofit):
            maxprofit = prof
        index = index + 1
    return maxprofit

a2 = [5, 2, 1, 3, 6, 4]
a = [7, 3, 4, 2, 15, 11, 16, 7, 18, 9, 11, 10]
print(Maxprof(a))
