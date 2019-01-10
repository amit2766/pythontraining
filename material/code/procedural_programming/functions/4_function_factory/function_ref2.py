#! /usr/bin/python3 

import sys

def f1 ():
    def f2 (X):
        print ("f2:X:", X, sep='') 
    return (f2) 

def main ():
    ref_f2 = f1 ()
    ref_f2 (100)
    ref_f2 (200) 
    ref_f2 ([1,2,3])
    sys.exit (0)

main ()
