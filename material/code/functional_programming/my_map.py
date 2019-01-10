#! /usr/bin/python3 

def my_map (ops, L):
    if (str (type (ops)) != "<class 'function'>"):
        raise TypeError ("ops should be of type function but is of type", type (ops))
    if (type (L) != list):
        raise TypeError ("L should be of type list but is of type", type (L))
    res = [] 
    for x in L: 
        res.append (ops (x))
    return res

def add (x):
    return (x+10)

def main ():
    L = my_map (add, [x for x in range (10)])
    print (L) 

main ()

