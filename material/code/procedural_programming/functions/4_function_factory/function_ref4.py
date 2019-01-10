#! /usr/bin/python3 

import sys

def f1 (n):
    def f2 (X):
        return (X ** n)
    return (f2) 

def main ():
    sqrt = f1 (2) 
    print ("sqrt (2) =", sqrt (2))
    print ("sqrt (15) =", sqrt (15))
    print ("sqrt (3.14) =", sqrt (3.14))

    cube = f1 (3)
    print ("cube (10) =", cube (10))
    print ("cube (234) =", cube (234))
    print ("cube (3.14) =", cube (3.14))

    sys.exit (0)

main ()
