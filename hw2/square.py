#!/usr/bin/python

def square(p):
    n = len(p)
    if (n <= 1):
        return[p[0]^2] #square the constant term
    #or else n > 1
    (p1, p2) = split(p) #split into two parts
    #Fill in the rest
    #You are allowed to use functions like
    #shift (r,k) to compute (x^k)*r for polynomial r
    #add (p1,p2) to add two polynomials
    #sub (p1,p2) to subtract two polynomials
    #scale (p1,c) to scale polynomial p1 by a constant


def split(p):
    n = len(p)
    k = int(n/2)
    p1 = p[0:k+1]
    p2 = p[k+1:n]
    return p1, p2


p = [1,2,3,4,5]
print(square(p))
