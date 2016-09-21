#!/usr/bin/python

def quicksort(A,l,r):
    if (r - l < 1):
        return
    if len(A) > 2:
        n = r
        mid = (n-1)//2
        i = -1
        j = 0
        pivot = A[r-1]
        print A

        print ("\n ")
        while (j < n-1):
            if (A[j] <= pivot):
                print A
                print("\n")
                print('enter swap')
                print ('current elm is : ', A[j])
                print('want to swap with: ', A[i + 1])
                print('Pivot is : ', pivot)
                print ("\n ")
                A[i+1],A[j] = A[j], A[i+1]

                i = i + 1
                j = j + 1
            else:
                j = j + 1

        A[i+1],A[j] = A[j], A[i+1]
        print("\n")
        print ('final J: ',j)
        print('final i: ', i)
        quicksort(A, l, mid-1)
        quicksort(A, mid+1, r-1)
    return A



A = [3,7,1,2,6,4]
B = [1, 4, 2, 3, 15, 5]
print quicksort(B, 0, len(A))
