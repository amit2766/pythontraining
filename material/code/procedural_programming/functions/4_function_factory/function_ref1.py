#! /usr/bin/python3 

import sys

def f1 ():
    def f2 ():
        X = 100
        print (X) 
    return (f2) 

def main ():
    ref_f2 = f1 ()
    ref_f2 ()
    sys.exit (0) 

main ()
