import sys 

def main(argv): 

    if len(argv) != 2: 
        raise ValueError("Usage Error:", argv[0], "file name") 
        sys.exit(-1) 

    with open(argv[1], "r") as f: 
        for line in f:
            print(line) 

    sys.exit(0) 

main(sys.argv) 


"""Alternate code : 

try: 
    f = open(argv[1], "r") 
except: 
    print("cannot open file") 
    sys.exit(0) 

for line in f: 
    print(line) 

f.close() 

sys.exit(0) 
""" 
