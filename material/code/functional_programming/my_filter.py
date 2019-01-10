#! /usr/bin/python3 

def my_filter (cond, L):
    if str (type (cond)) != "<class 'function'>":
        raise TypeError ("cond should be of type <class 'function'> but is of", 
                          type (cond))
    if type (L) != list:
        raise TypeError ("L should be of type list but is of", type (L))
    res = [] 
    for x in L:
        if cond (x) == True:
            res.append (x) 
    return res 

def is_even (x):
    return (x % 2 == 0)

def main ():
    L = my_filter (is_even, [x for x in range (100)])
    print (L) 
    
    print (list (filter (is_even, [x for x in range (100)])))

main ()
