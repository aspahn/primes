import sys

def player():
    z = 0
    while True:
        player1 = raw_input("Hello, welcome to tic tac toe. Do you want to be X's or O's?: ")
        if player1 == 'X' or 'x':
            print("I will be O's. You will have the first move.")
            computer = 'O';
            z = 1
            break
        elif player1 == 'O' or 'o':
            print("I will be X's. I will have the first move.")
            computer = 'X'
            z = 2
            break
        else:
            print("Oops that's not a option. Please try again.")
    print("This is the starting board. Are you ready to lose?")
    display_board(board)
    return z


def display_board(board):

    for j in range(3):
        print(" --- "*3)
        print("| " + str(board[j*3]) + "  | " + str(board[j*3+1]) + "  | " + str(board[j*3+2])+  " | ")


def get_input(board, y):
    while 1 :
        if y%2 == 0 and player() == 1:
            p1 = int(raw_input("Human enter your move: "))
            if p1 not in range(0,10):
                print("Sorry that is not an acceptable move. Please enter a number between 1 and 9.")
            if board[p1-1]!= 'X' and board[p1-1]!= 'O':
                board[p1-1] = 'X'
                break
        elif: y%2 == 0 and player() == 2:
        elif: y%2 != 0 and player() == 1:
        elif: y%2 != 0 and player() == 2:
            p2 = int(raw_input("Human enter your move: "))
            if p2 not in range(0,10):
                print("Sorry that is not an acceptable move. Please enter a number between 1 and 9.")
            if board[p2-1] != 'X' and board[p2-1] != 'O':
                board[p2-1] =  'O'

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
#print("This is the starting board: ")
#display_board(board)
#print("Player1 you are X's. Player2 you are O's. Player1 you will go first.")
#y = 0
#while check_winner(board) != 1 and y<9:
 #   get_input(board, y)
  #  check_winner(board)
#if check_winner(board) == 1:
 #       print("Congrats Player1! You have won. The game is now over.")
  #      sys.exit()
#elif check_winner(board) == 2:
 #       print("Congrats Player2! You have won. The game is now over.")
  #      sys.exit()
   # y = y+1
#print("It's a tie! the game is now over.")

player()
