#!/usr/bin/python

def swap (a ,i , j):
    (a[i], a[j]) = (a[j], a[i])


def lomutoThreeWayPartition (a):
 n = len (a)
 pivot = a[n -1]
 i, j = -1, 0 # todo : modify
 k = -1 # todo : modify
 for j in range (0 ,n-1):
     print("\n")
     print("current element is: ", a[j])
     print("current i val is: ", i)
     print("current k val is: ", k)
     print("current a is: ",a)
     if (a[j] < pivot ):
         swap(a, i+1,j)
         if (k != i):
             swap(a,k+1,j)
         i = i + 1
         k = k + 1
     elif (a[j] == pivot ):
         swap(a,k+1, j)
         k = k + 1
 print("\n")
 print("for the last swap outside loop")
 print("pivot is : ",pivot)
 print("k+1 is : ", a[k+1], 'where k is : ',k)
 print("\n")
 if (i != k):
     swap(a,k+1, n-1)
 elif(a[0] > pivot):
    swap(a,k+1,n-1)
     # todo : fill in the code for this part ..
     # todo : move the pivot element back to the correct place .
     # ...


def test(a):
    print("Input: ", a)
    lomutoThreeWayPartition(a)
    print("Output: ", a)



a = [1,6,3,5,4,9,5]
b = [3, 1, 6, 4, 2, 7, 8, 4]
c = [20,12,17,18,9,5,4,12,8,12]
d = [1,5,5,5,5,5,5,5,5,6,7,8,4,5]
e = [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
allfive = [5,5,5,5,5,5,5,5,1]
test(a)
