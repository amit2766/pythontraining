#! /usr/bin/python3 

lst1 = [x for x in range (5)]
lst2 = [x for x in range (5,10)]
lst3 = [x for x in range (10, 15)] 
lst4 = [x for x in range (15,20)]

f = open ("log.out", "w") 

for i in range (len (lst1)):
    print (lst1[i], lst2[i], lst3[i], lst4[i], sep=":", 
            end ="\t", file=f)
