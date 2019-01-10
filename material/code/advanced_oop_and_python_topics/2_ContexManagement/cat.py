import sys 

def main(argv): 
    if len(argv) != 2: 
        raise ValueError(argv[0], "file_name") 
    with open(argv[1], "r") as f: 
        for line in f:
            print(line, end='') 
    sys.exit(0)

main(sys.argv) 
