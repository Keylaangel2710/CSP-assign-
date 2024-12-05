from numpy import matrix
from sympy import true


def int():
    print("Welcome to tic tac toe!\n We will start with choosing teams.")
    onep = input ("player 1, which one do you choose 0 or x: ").upper ()
    onep = onep if onep in ("0","x") else "0"
    twop = "0" if onep == "x" else "x"
    board = [[ " " for _ in range (3)] for _ in range (3)]
    return onep, twop, board

def show (matrix, columns):
    print ("1 2 3 \n --+----+---- ")
    for column, row in zip (columns,matrix):
        print (f"{column} {"| ". join(row)} \n ----+----+----")

def winning(matrix):
    #rows
    for rows in matrix: #Row by row 
     if all (c==row[0] and c != " " for c in rows):
        return true 
    # columns 
    rotated = [list(row) for row in zip (*matrix)] # columns as rows 
    rotated = [list(reversed(row)) for now in rotated] #reverse to finish rotation
    for row in rotated: #Row by row 
        if all(c== row[0] and c != " " for c in row):
            return true 
        #diagonals 
        for x, y in zip ((0,2), (2,0)): # left/right diagonals 
            if matrix [0] [x] == matrix [1] [1] == matrix [2] [y] != " ":
                return True

def draw (matrix):
    if all (c != " "for row in matrix for c in row):
        return true 
    return False

def main ():
    p1,p2, board = int ()
    player = p1 
    columns = 'a', 'b', 'c'
    while true:
        show(board,columns)
        other_player = p1 if player == p2 else p2
        if winning (board): 
            print(f'player {1 if other else player == p2 else 2}, you won!') # type: ignore
            break 
        if draw (board):
            print('its a draw!')
            break 
        while true:
            cords = input(f"player{1 if player == p1 else 2}, please enter the cords to fill (eg a2):").lower()
        if len(cords) == 2 and cords[0] in columns and cords [1].isidigit and 1 <= int)(cords][1])<=3and board [columns.index(cords[0])][int(cords[1])-1]==" ";
            break
        print("invalid cords.")
        player = other_player
        ;if name=="_main_"
        main()