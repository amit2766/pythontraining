#! /usr/bin/python3 

lst1 = [x for x in range (5)] 
lst2 = [x for x in range (5,10)] 
lst3 = [x for x in range (10,15)] 

for i in range (len (lst1)):
    print (lst1[i], lst2[i], lst3[i])

print ("Demo of : as a separator") 
for i in range (len (lst1)):
    print (lst1[i], lst2[i], lst3[i], sep=':')

print ("Demo of end of line") 
for i in range (len (lst1)):
    print (lst1[i], lst2[i], lst3[i], sep=':', end='\t')
print ('\n') 

print ("Demo of redirection") 

f = open ("abc.txt", 'w') 

for i in range (len (lst1)):
    print (lst1[i], lst2[i], lst3[i], sep=':', end='\t', 
            file=f)
f.write ('\n') 
f.write ("End of file") 
