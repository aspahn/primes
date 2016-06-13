import sys
import random

corners = [0,2,6,8]
edges = [3,7,5,1]
center = 4
winners = [[1,2,3],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
board = [1,2,3,4,5,6,7,8,9]

def display_board(board):

    for j in range(3):
        print(" --- "*3)
        print("| " + str(board[j*3]) + "  | " + str(board[j*3+1]) + "  | " + str(board[j*3+2])+  " | ")

def space_free(board, i):

    if board[i] != 'X' and board[i] != 'O':
        return True
    else:
        return False

def board_full(board):

    for i in range(9):
        if all(board[i] == 'X' or board[i] == 'O'):
            return True
        else:
            return False


def marker():

    while True:
        player  = raw_input("Would you like to be X's or O's? ")
        if player == 'X':
             print("Very well. I will be O's.")
             return 'X', 'O' 
             break
        elif player == 'O':
             print("Very well. I will be X's.")
             return 'O', 'X'
             break
        else:
             print("Not a vaild token. Please try again.")

def player_move(board,player):

    while True:
        p = int(raw_input("Enter a number  between 1-9: "))
        if p in range (1,10):
            if board[p] != 'X' and board[p] != 'O':
                board[p-1] = player
                break
            else:
                print("Oops that spot is taken. Try again.")
        else:
            print("Oops that is not a valid move. Try again.")
    display_board(board)

def check_winner(board, winners, player, computer):
                   
    for i in winners:
        if board[winners[0]] == board[winners[1]] == board[winners[2]] == player:
            win = ("Congrats Player! You have somehow managed to beat me!")
            return win
        elif board[winners[0]] == board[winners[1]] == board[winners[2]] == computer:
            win = ("Haha I have won! I knew a puny human wouldn't be able to beat me!")
            return win
        else:
            return False

def computer_block(board, winners, player):

    for i in winners:
        if board[winners[0]] == board[winners[1]] == player and space_free(board, winners[board[2]]) == True:
            return board[winners[2]]
        elif board[winners[0]] == board[winners[2]] == player and space_free(board, winners[board[1]]) == True:
            return board[winners[1]]
        elif space_free(board, board[winners[0]]) == True and board[winners[1]] == board[winners[2]] == player:
            return boad[winners[0]]
        else:
            return False

def computer_win(board, winners, computer):

    for i in winners:
        if board[winners[0]] == board[winners[1]] == computer and space_free(board, board[winners[2]]) == True:
            return board[winners[2]]
        elif board[winners[0]] == board[winners[2]] == computer and space_free(board, board[winners[1]]) == True:
            return board[winners[1]]
        elif space_free(board, board[winners[0]]) == True  and board[winners[1]] == board[winners[2]] == computer:
            return space_free(board,0)
        else:
            return False
     
def computer_random(board, corners, center, edges):

    if space_free(board, center) == True:
        return center

    for i in corners:
        if space_free(board, corners[i]) == True:
            return i

    for i  in edges:
        if space_free(board, edges[i]) == True:
            return i

    assert(False, "Board is full")

def computer_move(board,computer):

    if computer_block(board,winners,player)  != False:
             if space_free(board, computer_block(board,winners,player)) == True:
                          board[computer_block(board,winners,player)] = computer
    elif computer_win(board,winnres,computer) != False:
             if space_free(board, computer_win(board,winners,computer)) == True:
                           board[computer_win(board,winners,computer)] = computer
    elif space_free(board, computer_random(board,corners,center,edges)) == True:
                   board[computer_random(board,corners,center,edges)] = computer
    display_board(board)
    
def random_turn():

    print("To decide who will go first 1 or 0 will be randomly chosen. If the number is 0, I will go first. If the number is 1, you will go first.")
    if random.randint(0,1) == O:
         print("The number was 0, so I will go first")
         return 1
    if random.randint(0,1) == 1:
         print("The number was 1, so you will go first")
         return 2


print("Welcome to tic tac toe. The rules are simple: enter a number 1-9 for your move, if that spot is taken you will be prompted to enter another number. The first one to get three in a row wins. Good luck, human. You will need it.")
marker()
player, computer = marker()
random_turn()
print("This is the board to begin with. You will be able to see it after every move.")
display_board(board) 
a = 0
if random_turn() == 1:
    while a < 9:
        computer_move(board,computer)
        a = a+1
        if check_winner(board,winners,computer,player) != False:
            print check_winner(board,winners,computer,player)
            sys.exit()
        else:
            if board_full(board) == True:
                print("The game has ended in a tie.")
                sys.exit()
        player_move(board,player)
        a = a+1
        if check_winner(board,winners,computer,player) != False:
            print check_winner(board,winners,computer,player)
            sys.exit()
        else:
            if board_full(board) == True:
                print("The game has ended in a tie.")
                sys.exit()
else:
    while a < 9:
        player_move(board,player)
        a = a+1
        if check_winner() != False:
            print check_winner(board,winners,computer,player)
            sys.exit()
        else:
            if board_full(board) == True:
                print("The game has ended in a tie.")
                sys.exit()
        computer_move(board,player)
        a = a+1
        if check_winner() != False:
            print check_winner(board,winners,computer,player)
            sys.exit()
        else:
            if board_full(board) == True:
                print("The game has ended in a tie.")
                sys.exit()

