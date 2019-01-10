#! /usr/bin/python3 

import sys
import random

def main (argv):
    if len (argv) != 2:
        print ("Usage error:", argv[0], "n") 
        sys.exit (-1) 
    n = int (argv[1]) 
    if n <= 0:
        print ("Nothing to do")
        sys.exit (-1) 
    lst = []
    for i in range (n):
        lst.append (random.randint (0, 10000))
    for j in range (1,n):
        key = lst[j]
        i = j - 1
        while i > -1 and lst[i] > key:
            lst[i+1] = lst[i] 
            i = i - 1
        lst[i+1] = key
    for i in range (n):
        print ("lst[", i, "]:", lst[i])
    sys.exit (0) 

main (sys.argv)
