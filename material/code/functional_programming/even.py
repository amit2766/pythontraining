#! /usr/bin/python3 

def get_even (L): 
    lst = [] 
    for x in L:
        if x % 2 == 0:
            lst.append (x)
    return (lst) 

def is_even (x):
    return (x % 2 == 0)

def main ():
    L = [x for x in range (15)] 
    print ("Original L:", L)
    e_lst = get_even (L) 
    print ("After get_even (L), L:", L)
    print ("After get_even (L), e_lst:", e_lst)
    e_lst_f = list (filter (is_even, L))
    print ("After 2:L:", L)
    print ("After 2:e_lst_f:", e_lst_f)
    e_lst_lambda = list (filter ((lambda x : x % 2 == 0), L))
    print ("e_lst_lambda:", e_lst_lambda)
    e_lst_map = list (map ((lambda x : x % 2 == 0), L))
    print ("e_lst_map:", e_lst_map)
main ()
