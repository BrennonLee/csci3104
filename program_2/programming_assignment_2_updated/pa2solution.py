from __future__ import print_function
# in case you wish to use python2, but I strongly prefer that you use python3
import sys
import random

# NAME: Brennon Lee
# STUDENT ID NUMBER: 103419905
# On my honor as a University of Colorado Boulder student, I have not received any unauthorized help.
# I also realize that plagiarizing code defeats the purpose of an assignment like this and that the
# instructors and TAs have very sophisticated approaches to finding such plagiarism that can defeat
# things like renaming variables or rearranging statements.
#
# Acknowledged By: Brennon Lee

# Brennon Lee
# 103419905
# On my honor as a University of Colorado student, I acknowledge that
# I did not receive any unauthorized help for this assignment.
# I understand that systems like MOSS can easily detect code plagiarism.

sys.setrecursionlimit(30000)

def partition(A,l,r):
    pivot = A[r][0]
    i = l-1
    j = l
    for j in range(l,r):
        if(A[j][0] <= pivot):
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

def free_time_intervals(interval_lst, T):
    if (len(interval_lst)-1 < 0):
        return

    # sorted_list = quicksort(interval_lst,0, len(interval_lst)-1)
    sorted_list = sorted(interval_lst)
    # print ("sorted list is: ",sorted_list)
    # print('\n')
    b = []
    latest = 0

    for i in range(len(sorted_list)):
        if (latest > T):
            return b
        if (sorted_list[i][0] > T) and (sorted_list[i][0] > latest):
            b.append((latest, T))
        elif (sorted_list[i][0] > latest):
            b.append((latest, sorted_list[i][0]))
        latest = max(latest, sorted_list[i][1])
        # print ("Latest is now: ", latest)
    if latest < T:
        b.append((latest,T))
    # print(b)
    return b

def max_logged_in(interval_lst,T):
    if (len(interval_lst)-1 < 0):
        return

    b = []
    count = 0
    Max = 0
    minTime = T

    for i in range(len(interval_lst)):
        # print(b)
        b.append((interval_lst[i][0], 1))
        b.append((interval_lst[i][1], -1))

    # sorted_b = quicksort(b,0,len(b)-1)
    sorted_b = sorted(b)
    # print (sorted_b)
    for i in range(len(sorted_b)):
        # print("current count: ",count, "Current count + sorted_b: ", sorted_b[i])
        count = count + sorted_b[i][1]
        # print("max is: ", Max, "count is: ", count)
        # print("where i is : ", i)
        if (sorted_b[i][0] > T):
            return (Max, minTime)
        if (Max < count):
            # print("Max is: ", Max, "count is: ", count)
            minTime = sorted_b[i][0]
            # print ("    MINTIME: ",minTime)
        Max = max(Max, count)

    return (Max,minTime)


if __name__ == '__main__':
    #Test Cases

    lst1 = [(5,15)]
    print('Input:', lst1)
    print(free_time_intervals(lst1,30))
    print(max_logged_in(lst1,30))

    lst2 = [(1,3), (2,8),(3,6), (2,6), (10,15), (12,17), (19,23), (27,35)]
    print('Input:', lst2)
    print(free_time_intervals(lst2,30))
    print(max_logged_in(lst2,30))

    lst3 = [(5,15), (18,25), (3,12), (4, 11), (1,15), (18,19)]
    print('Input:', lst3)
    print(free_time_intervals(lst3,30))
    print(max_logged_in(lst3,30))
