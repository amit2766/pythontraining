def gensquares(n): 
    if type(n) != int: 
        raise TypeError("n must be int") 
    for i in range(n): 
        yield (i**2) 

print("type(gensquares):", type(gensquares)) 
ret = gensquares(10) 
print("type(ret):", type(ret)) 
for element in ret:
    print(element) 

for element in gensquares(15):
    print(element) 
