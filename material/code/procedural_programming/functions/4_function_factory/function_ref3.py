#! /usr/bin/python3 

import sys

def f1 ():
    X = 2
    def f2 (n):
        print ("f2:X=", X, " n=", n, " X**n=", X**n, sep='')
    return (f2)

def main ():
    ref_f2 = f1 ()
    ref_f2 (2)
    ref_f2 (3)
    ref_f2 (3.14)
    sys.exit (0) 

main ()
