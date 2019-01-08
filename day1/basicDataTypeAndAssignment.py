# print("hello")
#
# a=10
# b=10
# b = True
# b="sdf"
#
# n = 10
# f = 3.14
# s = "hello"
# t = (20,30,40)
# L = [True,10,(1,2),"Python"]
# D = {"a":1,"b":2,"c":3}
# S= {-1,"Hello",(1,2)}
#
# print (n)
# print(type(n))
# print(id(n)) #gives the memory location
# print(len(s))
#
# class Vector:
#     pass
# v=Vector()
#
# print(type(v))
#
#
# import sys
# popo=1234989237423980478769897987765765880909099090909
# del(popo)
# print(sys.getrefcount(popo))


# n1=7
# n2=2
# print(n1//n2) #floor division
# print (n1/n2) #
#
# print(n1**n2) # power
# print(pow(n1,n2)) # power
# no overflow in python
# p1=23452523452352345245234523523523458720958723094857230985720347258752304985702349587
# print(p1**39)

#calculating hash
n=10
b=True
s="s"

# print(hash([1,3,4])) #exception: TypeError: unhashable type: 'list'

print(hash(n))
print(hash(b))
print(hash(s))