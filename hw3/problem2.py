#!/usr/bin/python

B = [1, 4, 2, 3, 15, 5]

def sort(A,left,right):
    #done for us
    return




def SortInPlace(A, k):
    i = 0
    for i in range(len(A)):
        if (i+k) > len(A):
            return
        else:
            sort(A,i,i+k)
    return



print(sort(B,0, len(B)))
