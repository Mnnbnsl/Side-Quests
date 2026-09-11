def print_board(board) :
    for row in board:
        for cell in row:
            print(cell, end = " ")
        print()

# as cells are 9 so max depth = 9

INF = 1e3
player, opponent = 'O', 'X'

def is_moves_left(board) :
    for row in board:
        for cell in row:
            if cell == '.':
                return True 

    return False

def eval(board) :
    # check for row
    for row in range(3):
        if (board[row][0] != '.' and board[row][0] == board[row][1] and board[row][1] == board[row][2]) :
            if (board[row][0] == player) :
                return 10
            else :
                return -10
        
    # check for column
    for col in range(3):
        if (board[0][col] != '.' and board[0][col] == board[1][col] and board[1][col] == board[2][col]) :
            if (board[0][col] == player) :
                return 10
            else :
                return -10

    # check for diagonal
    if (board[1][1] != '.' and board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        if (board[0][0] == player) :
            return 10
        else :
            return -10
    if (board[1][1] != '.' and board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        if (board[0][2] == player) :
            return 10
        else :
            return -10

    return 0

def minimax(board, is_max):
    score = eval(board)
    # return score if game complete
    if (score != 0) :
        return score 
    
    # return 0 if no moves left
    if (not is_moves_left(board)):
        return 0
    
    if is_max: # player's turn 
        score = -INF 
        for i in range(3):
            for j in range(3):
                if board[i][j] == '.':
                    board[i][j] = player
                    score = max(score, minimax(board, not is_max))
                    board[i][j] = '.'

        return score 

    else : # computer's turn
        score = INF
        for i in range(3):
            for j in range(3):
                if board[i][j] == '.':
                    board[i][j] = opponent
                    score = min(score, minimax(board, not is_max))
                    board[i][j] = '.'
        
        return score

def find_best_move(board, turn) :
    best_i, best_j = -1, -1
    if turn == player :
        score = -INF    
        for i in range(3) :
            for j in range(3):
                if board[i][j] == '.':
                    board[i][j] = player
                    cur = minimax(board, False)

                    board[i][j] = '.'
                    if cur > score :
                        score = cur 
                        best_i = i 
                        best_j = j 
    
    else :
        score = INF 
        for i in range(3) :
            for j in range(3):
                if board[i][j] == '.':
                    board[i][j] = opponent
                    
                    cur = minimax(board, True)

                    board[i][j] = '.'
                    if cur < score :
                        score = cur 
                        best_i = i 
                        best_j = j 

    return (best_i, best_j)

def play_game() :
    # start with an empty board
    board = [['.', '.', '.'] for _ in range(3)]

    # first turn of human
    turn = player 
    turns_played = 0
    is_game_complete = False
    while turns_played < 9:
        print(f"Move played by {'Human' if turn == player else 'Computer'}")
        if turn == player :
            print("Enter coordinates of move : ")
            i = int(input())
            j = int(input())
            if 0 <= i < 3 and 0 <= j < 3 and board[i][j] == '.':
                board[i][j] = turn 
                turn = opponent # flip turn
                turns_played += 1
            else :
                print("Enter Correct Move.")


        else :
            i, j = find_best_move(board, turn)
            board[i][j] = turn
            turn = player 
            turns_played += 1
        score = eval(board)
        print_board(board) 
        if score == 10 :
            print("HUMAN WON!")
            is_game_complete = True
            break 
        elif score == -10 :
            print("COMPUTER WON!")
            is_game_complete = True
            break
    
    if (not is_game_complete) :
        print("GAME IS DRAWED")

play_game()