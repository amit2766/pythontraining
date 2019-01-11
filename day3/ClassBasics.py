# syntax class <class name>
# class T:                  # Syntax 1
# BLOCK

# class D (B1, B2, B3,...,Bn):     # Syntax 2
# BLOCK

# class DM (B1, B2, B3,...,Bn, metaclass= Meta)  # Syntax 3

# class CM (metaclass= XYZ) # Syntax 4

class T:  # class statements are executed when class is loaded
    a = 10
    b = 20
    c = 30

    def f():
        print("Hey")

class T1:
    print("Hello")
    print("World")
    a = 10
    b = 20
    c = a + b
    print(c)


# all are of class type
print(type(T))
print(type(T1))
print(type(bool))
print(type(int))
print(type(list))
print(type(map))

t = T()
print(type(t))

print(T1.b)
print(T.f())

# print(t.f()) #TypeError: f() takes 0 positional arguments but 1 was given.


# type is root of all other types (like object class of java)
# inheritence wise c

class C:
    def fun(self):
        # print("Type " , type(self))
        print ("Inside C")
# C.fun(10)

c = C()
c.a=10



