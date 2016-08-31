#!/usr/bin/python
def commonElm(a, b):
    i = 0
    j = 0
    m = len(a)
    n = len(b)
    while (a[i] != b[j]):
            if (a[i] < b[j]):
                i = i + 1
            else:
                j = j + 1
    if(a[i] == b[j]):
        print("common elm was: ", a[i])
        return True
    else:
        print("No match found")
        return False

a = [0, 2, 4, 5, 6, 8]
b = [1, 3, 5, 7, 9, 12]
commonElm(a,b)
