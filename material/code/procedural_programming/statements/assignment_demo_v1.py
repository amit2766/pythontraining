#! /usr/bin/python3 

e = "-" * 80

print ("[1]:Basic assignment") 
msg = "This is a message"
print (msg) 
print (e) 

print ("[2]:Tuple assignment (positional)") 
(o1, o2, o3) = ("Hello", [1,2,3], {'a':1, 'b':2, 'c':3})
print ("o1:", o1)
print ("o2:", o2)
print ("o3:", o3)
print (e)

print ("[3]:List assignment (positional)") 
[o1, o2, o3] = ["Hello", "Python", "World"] 
print ("o1:", o1)
print ("o2:", o2) 
print ("o3:", o3) 
print (e) 

print ("[4]:Sequence assignment generalized") 
o1, o2, o3, o4 = 1, 3.14, "Hello", (1,2,3)
print ("o1:", o1) 
print ("o2:", o2) 
print ("o3:", o3) 
print ("o4:", o4) 
print (e) 

print ("[5]:Multiple target assignment") 
L = [o1, o2, o3] = [1, 3.14, "Hello"]
for o in L:
    print ("o:", o)
print (e) 

print ("[6]:Extended sequence unpacking") 
a, *b = 'SPAM' 
print ("a:", a) 
print ("b:", b) 
print (e) 

print ("[7]:Augmented assignment") 
num = 40
print ("num:", num) 
num += 4
print ("After num += 4, num:", num) 
print (e) 

print ("[8]:Advanced sequence patterns") 
msg = 'SPAM MESSAGE' 
print ("msg:", msg) 
T = o1, o2, o3 = msg[:2], msg[2:6], msg[6:]
print ("[8-1]:")
print ("o1:", o1) 
print ("o2:", o2) 
print ("o3:", o3) 
print ("[8-2]:Printing through tuple") 
for o in T: 
    print ("o:", o)
print ("[8-3]:[a, b, c] = [1, 2, 3]")
[a, b, c] = [1, 2, 3]
print ("a:", a)
print ("b:", b)
print ("c:", c) 
print ("[8-4]:[a,b,c] = [[1,2,3], [4,5,6], [7,8,9]]")
[a, b, c] = [[1,2,3], [4,5,6], [7,8,9]]
print ("a:", a) 
print ("b:", b) 
print ("c:", c) 
print ("[8-5]:[[a,b], c] = [[[1,2,3],[4,5,6]],[7,8,9]]")
[[a,b],c] = [[[1,2,3], [4,5,6]], [7,8,9]]
print ("a:", a) 
print ("b:", b) 
print ("c:", c) 
print ("[8-6]:a,b,c = range (3)")
a, b, c = range (3)
print ("a:", a) 
print ("b:", b) 
print ("c:", c) 
print ("[8-7]:for loop v1") 
lst = [(1,2,3), (4,5,6), (7,8,9)] 
it = 0 
for (x,y,z) in lst:
    print ("iteration:", it) 
    print ("x:", x) 
    print ("y:", y) 
    print ("z:", z)
    it = it + 1
print ("[8-8]:for loop v2") 
lst = [((1,2),3), ((4,5),6), ((7,8),9)]
it = 0
for ((x,y),z) in lst:
    print ("iteration:", it) 
    print ("x:", x)
    print ("y:", y) 
    print ("z:", z) 
    it = it + 1
print (e) 

print ("[9]:Advanced extended unpacking:for python3 only") 
print ("[9-1]:a,b* = lst") 
lst = [1,2,3,4,5] 
a, *b = lst 
print ("a:", a) 
print ("b:", b) 
print ("[9-2]:*a, b = lst") 
*a, b = lst
print ("a:", a) 
print ("b:", b) 
print ("[9-3]:a, b, *c, d = lst")
a, b, *c, d = lst 
print ("a:", a) 
print ("b:", b) 
print ("c:", c) 
print ("d:", d) 
print (e) 
