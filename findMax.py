#!/usr/bin/python

def findMax(a, l, u):
    print ("splitting ", a)
    mid = int((l + u)/2)
    if ((a[mid] > a[mid + 1]) and (a[mid] > a[mid -1])):
        return a[mid]

    else:
        #lefthalf = a[l:mid]
        #righthalf = a[mid:u]
        if(a[mid] < a[mid -1]):

            return findMax(a, l, mid)
        else:

            return findMax(a, mid + 1, u)

a =  [1, 2, 5, 17, 19, 15, 12, 11, 4, 2, 1, 0]

print findMax(a, 0, len(a)-1)
