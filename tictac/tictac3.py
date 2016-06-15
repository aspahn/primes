import sys
import random
import doctest

corners = [0,2,6,8]
edges = [3,7,5,1]
center = 4
winners = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def display_board(board):

    for j in range(3):
        print(" --- "*3)
        print("| " + str(board[j*3]) + "  | " + str(board[j*3+1]) + "  | " + str(board[j*3+2])+  " | ")

def space_free(board,i):

    if board[i] != 'X' and board[i] != 'O':
        return True
    else:
        return False

def marker():

    while True:
        player_input  = raw_input("Would you like to be X's or O's? ")
        if player_input == 'X' or player_input == 'x':
            print("Very well. I will be O's.")
            return 'X','O'
        elif player_input == 'O' or player_input == 'o':
            print("Very well. I will be X's.")
            return 'O','X'
        else:
            print("Not a vaild token. Please try again.")

def player_move(board, player):

    while True:
        p = int(raw_input("Enter a number between 1-9: "))
        if p in range (1,10):
            if board[p-1] != 'X' and board[p-1] != 'O':
                board[p-1] = player
                break
            else:
                print("Oops that spot is taken. Try again.")
        else:
            print("Oops that is not a valid move. Try again.")
    display_board(board)

def check_winner(board, player, computer):

    for f,j,i  in winners:
        if board[f] == player and  board[j] == player and  board[i] == player:
            return 0
        elif board[f] == computer and board[j] == computer  and  board[i] == computer:
            return 1
    return -1

def computer_block(board, player):

    for f,j,i in winners:
        if board[f] == player and board[j] == player and space_free(board, i) == True:
            return i
        elif board[f] == player and board[i] == player and space_free(board, j) == True:
            return j
        elif board[i] == player and board[j] == player and space_free(board, f) == True:
            return f
    return -1

def computer_win(board, computer):

    for f,j,i in winners:
        if board[f] == board[j] == computer and space_free(board, i) == True:
            return i
        elif board[f] == board[i] == computer and space_free(board, j) == True:
            return j
        elif board[j] == board[i] == computer and space_free(board, f) == True:
            return f
    return -1

def computer_random(board):

    if space_free(board,center) == True:
        return center
    for i in corners:
        if space_free(board,i) == True:
            return i
    for i  in edges:
        if space_free(board,i) == True:
            return i
        else:
            return -1

def computer_move(board, computer, player):

    block = computer_block(board,player)
    win = computer_win(board,computer)
    rand = computer_random(board)
    print("Hmm...Let me think..")
    if block >=0:
        board[block] = computer
    elif win >=0:
        board[win] = computer
    elif rand >=0:
        board[rand] = computer
    else:
        print("Ahh the game has ended in a tie. Well played.")
        sys.exit()
    display_board(board)

def random_turn():

    print("To decide who will go first 1 or 0 will be randomly chosen. If the number is 0, I will go first. If the number is 1, you will go first.")
    if random.randint(0,1) == 0:
        print("The number was 0, so I will go first")
        return 1
    if random.randint(0,1) == 1:
        print("The number was 1, so you will go first")
        return 2

def main():

    print("Welcome to tic tac toe. The rules are simple: enter a number 1-9 for your move, if that spot is taken you will be prompted to enter another number. The first one to get three in a row wins. Good luck, human. You will need it.")
    player, computer = marker()
    board = [1,2,3,4,5,6,7,8,9]
    print random_turn()
    print("This is the board to begin with. You will be able to see it after every move.")
    display_board(board)
    a  = 0
    if random_turn() == 1:
        while a < 9:
            computer_move(board,computer,player)
            a+=1
            if check_winner(board,player,computer) == 0:
                print("Congrats! You have somehow managed to beat me!")
                sys.exit()
            else:
                if check_winner(board,player,computer) == 1:
                    print("Haha I have won! I knew a human wouldn't be able to beat me!") 
                    sys.exit()
            player_move(board,player)
            a+=1
            if check_winner(board,player,computer) == 0:
                print("Congrats! You have somehow managed to beat me!")
                sys.exit()
            else:
                if check_winner(board,player,computer) == 1:
                    print("Haha I have won! I knew a human wouldn't be able to beat me!")
                    sys.exit()
        print("Ahh the game has ended in a tie. Well played.")
        sys.exit()
    else:
        while a < 9:
            player_move(board,player)
            a+=1
            if check_winner(board,player,computer) == 0:
                print("Congrats! You have somehow managed to beat me!")
                sys.exit()
            else:
                if check_winner(board,player,computer) == 1:
                    print("Haha I have won! I knew a human wouldn't be able to beat me!") 
                    sys.exit()
            computer_move(board,computer,player)
            a+=1
            if check_winner(board,player,computer) == 0:
                print("Congrats! You have somehow managed to beat me!")
                sys.exit()
            else:
                if check_winner(board,player,computer) == 1:
                    print("Haha I have won! I knew a human wouldn't be able to beat me!") 
                    sys.exit()
        print("Ahh the game has ended in a tie. Well played.")
        sys.exit()

if __name__ == '__main__':
    if ("--test" in sys.argv):
        doctest.testmod(verbose=True)
        sys.exit(0)

    main()
