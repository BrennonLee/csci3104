#!/usr/bin/python

def swap (a ,i , j):
    (a[i], a[j]) = (a[j], a[i])


def lomutoThreeWayPartition (a):
 n = len (a)
 pivot = a[n -1]
 i, j = -1, 0 # todo : modify
 k = 0 # todo : modify
 for j in range (0 ,n-1):
     print("\n")
     print("current index is: ", a[j])
     print("current i val is: ", i)
     print("current k val is: ", k)
     print("current a is: ",a)
     if (a[j] < pivot ):
         swap(a, i+1,j)
         i = i + 1
         k = k + 1
     elif (a[j] == pivot ):
         swap(a,k, j)
         k = k + 1
 print("\n")
 print("for the last swap outside loop")
 print("pivot is : ",pivot)
 print("i+1 is : ", a[i+1])
 print("\n")
 swap(a, i+1, n-1)
     # todo : fill in the code for this part ..
     # todo : move the pivot element back to the correct place .
     # ...


def test(a):
    print("Input: ", a)
    lomutoThreeWayPartition(a)
    print("Output: ", a)



a = [1,6,3,5,4,9,5]
b = [3, 1, 6, 4, 2, 7, 8, 4]
c = []
test(a)
