#! /usr/bin/python3 

def main ():
    L1 = [x + y for x in range (5) for y in range (10)]
    print (L1) 
    L2 = [x * y for x in range (5)
                for y in range (10)] 
    print (L2) 
    
    L = [lambda x : x ** 2, lambda x : x ** 3, lambda x : x ** 4] 
    
    L3 = [x(y) for x in L
               for y in range (5)] 
    print (L3)

    L4 = [x + y for x in 'SPAM' 
                for y in 'HAM'] 
    print (L4) 

    L5 = [(x, y) for x in range (10) if x % 2 == 0
                 for y in range (10) if y % 2 == 1] 
    print (L5) 

main ()
