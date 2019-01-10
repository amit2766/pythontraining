#! /usr/bin/python3 

import sys

def main (argv):
    
    if len (argv) != 2:
        print ("usage error:", argv[0], "search_key") 
        sys.exit (-1) 
    
    lst = [x for x in range (50)]
    search_key = int (argv[1])

    for i in range (len (lst)):
        if lst[i] == search_key:
            break
    else:
        print ("Element not found")
        sys.exit (-1)
    print ("element found at index:", i)
    
    sys.exit (0) 

main (sys.argv) 
