location_map={
    1: (0,0),
    2: (0,1),
    3: (0,2),
    4: (1,0),
    5: (1,1),
    6: (1,2),
    7: (2,0),
    8: (2,1),
    9: (2,2)}

def create_board():
    board = [
        ["1 |","2 |","3"],
        ["4 |","5 |","6"],
        ["7 |","8 |","9"]
    ]
    return board

def update_board(board,row,col,symbol):
    board[row][col] = symbol
    return board

def print_board(board):
    for row in board:
        for item in row:
            print(item,end=" ")
        print()
    print()
    
def initialize_game():
    player_symbol = ""
    computer_symbol = ""
    my_board = create_board()
    print_board(my_board)
    player_symbol = input("Do you want to be X or O? ")
    if player_symbol == "X":
        computer_symbol = "O"
    else:
        computer_symbol = "X"
    symbols = (player_symbol,computer_symbol)
    board = create_board()
    return (symbols,board)

def make_move(board,player_symbol):
    global location_map
    while True:
        location = int(input(f"Where would you like to put your symbol {player_symbol}? "))
        grid_location = (location_map[location][0],location_map[location][1])
        if "X" not in board[grid_location[0]][grid_location[1]] and "O" not in board[grid_location[0]][grid_location[1]]: # use not in
            if location %3 == 0:
                board = update_board(board,location_map[location][0],location_map[location][1], player_symbol)
            else:
                board = update_board(board,location_map[location][0],location_map[location][1], player_symbol+" |")
            break
        else:
            print("That space is occupied. Choose again.")
            continue
    return board
    
def check_board(board,turns):
    # rows
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2]:
            return True
    
    # columns
    for i in range(len(board[0])):
        if board[0][i] == board[1][i] == board[2][i]:
            return True
    # diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        return True
    elif board[0][2] == board[1][1] == board[2][0]:
        return True
    
    if turns == 9:
        print("Tie game")
        return True
    
    return False

def print_scores(player_info):
    print(f"Player 1: {player_info['Player 1']['score']}\nPlayer 2: {player_info['Player 2']['score']}")

def main():
    
    player_info = {
        'Player 1':{'score':0},
        'Player 2':{'score':0}
        }
    turn = 0
    game_over = False
    while True:
        symbols,board = initialize_game()
        while not game_over:
            print_board(board)
            current_symbol = symbols[turn%2]
            board = make_move(board, current_symbol)
            print_board(board)
            turn += 1
            game_over = check_board(board,turn)
            if game_over and turn == 9:
                print("Tie game")
                print_scores(player_info)
            elif game_over and turn%2 == 1:
                print("Player 1 wins!")
                player_info["Player 1"]['score'] += 1
                print_scores(player_info)
            elif game_over and turn%2 == 0:
                print("Player 2 wins")
                player_info["Player 2"]['score'] += 1
                print_scores(player_info)
            if game_over:
                play_again = input("Play again? (y/n)")
                if play_again == 'n':
                    game_over = True
                    break
                else:
                    symbols,board = initialize_game()
                    continue
        break
main()