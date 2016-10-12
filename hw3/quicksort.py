#!/usr/bin/python


def partition(A,l,r):
    pivot = A[r]
    i = l-1
    j = l
    for j in range(l,r):
        if(A[j] <= pivot):
            i = i + 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1

def quicksort(A,l,r):
    if (l < r):
        q = partition(A,l,r)
        quicksort(A,l,q-1)
        quicksort(A,q+1,r)
    return A

# A = [3,7,1,2,6,4]
# B = [1, 4, 2, 3, 15, 5]
C = [5,18,3,4,1,18]
# D = [2,8,7,1,3,5,6,4]
print quicksort(C, 0, len(C)-1)
