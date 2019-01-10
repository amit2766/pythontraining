#! /usr/bin/python3 

import sys

def main (argv): 
    res = intersection ([1,2,3], (3,4,5,6))
    print (res) 
    D1 = {'a':1, 'b':2, 'c':3, 'd':4}
    D2 = {3.14:'a', 34:'b', 234:54}
    res = intersection (D1.keys(), D2.values())
    print (res) 
    sys.exit (0) 
def intersection (s1, s2): 
    L = [] 
    for x in s1:
        if x in s2:
            L.append (x) 
    return (L) 
main (sys.argv) 
