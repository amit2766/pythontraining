#! /usr/bin/python3 

import sys
import random

def main (argv):
    if len (argv) != 2: 
        print ("usage error:", argv[0], "nr_elements") 
        sys.exit (-1) 
    n = int (argv[1]) 

    lst = [] 
    input_lst (lst, n) 
    sort_lst (lst)
    output_lst (lst) 

    sys.exit (0)

def input_lst (lst, n): 
    cap = 1000000
    for i in range (n):
        lst.append (random.randint (0, cap))

def output_lst (lst): 
    for i in range (len (lst)):
        print ("lst[", i, "]:", lst[i], sep='')

def sort_lst (lst): 
    for j in range (1, len(lst)):
        key = lst[j]
        i   = j-1
        while i > -1 and lst[i] > key:
            lst[i+1] = lst[i]
            i = i-1
        lst[i+1] = key 

main (sys.argv) 
