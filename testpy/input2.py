while True:
    player1 = raw_input("Hello, welcome to tic tac toe. Do you want to be X's or O's?: ")
    if player1 == 'X':
        print("I will be O's. You will have the first move.")
        computer = 'O';
        break
    elif player1 == 'O':
        print("I will be X's. I will have the first move.")
        computer = 'X'
        break
    else:
        print("Oops that's not a option. Please try again.")
print("This is the starting board. Are you ready to lose?")
display_board(board)
