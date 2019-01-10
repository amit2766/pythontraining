L1 = [x for x in range(1, 10)]
L2 = [y for y in range(3, 25)]
L3 = [z for z in range(2, 12)]
L1_filter = []
for x in L1:
    if x % 2 == 0:
        L1_filter.append(x)
L2_filter = []
for x in L2:
    if x % 7 == 3:
        L2_filter.append(x)
L3_filter = []
for x in L3:
    if x % 2 == 1:
        L3_filter.append(x)
for i in range(len(L1_filter)):
    L1_filter[i] = L1_filter[i] ** 2

for i in range(len(L2_filter)):
    L2_filter[i] = L2_filter[i] ** 3

for i in range(len(L3_filter)):
    L3_filter[i] = L3_filter[i] ** 4
cart = []
for x in L1_filter:
    for y in L2_filter:
        for z in L3_filter:
            cart.append((x, y, z))
rs_semi = []
for (x, y, z) in cart:
    rs_semi.append(x-y+z)
rs_final = []
for x in rs_semi:
    if x > 0:
        rs_final.append(x)
del(L1, L2, L3, L1_filter, L2_filter, L3_filter, cart, rs_semi)
print(rs_final)
        
