def square(p):
    n = len(p)
    if (n <= 1):
        return[p[0]^2] #square the constant term
    #or else n > 1
    (p1, p2) = split(p) #split into two parts
    # F i l l in t h e r e s t
    # You are a l l ow e d t o use f u n c t i o n s l i k e
    # s h i f t ( r , k ) t o compute ( x ˆk ) ∗ r f o r p oly n om i al r
    # add ( p1 , p2 ) t o add two p ol y n om i al s
    # sub ( p1 , p2 ) t o s u b t r a c t two p ol y n om i al s
    # s c a l e ( p1 , c ) t o s c a l e a p oly n om i al p1 by a c o n s t a n t c


def split(p):
    
