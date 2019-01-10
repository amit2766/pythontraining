#! /usr/bin/python3 

L = [powx (n)(x) for powx in 
                 [lambda n : (lambda x : x ** n)]
                 for n in range (2,6)
                 for x in range (1,5)]

print (L) 
