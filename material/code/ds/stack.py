#! /usr/bin/python3 

import sys

def main ():
    st1 = create_stack ()
    st2 = create_stack ()

    if is_empty (st1) == True:
        print ("Initially st1 is empty") 
    else:
        print ("Fatal Error") 
        sys.exit (-1) 

    if is_empty (st2) == True:
        print ("Initially st2 is empty") 
    else:
        print ("Fatal error") 
        sys.exit (-1) 

    lst1 = [x for x in range (5)] 
    for x in lst1:
        push (st1, x)

    lst2 = [c for c in 'SPAM'] 
    for c in lst2:
        push (st2, c) 
    
    print ("stacktop (st1):", examine_stack_top (st1))
    print ("stacktop (st2):", examine_stack_top (st2))

    while True:
        x = pop (st1)
        if (x == None):
            break
        else:
            print (x) 

    while True:
        x = pop (st2)
        if (x == None):
            break
        else:
            print (x) 

    sys.exit (0)
def create_stack ():
    lst = [] 
    return (lst) 
def push (stack, obj):
    if type (stack) != list:
        print ("push:TypeError") 
        sys.exit (-1) 
    stack.append (obj) 
def is_empty (stack): 
    if type (stack) != list:
        print ("is_empty:TypeError") 
        sys.exit (-1) 
    return (len (stack) == 0)
def pop (stack): 
    if type (stack) != list:
        print ("pop:TypeError") 
        sys.exit (-1) 
    if is_empty (stack) == True:
        return (None)
    else:
        return (stack.pop ())
def examine_stack_top (stack):
    if type (stack) != list:
        print ("examine_stack_top:TypeError") 
        sys.exit (-1) 
    if is_empty (stack) == True:
        return (None)
    else:
        return (stack[len(stack)-1])

main ()
