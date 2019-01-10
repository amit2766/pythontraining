import sys 

class Board: 
    def __init__(self): 
        self.board = [[None, None, None], 
                      [None, None, None], 
                      [None, None, None]] 
        self.nr_rows = 3 
        self.nr_cols = 3 
    def is_occupied (self, row, col): 
        if row < 0 or row >= self.nr_rows:
            raise IndexError ("Bad square") 
        if col < 0 or col >= self.nr_cols: 
            raise IndexError ("Bad square") 
        if self.board[row][col] is None: 
            return True
        else: 
            return False
    def get_square (self, row, col): 
        if row < 0 or row >= self.nr_rows:
            raise IndexError ("Bad square") 
        if col < 0 or col >= self.nr_cols: 
            raise IndexError ("Bad square") 
        return self.board[row][col] 
    def set_square (self, row, col, value): 
        if row < 0 or row >= self.nr_rows:
            raise IndexError ("Bad square") 
        if col < 0 or col >= self.nr_cols: 
            raise IndexError ("Bad square") 
        if value != "X" and value != "O": 
            raise ValueError ("Bad value") 
        if self.board[row][col] != None: 
            raise ValueError ("Occupied square") 
        self.board[row][col] = value 
    def has_won (self, value): 
        if value != "X" and value != "O": 
            raise ValueError ("Bad Value") 
        b = self.board
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

    def display (self): 
        print ("\t", end='') 
        for i in range (self.nr_rows): 
            print (i+1, '\t', end='') 
        print ("\n", end='') 
        for i in range (self.nr_rows): 
            print (i+1, sep='', end='') 
        for j in range (self.nr_cols): 
            print ("\t", self.board[i][j], sep='', end='') 
        print ("\n", end='') 

class Player:  
    def __init__(self, name, symbol): 
        if type (name) != str: 
            raise TypeError ("Bad name") 
        if type (symbol) != str: 
            raise TypeError ("Bad symbol") 
        self.name   = name 
        self.symbol = symbol 
    def get_name (self): 
        return self.name 
    def get_symbol (self): 
        return self.symbol 
    def set_name (self, new_name): 
        if type (new_name) != str: 
            raise TypeError ("Bad new name") 
        self.name = new_name 
    def set_symbol (self, new_symbol): 
        if new_symbol != "X" and new_symbol != "O": 
            raise ValueError ("Bad symbol") 
        self.symbol = new_symbol 
    def move (self): 
        print ("Enter row:") 
        row = int (input ()) 
        if row < 1 or row > 3: 
            raise ValueError ("Bad row") 
        print ("Enter col:") 
        col = int (input ()) 
        if col < 1 or col > 3: 
            raise ValueError ("Bad coloumn") 
        return (row-1, col-1) 
      
class TicTacToe: 
    def __init__(self, T): 
        if type (T) != tuple:
            raise TypeError ("Bad input") 
        if len (T) != 4: 
            raise ValueError ("Bad input") 
        for i in range (len (T)): 
            if type (T[i]) != str: 
                raise TypeError ("Bad input") 
        if T[1] != 'X' and T[1] != 'O': 
            raise ValueError ("Bad input") 
        if T[3] != 'X' and T[3] != 'O': 
            raise ValueError ("Bad input") 
        if T[1] == T[3]: 
            raise ValueError ("Symbols must be different") 
        self.board = Board () 
        self.p1 = Player (T[0], T[1])
        self.p2 = Player (T[2], T[3]) 
    def play (self): 
        pass 
        # Write plays definition on the basis of main's definition 
        # in procedural solution of the approach 

def main (): 
    game = TicTacToe (("Player1", "O", "Player2", "X")) 
    game.play () 
    sys.exit ()

main () 
