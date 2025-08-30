import numpy as np

board = np.full((3,3)," ")

def display_board(board):
    print("\n")
    for row in board:
        print("|".join(row))
        print("-"*5)
        
def check_winner(board,player):
    for i in range(3):
        if np.all(board[i,:] == player) or np.all(board[:,i] == player):
            return True
    if (board[0,0] == board[1,1] == board[2,2] == player) or (board[0,2] == board[1,1] == board[2,0] == player):
            return True
    return False
    
def is_draw(board):
    return np.all(board !=" ")

def play_game():
    current_player = 'X'
    while True:
        display_board(board)
        try:
            row = int(input("Enter row (0-2)"))
            column = int(input("Enter column (0-2)"))
            
        except ValueError:
           print("Invalid input try entering between 0-2") 
           continue
        
        if 0<=row<=2 and 0<=column<=2:
            if board[row,column] == " ":
                board[row,column] = current_player
                
                
                if check_winner(board,current_player):
                 display_board(board)
                 print(f"Player {current_player} wins")
                 break
             
                elif is_draw(board):
                  display_board(board)
                  print("It is a draw")
                  break
                current_player = "O" if current_player == "X" else "X"
                
            else:
                print("Cell already taken")
        else:
            print("Please enter valid input")
            
play_game()
                