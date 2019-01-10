import sys 

nr_rows   = 3 
nr_cols   = 3 
max_moves = 9 

def create_board (): 
    L = list ([]) 
    for i in range (3): 
        L.append ([None, None, None]) 
    return L 

def display_board (board): 
    print ("\t", end='') 
    for i in range (nr_rows): 
        print (i+1, '\t', end='') 
    print ("\n", end='') 
    for i in range (nr_rows): 
        print (i+1, sep='', end='') 
        for j in range (nr_cols): 
            print ("\t", board[i][j], sep='', end='') 
        print ("\n", end='') 

def has_won (board, value): 
    
    b = board 
    
    if b[0][0] == value and b[0][1] == value and b[0][2] == value: 
        return True
    elif b[1][0] == value and b[1][1] == value and b[1][2] == value: 
        return True 
    elif b[2][0] == value and b[2][1] == value and b[2][2] == value: 
        return True 
    elif b[0][0] == value and b[1][0] == value and b[2][0] == value: 
        return True 
    elif b[0][1] == value and b[1][1] == value and b[2][1] == value: 
        return True 
    elif b[0][2] == value and b[1][2] == value and b[2][2] == value: 
        return True 
    elif b[0][0] == value and b[1][1] == value and b[2][2] == value: 
        return True 
    elif b[0][2] == value and b[1][1] == value and b[2][0] == value: 
        return True 

    return False 

def main (): 
    
    board = create_board () 
    
    turn = {0:"Player1", 1:"Player2"} 
    sym  = {0:"O", 1:"X"} 
    move = 0 

    display_board (board) 
    
    for i in range (max_moves): 
        print (turn[move], "'s turn", sep='') 
        print (turn[move], "Enter row:", end='') 
        row = int (input ()) 
        if row < 1 or row > 3:
            raise ValueError ("Invalid row") 
        print (turn[move], "Enter col:", end='') 
        col = int (input ()) 
        if col < 1 or col > 3: 
            raise ValueError ("Invalid col") 
        if board[row-1][col-1] == None: 
            board[row-1][col-1] = sym[move]
        else: 
            raise ValueError ("Existing square") 
        display_board (board) 
        if i > 3: 
            if has_won (board, sym[move]) == True: 
                print (turn[move], "has won") 
                break 
        move = (move + 1) % 2 
    else: 
        print ("Game Drawn") 

    sys.exit (0) 

main () 
