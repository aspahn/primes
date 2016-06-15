import sys
import random
import doctest

class TicTacToe:

    corners = [0,2,6,8]
    edges = [3,7,5,1]
    center = 4
    winners = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    def __init__(self):

        self.board = [1,2,3,4,5,6,7,8,9]

    def display_board(self):

        for j in range(3):
            print(" --- "*3)
            print("| " + str(self.board[j*3]) + "  | " + str(self.board[j*3+1]) + "  | " + str(self.board[j*3+2])+  " | ")

    def space_free(self,i):

        if self.board[i] != 'X' and self.board[i] != 'O':
            return True
        else:
            return False

    def marker(self):

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

    def player_move(self, player):

        while True:
            p = int(raw_input("Enter a number between 1-9: "))
            if p in range (1,10):
                if self.board[p-1] != 'X' and self.board[p-1] != 'O':
                    self.board[p-1] = player
                    break
                else:
                    print("Oops that spot is taken. Try again.")
            else:
                print("Oops that is not a valid move. Try again.")
        self.display_board()

    def check_winner(self, player, computer):

        for f,j,i  in TicTacToe.winners:
            if self.board[f] == player and  self.board[j] == player and  self.board[i] == player:
                return 0
            elif self.board[f] == computer and self.board[j] == computer  and  self.board[i] == computer:
                return 1
        return -1

    def computer_block(self, player):

        for f,j,i in TicTacToe.winners:
            if self.board[f] == player and self.board[j] == player and self.space_free(i) == True:
                return i
            elif self.board[f] == player and self.board[i] == player and self.space_free(j) == True:
                return j
            elif self.board[i] == player and self.board[j] == player and self.space_free(f) == True:
                return f
        return -1

    def computer_win(self, computer):

        for f,j,i in TicTacToe.winners:
            if self.board[f]== computer and self. board[j] == computer and self.space_free(i) == True:
                return i
            elif self.board[f] == computer and self.board[i] == computer and self.space_free(j) == True:
                return j
            elif self.board[j] == computer and self.board[i] == computer and self.space_free(f) == True:
                return f
        return -1

    def computer_random(self):

        if self.space_free(TicTacToe.center) == True:
            return TicTacToe.center
        for i in TicTacToe.corners:
            if self.space_free(i) == True:
                return i
        for i  in TicTacToe.edges:
            if self.space_free(i) == True:
                return i
            else:
                return -1

    def computer_move(self, computer, player):

        block = self.computer_block(player)
        win = self.computer_win(computer)
        rand = self.computer_random()
        print("Hmm...Let me think..")
        if block >=0:
            self.board[block] = computer
        elif win >=0:
            self.board[win] = computer
        elif rand >=0:
            self.board[rand] = computer
        self.display_board()

    def random_turn():

        print("To decide who will go first 1 or 0 will be randomly chosen. If the number is 0, I will go first. If the number is 1, you will go first.")
        if random.randint(0,1) == 0:
            print("The number was 0, so I will go first")
            return 1
        if random.randint(0,1) == 1:
            print("The number was 1, so you will go first")
            return 2

    def play(self):

        print("Welcome to tic tac toe.  \nThe rules are simple: enter a number 1-9 for your move,if that spot is taken you will be prompted to enter another numb\
er.  \nThe first one to get three in a row wins. Good luck, human. You will need it.")
        while 1:
            self.board = [1,2,3,4,5,6,7,8,9]
            player, computer = self.marker()
            print("This is the board to begin with. You will be able to see it after every move.")
            self.display_board()
            a  = 0
            if self.random_turn  == 1:
                while 1:
                    self.computer_move(computer,player)
                    if self.check_winner(player,computer) == 1:
                        print("Haha I have won! I knew a human wouldn't be able to beat me!")
                        break
                a +=1
                if a > 8:
                    print("Ahh the game has ended in a tie. Well played.")
                    break
                self. player_move(player)
                if self.check_winner(player,computer) == 0:
                    print("Congrats! You have somehow managed to beat me!")
                    break
                a +=1
            else:
                while 1:
                    self.computer_move(computer,player)
                    if self.check_winner(player,computer) == 1:
                        print("Haha I have won! I knew a human wouldn't be able to beat me!")
                        break
                    a +=1
                    if a > 8:
                        print("Ahh the game has ended in a tie. Well played.")
                        break
                    self. player_move(player)
                    if self.check_winner(player,computer) == 0:
                        print("Congrats! You have somehow managed to beat me!")
                        break
                    a +=1
            play_again = raw_input("Would you like to play again? Please enter Y or N: ").upper()
            if play_again != 'Y':
                sys.exit()

t = TicTacToe()
t.play()
