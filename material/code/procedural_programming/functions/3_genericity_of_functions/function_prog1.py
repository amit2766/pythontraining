#! /usr/bin/python 

import sys 

def main ():
    res = times (1, 2) 
    print (res) 
    res = times (3.14, 4)
    print (res) 
    res = times ("Hello!", 5)
    print (res) 
    sys.exit (0)

def times (n1, n2):
    return n1*n2 

main ()
