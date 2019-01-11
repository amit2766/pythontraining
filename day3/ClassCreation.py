class Test:
    def __init__(self):
        print("Inside constructor")
        print("Type(self)",type(self))
        print("self.__dict__ ",self.__dict__)
        self.a=10  # private like behaviour
        self.b=20
        self.c=30
        print("self.__dict__ ",self.__dict__)


    def fun(self):
        print(self.a)
    x="a1"
    y="b1"
    z="c1"







t=Test()
t.fun()

#operator overloading (overload __add__)
class Sum:

    def __init__(self,x):
        self.x=x
    def __add__(self,other):
        return self.x+other.x

s1=Sum(100)
s2=Sum(20)
print(s1+s2)

class CustomList:
    def __init__(self,L):
        self.x=L

    def __mul__(self, other):
        A= CustomList(len(self))

s1=CustomList(4)
s2=CustomList(5)
print("-------",s1*s2)

