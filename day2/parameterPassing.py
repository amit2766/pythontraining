def f(a,b,c):
    print(a,type(a))
    print(b,type(b))
    print(c,type(c))

f(10,20,30) # Nonkeyword syntax. Positional matching
f(a=10,b=20,c=30) #Keyword syntax
f(a=10,c=30,b=20) #Keyword syntax. Correct
f(10,c=30,b=20) #Mixed syntax. Correct. First is positional.
# f(10,b=30,20) #Error. Positonal is used after keyword
# f(a=10,b=20,d=30) #Error TypeError: f() got an unexpected keyword argument 'd'

(a,b)=(10,20) #Tupple positional assignment
print(a)
print(b)

[a,b]=[10,20] #List positional assignment
print(a)
print(b)

a,b,c=1,2,3
print(a)
print(b)
print(c)

# a,b,c=1,2,3,4 #ValueError: too many values to unpack (expected 3)
# a,b,c=1,2 #ValueError: not enough values to unpack

a, *b,c =1,3 #Starred expression. *b will be an empty list
a, *b,c =1,2,3,4,5,6, #a=1,c is last and b is list of all other elements
print(a)
print(b)
print(c)

# a, *b,*c =1,3 #SyntaxError: two starred expressions in assignment

def F(*arg):
    print(arg) #arg is a tuple
    for i in range (len (arg)):
        print("arg[%d]:%d"%(i,arg[i]))
F(1,2,3,4,5,6)

def F(a,b,c, *arg, d,e): #*arg is extra non arguments
    print(a,type(a))
    print(b,type(b))
    print(c,type(c))
    print(arg,type(arg))
    print(d,type(d))
    print(b,type(b))

F(10,20,30,40,50,60,d=1,e=2) # anything after *arg will become keyword only syntax
# F(10,20,30,40,50,60,1,2) # Error TypeError: F() missing 2 required keyword-only arguments: 'd' and 'e'

# F(a=10,b=20,30,40,50,60,d=1,e=2) #Error SyntaxError: positional argument follows keyword argument
# Extra non keywords can be send only using non keyword fashion. Hence these a and b are forcefully nonkeyword

def G(a,b,c,d=400,e=500): # d and e are optional they have default values
    print(a,b,c,d,e)

G(1,2,3)

# def G(a,b,c,d=400,e=500,f): # SyntaxError: non-default argument follows default argument
#     pass
def G(a,b,c,d=400,e=500,*arg,f):
    pass

def F(**kwargs):
    print(kwargs,type(kwargs))

F(a=1,b=7)
F(**{'a':10,'b':20}) # same as above line. Except sent using map

# function above is same as in dict
print(dict(a=1,b=7))

def Master(a,b,c,*d,e=100,f=200,g,**i):
    print(a,type(a))
    print(b,type(b))
    print(c,type(c))
    print("Extra non keyword argements: ")
    for (x,y) in enumerate(d):
        print(x,y)
    print(e, type(e))
    print(f, type(f))
    print(g, type(g))
    for (k,v) in dict(i):
        print(k,v)

# Master(1,2,3,4,5,6,7,8,g=100,(x=10,y=20))

def F(a,b,*c,d):
    print(a,b,c,d)
F(1,2,(3,4,5,6,7),d=8) #c will be a tuple of tuple
F(1,2,*(3,4,5,6,7),d=8) #c will be a tuple. So if we want a tuple
F(1,2,*[3,4,5,6,7],d=8) #c will be a tuple. So if we want a tuple