#! /usr/bin/python3 

lst = [x for x in range (10)] 

while True:
    print ("Enter index of an element:", end='') 
    n = int (input ()) 
    try:
        print ("lst[", n, "]:", lst[n], sep='')
    except:
        print ("Wring index. Enter between 0-9") 
    print ("Do you want to continue[y/n]:", end='') 
    ans = input () 
    if ans == 'y' or ans == 'Y':
        continue
    else:
        break 

