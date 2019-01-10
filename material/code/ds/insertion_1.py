#! /usr/bin/python3 

import sys
import random

def main (argv): 
    lst = [] 
    for i in range (100):
        lst.append (random.randint (0, 10000))
    for j in range (1, 100):
        key = lst[j] 
        i   = j - 1
        while i > -1 and lst[i] > key: 
            lst[i+1] = lst[i] 
            i = i - 1
        lst[i+1] = key
    for i in range (100):
        print ("lst[",i,"]:", lst[i], sep='')

    sys.exit (0) 

main (sys.argv)
