#!/usr/bin/python
#Question 3 part C
def findMin(a, i):
    index =  0
    b = []
    Min = a[0]
    while (index <= i-1 ):
        if (Min > a[index]):
            b.append(a[index])
            Min = a[index]
        else:
            b.append(Min)
        index = index + 1
    return b

a2 = [5, 2, 1, 3, 6, 4]
a = [7, 3, 4, 2, 15, 11, 16, 7, 18, 9, 11, 10]
i = 4
print ("3c: Array of Minimum elms is :  ",findMin(a,i))

# array b will be created in big o of n time?
#Question 3 part D
def Maxprof(array):
    count = 0
    L = len(array)
    small = findMin(array, L)
    Mprof = array[count] - small[count]
    while (count < len(array)):
        prof = array[count] - small[count]
        if (prof > Mprof):
            Mprof = prof
        count = count + 1
    return Mprof


print("Max profit is: ", Maxprof(a))
