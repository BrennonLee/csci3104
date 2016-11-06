#!/usr/bin/python

def sumTwo(a, T):
    n = len(a)
    # j = 0
    i, j = 0, 0
    ans = ()
    table = {}
    for i in range(n):
        table[a[i]] = i;   #sets up hashtable since dictionaries are hashtables in python
        # print(table)
    for j in range(n):
        if (T - a[j]) in table:
            ans = (a[j], T-a[j])
            return ans
            return True
        else:
            return False

    # for i in range(n):
    #     target = T - a[i]
    #     # print("current elm is: ", a[i])
    #     # print('target is: ', target)
    #     print("\n")
    #     for j in range(n):
    #         if (target == a[j]):
    #             # print("elm has been added! ", a[i])
    #             ans.append(a[j])
    # return ans
def sumThree(a,T):
    n = len(a)
    i, j = 0,0
    ans2 = ()
    table = {}

    # print("answer is ", answer )

    for j in range(n):
        # print (j)
        answer = sumTwo(a,T-a[j])
        if (answer != False):
            print(answer, a[j])
            return True
    return False
        # if (T-answer[0] - answer[1]) in table:
            # ans2 = answer
            # return (answer, a[j])
        # else:
            # return ("none found")

if (__name__ == '__main__'):

    a = [10, 11, 2, 3, 15, 5, 8, 19, -2, 23, 25, 18, 45]
    print(sumThree(a, 10))
