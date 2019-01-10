#! /usr/bin/python3 

import sys

def main ():
    D = {
         'add':(lambda x,y : x + y), 
         'sub':(lambda x,y : x - y), 
         'mul':(lambda x,y : x * y)
        }

    print ("Enter n1:", end='')
    n1 = int (input ())
    print ("Enter n2:", end='')
    n2 = int (input ())
    print ("Enter operation:[add/sub/mul]:", end='')
    ops = input () 

    if D.get (ops) == None:
        print ("Enter valid operation") 
        sys.exit (0) 
    else:
        res = (D.get (ops))(n1, n2)
        print (n1, ops, n2, res) 

    sys.exit (0)

main ()
