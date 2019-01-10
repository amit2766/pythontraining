L = [10, 20, 30, 40, 50] 
for x in L:
    print("x:", x) 

lst_iter = iter(L) 
print("lst_iter:", type(lst_iter)) 
print(next(lst_iter)) 
print(next(lst_iter))
print(next(lst_iter))
print(next(lst_iter))
print(next(lst_iter)) 
try: 
    print(next(lst_iter)) 
except StopIteration: 
    print("Tried to apply next method on empty iterator") 

print("Doing it using while loop") 
lst_iter = iter(L) 
print("hex(id(lst_iter)):", hex(id(lst_iter))) 
while True: 
    try: 
        print(next(lst_iter)) 
    except: 
        break 
print("Doing it explicitly") 
lst_iter =  list.__iter__(L) 
print("hex(id(lst_iter)):", hex(id(lst_iter))) 
while True: 
    try: 
        element = lst_iter.__next__()  
    except StopIteration: 
        break 
    print(element) 



