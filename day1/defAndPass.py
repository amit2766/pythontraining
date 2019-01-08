def someMethod(s1,s2):
    L=[]
#every def is a callable object
print(type(someMethod(1,2)))

class T: #callable
    def __init__(self):
        pass
    def __call__(self):
        print("Callable of type T")
    def something(self):
        print("inside something")

class NC:
    pass
t = T()
t.something()

print(t()) #calling t
n=NC()
print(type(n))
# print(n()) #TypeError: 'NC' object is not callable

print(dir(t))
print(callable(t)) #true if t is callable