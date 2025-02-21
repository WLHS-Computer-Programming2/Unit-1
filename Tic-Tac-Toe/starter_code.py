'''
To do:
1) Implement winner logic
2) Add ties to winner logic
3) Make sure player cannot take occupied space
4) Make sure player can only enter valid row/columns 

'''

board = [
#col  0   1   2
    ['_','_','_'], # row 0
    ['_','_','_'], # row 1
    ['_','_','_']  # row 2
]

def print_board(board):
    for row in board:
        for item in row:
            print(item, end=' ')
        print()

def check_winner(board,symbol):
    # returns true if winner
    # rows
    
    # cols
    

    # diagonals

    # what about ties?

    return False

def main():
    while True:
        player_one = "X"
        player_two = "O"
        print_board(board)
        print(f"Player {player_one} make your move")
        row = int(input("Row? (0,1,2)"))
        column = int(input("Column? (0,1,2)"))
        board[row][column] = player_one
        print_board(board)
        if(check_winner(board,player_one) == True):
            print(f"Player {player_one} wins")
            break
        else:
            print(f"Player {player_two} make your move")
            row = int(input("Row? (0,1,2)"))
            column = int(input("Column? (0,1,2)"))
            board[row][column] = player_two
        if(check_winner(board,player_two) == True):
             print(f"Player {player_one} wins")
             break
        else:
            continue

main()
