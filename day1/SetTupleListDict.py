# L1=[10,20,30,40,50,60,70,80,90]
# # L2=["a","b","c"]
# # z=zip(L1,L2)
# # print(z)
#
# L2 = [n**2 for n in range(1,101) if n%2 ==0]
# print ( L2)
# L1.append('5')
# print (L1)
# for i in L1[1:10:2]:
#     print(i)
# T1= (10,20,30,40,50,60,70,80,90)
# for i in L1[1:10:2]:
#     print(i)
# L1.append(T1) # will add T1 as tuple to last index
# print(L1)
# L1.extend(T1)# will add each object of tuple as objects inside list
# print(L1)
# L1.insert(99,'A')
# print('----asd--------')
# print(L1)
#
# T2=(10)#not a tuple
# T3=(10,) #is a tuple
# print(type(T2))
# print(type(T3))
#
# # print(L1.index(10))
# # print(T1.index(10))
# #L1.find() no find method in list or tupple
# # print(T1.__sizeof__())
# del(L1[1]) #index 1 gone
# del (L1[1:2]) #index 1 to 2 gone
# L1[5:7] = [] # same as deleteing 5 to 7 should not be used
# L1[5] =  [] # will replace 5th index by [] (will not delete)
# L1.remove(10) #remove 10 element. if not present will throw exception
# L1.pop() #will delete last index
#
#
# print("---------------------------------------------")
# L1=[10,20,30,40,50,60,70,80]
# def f(L1):
#     print("f:lst:", L1)
#     print("f:id(L1)", id(L1))
# f(L1) #pass by reference
#
# L2= L1.copy() # to emulate copy object
# print(L1==L2)
# print(id(L1))
# print(id(L2))
#
# #dict set and list have copy method
#
# L1=[10,20,30,40,50,60,70,80]
# L2=L1
# print(L1)
# print(L2)
# print(id(L1))
# print(id(L2))
# L1=[]
# print(L1)
# print(L2)
# print(id(L1))
# print(id(L2))
#
# L1.clear()
# print(L1)
# print(L2)
# print(id(L1))
# print(id(L2))
#
# # L3=sorted(L1) #will not modify L1
# # L1= L1.sort() #will sort L1 and modify itslef
# # L1[::-1] #will return new list
# # L1.reverse() # will reverse list
#
# #set do have discard method L1 does not have discard
# # print(dir(L1))
# print(sorted(L1,reverse=True))
#
# #Set
# s="aslfkja;lsfkafkafhklasdfhkajhfaklfhaklfhweiuqrqwiurhklajfdsaf"
# print(set(s))
# set1 = {1,2,3,4}
# set2 = {4,5,6,7,8,9}
# print('set related operations ----')
# print(set1.intersection(set2))
# print(set1.union(set2))
# print(set1.difference(set2))
# print(set1.symmetric_difference(set2))
# print(set1.issubset(set2))
# print(set1.issuperset(set2))
# print(set1.isdisjoint(set2))
#
# #add,copy,discard,remove,clear,pop
#
# s=set()
# s.add(1)
# s.add(2)
# s.add(3)
#
# #set cannot have mutable elements (list,dict, other set)
# # s.add(set1) #TypeError: unhashable type: 'set'
# # s.add({"1",1}) #TypeError: unhashable type: 'map'
# # s.add([1]) #TypeError: unhashable type: 'map'
#
# # Set does not guarantee order but once decided order does not change unless set is changed.
# s ={} # will create an empty dictionary
# s = set() # will create an empty set
# print(set1 is set2) # compares id of both objects
#

print ('--------------------- Dictionary ------------------------')
d = {
    True:10,
    False:20,
    3.14:30,
    1000:40,
    "a":50,
    "b":60
}
#Key is immutable object
#Value any object

print(d["a"])
print(d.keys())

for k in d.keys():
    print (d[k])

for v in d.values():
    print (v)
print(d.items()) #returns tuple

for k,v in d.items():
    print (k,v)

# print(d['x']) # KeyError: 'x' exception
print(d.get('x')) # no exception

#pop and pop item
d.setdefault('x',True) # if not present then add True with key x if present then return actual value
x=7
if (x==None):
    print("falxs")

d1 = {
    "1":"a",
    "2":"b",
    "3":"c"
}
#Create dict

d= dict(a=10,b=20,v=30) #keys will always be converted to string
dict.fromkeys([1,2,3,4,5,6,7], None) #keys 1 to 7 with default value none

K = [1,2,3,4,5,6]
V = ["a","b","c","d","e"]
Y = ["a","b","c","d","e"]
d= dict(zip(K,V)) #creates dict using zip function
print(zip(K,V))
for z in zip(K,V,Y):
    print(z)
# set is size mutable

#internally set is key of dict with default value

L=[1,2,3,4,5,6]
# l.remove(x) #value error exception

set1= {1,2,3,4}
set.remove(x) #set.remove(x) #key error exception

#we dont need to store values corresponding to keys for set. This is a wrapper of key implementation around dictionary

#since types are not check we can pass
def intersaction(L1,L2):
    #expect L1 and L2 to be list and perform operation
    pass
#pass intersaction some numbers and no compilation error