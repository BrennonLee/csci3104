#!/usr/bin/python

def minSteps(pos, E):

    fail = 18
    if(pos == 4 or pos == 11 or pos == 13 or pos == 16):
        return fail
    elif(pos == 5 or pos == 12):
        E = E+5
    elif(pos == 17):
        return 1
    elif(pos > 17):
        return fail
    elif(E <= 0):
        return fail

    a1 = 1+minSteps( (pos+1), (E-1))
    a2 = 1+minSteps( (pos+2), (E-3))
    a3 = min(a1, a2)

    return a3

E = 9
pos = 0
print (minSteps(pos,E))
