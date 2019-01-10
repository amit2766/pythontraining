import sys, random 

class Decorator: 
    def __init__(self, ref_fun): 
        self.ref_fun = ref_fun
        
    def __call__ (self, n1, n2): 
        print ("In WP:")
        print ("n1:", n1, "n2:", n2)
        ret = self.ref_fun (n1, n2) 
        print ("End of WP") 
        return (ret) 

@Decorator
def my_add (n1, n2): 
    return (n1+n2) 

def main (): 
    for i in range (5):
        print (my_add (random.randint (0, 101), random.randint (101, 201)))

    sys.exit (0) 

main () 
