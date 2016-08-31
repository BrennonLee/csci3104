#!/usr/bin/python

def mergesort(a):
    array = a
    lefthalf = a
    righthalf = a
    print("Splitting ", a)
    if (len(a) > 1):
        mid = len(a)//2
        lefthalf = a[:mid]
        righthalf = a[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)
        merge(lefthalf, righthalf, array)

def merge(lefthalf, righthalf, array):
    i = 0
    j = 0
    k = 0
    while (i < len(lefthalf) and j < len(righthalf)):
        if (lefthalf[i] < righthalf[j]):
            array[k] = lefthalf[i]
            i = i + 1
        else:
            array[k] = righthalf[j]
            j = j + 1
        k = k + 1
    while (i < len(lefthalf)):
        array[k] = lefthalf[i]
        i = i + 1
        k = k + 1
    while (j < len(righthalf)):
        array[k] = righthalf[j]
        j = j + 1
        k = k + 1
    print ("Merging", array)
    return array


array = [8, 1, 16, 3, 2, 9, 4, 5];
lower = 0;
upper = len(array)
mergesort(array)
