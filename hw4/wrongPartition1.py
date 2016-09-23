#!/usr/bin/python

def swap(a,i,j):
    (a[i], a[j]) = (a[j], a[i])

def wrongPartition(a):
    # Implement Lomuto partition algorithm
    n = len(a)
    pivot=a[n-1] # choose pivot at the very end
    i=-1    # start with i = 0 and j = 0
    j=0
    for j in range(0,n-1):
        # Invariant: a[0] to a[i] are <= pivot, whereas
        #            a[i+1] to a[j-1] are > pivot,
        #            everything else is to be processed
	print("J is :", j )
	print("I is :", i)
	print("a is: ",a)
        if (a[j] <= pivot): #If a[j+1] is smaller than pivot
            swap(a,i+1,j)  # move the new to be processed
                             # element into the correct place
            i = i +1
    # end for loop
    if (i == -1):
        if (a[0] < pivot):
            swap(a,i+1,n-1)
    else:
        swap(a,i+1,n-1)# Final step: restore the pivot back to place

def test(a):
    print('Input',a, 'Pivot:',a[len(a) -1])
    wrongPartition(a)
    print('Output',a)


a = [6,1,3,9,4,5]
b = [1,2,3,4,5,6]
same = [5,5,5,5,5,5,5,5]
incre = [1,2,3,4,5,6]
dec = [6,5,4,3,2,1]
test(same)
