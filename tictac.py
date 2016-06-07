import sys

def display_board(board):

    for j in range(3):
        print(" --- "*3)
        print("| " + str(board[j*3]) + "  | " + str(board[j*3+1]) + "  | " + str(board[j*3+2])+  " | ")

    
def get_input(board, y):
    while 1 :
        player = int(raw_input("Player please enter your move: "))
        if player not in range(0,10):
            print("Sorry that is not an acceptable move. Please enter a number between 1 and 9")   
        if board[player-1]!= 'X' and board[player-1]!= 'O':
            if y%2 == 0:
                board[player-1] = 'X'
            if y%2 != 0:
                board[player-1] = 'O'
            break
        else:
            print("Oops that spot is taken. Try another move")
    print("This is the board after your move: ")
    display_board(board) 

def check_winner(board):

   z = 0 
   for c in range(0,3):
       if board[c*3] == 'X' and board[c*3+1] == 'X' and board[c*3+2] == 'X':
           z = 1
       elif board[c] == 'x' and board[c+3] == 'X' and board[c+6] == 'X':
           z = 1
   if  board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
       z = 1
   if board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
       z = 1
   for c in range(0,3):
       if board[c*3] == 'O' and board[c*3+1] == 'O' and board[c*3+2] == 'O':
           z = 2
       elif board[c] == 'O' and board[c+3] == 'O' and board[c+6] == 'O':
           z = 2
   if board[0]== 'O' and board[4] == 'O' and board[8] == 'O':
       z = 2
   if board[2]== 'O' and board[4] == 'O' and board[6] == 'O':
    z = 2
   return z 

board = [1,2,3,4,5,6,7,8,9]
print("This is the starting board: ")
display_board(board)
print("Player1 you are X's. Player2 you are O's. Player1 you will go first.")
y = 0  
while check_winner(board) != 1 and y<9:
    get_input(board, y)
    check_winner(board)
    if check_winner(board) == 1:
        print("Congrats Player1! You have won. The game is now over.")
        sys.exit()
    elif check_winner(board) == 2:
        print("Congrats Player2! You have won. The game is now over.")
        sys.exit()
    y = y+1
print("It's a tie! the game is now over.")

