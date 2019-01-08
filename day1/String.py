# import math
#
# s1 = "hello"
# s2 = 'hello'
# s3 = 'hello\nworld'
# s4 = 'hello world, I am "Amit" '
# s5 = "hello world, I am 'Amit' "
# s6 = """"hello world, I am
#         amit how are
#         ayou            i am
#         good"""
# print(s1)
# print(s2)
# print(s3)
# print(s4)
# print(s5)
# print(s6) #used for documentations
#
# """This is not documentation"""
# def f(a,b):
#     """ this is documentaiton of f"""
#     pass
#
# help(f)
# print(dir(math))
#
# class T:
#     def __str__(self):
#         return "this is class T"
#
# class OT:
#     pass
# objT = T()
# print(objT)
# print(OT())

# Operations on String (Common operations of String, List, Tuple)
s1= "hello"
s2= "world"
s3= "1234"
lst1= list(s1)
lst2= list(s2)
lst3= list(s3)
tpl1 = tuple(s1)
tpl2 = tuple(s2)
tpl3 = tuple(s3)
#
# print(lst1)
# print (tpl1)
# print (tpl1)
#
# print(tpl1+tpl2)
# print(tpl3*2)
# print(lst3*2)

#Substring operations
# index
# s[i]
#range
#s[i,j]
# slice
# s[i:j:k] # select every kth letter starting from i until j(including i excluding j). If k is negative go in backward direction.

s="Hello world"

# print(s[20:1:-3])
#
# for i in range (10,15):
#     print(i)
#
# for i in range (15,10,-1):
#     print (i)
#
#
# # 0 ,1 ,.............12
# # _______________________
# #: |H|e|l|l|o| |w|o|r|l|d|:
# # -12,-11..............-1
# #: left anchor  right anchor :
# print ("negative range : " +s[-11:-6])
#
# print("anchor left "+ s[:4])
# print("anchor right "+ s[4:])
# print("Reverse string "+ s[::-1])
# print("All even indices "+ s[::2])
# print("All odd indices "+ s[1::2])
#
#

s= "Hello,world!"
print('-------------------------')

print(s.index('e'))
print(s[s.index('H'):s.index('o')+1])
print(s.index('l',4)) #index of first occurance after position 4
# print(s.index('l',14)) #exception
print(s.count('l'))
print(s.find('o'))
print(s.find('o',14)) #no exception

print("        a   ".strip()) #strip starting and ending white spaces or \n
print("some:thing:split:by:colon".split(":"))
print("some:thing:split:by:colon".isalpha()) #false
print("some thing split by colon".isalpha()) #false
print("somethingsplitbycolon".isalpha()) #True

# print(s[5])
# print(s[-3])
# print(s[15])
# print(s[1:8])
# print(s[-5:-2])
# print(s[1:11:2])
# print(s[1:11:-2])
# print(s[11:1:2])
# print(s[2:10:4])
# print(s[3:6:9])
# print(s[::2])
# print(s[::-1])

# ,
# l
# out of index
# out of index
# ello,wo
# orl
# el,ol
# ''
# ''
# lw
# l
# Hlowrd
#
# !dlrow,olleH
