#! /usr/bin/python3 

X = 100
def f1 ():
    import global_access_ways 
    print ("f1:global_access_ways.X:", global_access_ways.X           , sep='') 
    X = "Hello" 
    print ("f1:X:", X, sep='')

def f2 ():
    print ("f2:X:", X, sep='') 

Y = 100
def f3 ():
    import sys
    import global_access_ways
    ref_s = sys.modules['global_access_ways'] 
    print ("f3:ref_s.Y:", ref_s.X, sep='')
    X = "Hello"
    print ("f3:Y:", X, sep='') 

def f4 ():
    print ("f4:Y:", Y, sep='') 

