#! /usr/bin/python3 

D = {'add':lambda x,y : x+y, 'sub':lambda x,y : x-y,
     'mul' : lambda x,y : x * y}
print ("Enter x:", end='') 
x = int (input ()) 
print ("Enter y:", end='') 
y = int (input ())
print ("Enter operation [add/sub/mul]:", end='') 
ops = input ()
print (x, ops, y, "=", D[ops](x,y))
