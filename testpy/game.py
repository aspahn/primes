import random

def player_move(board):
     
    p = int(raw_input("Human what is your move?: ")
    while True:
      if p not in range(0,10):
             print("Oops invalid move. Please try again.")
      elif board[p-1] != 'X' and board[p1-1] != 'O':
             if player(z) == 1:   
                   board[p-1] = 'X'
             else:
                   board[p-1] = 'O'
             break
      elif:
             print("Oops that spot is already taken. Please try again.")


def computer_move(board):
while z == 2:
   if y == 0:
      print("Hmmm... let me think")
      board[4] = 'X'
      break

       

def scenario1(board,y):

  if y == 2:
      if board[3] == 'O':
            print("Hmmm... let me think")
            board[8] = 'X'
            break
      if board[5] == 'O':
            print("Hmmm... let me think")
            board[6] = 'X'
            break
  elif y == 4:
       if board[0] == 'O':
            print("Hmmm... let me think")
            board[6] = 'X'
            break
       if board[2] == 'O':
            print("Hmmm... let me think")
            board[8] =='0'
            break
  elif y == 6:
       if board[7] == 'O':
            print("Hmmm... let me think")
            if board[0] != '0':
               board[0] = 'X'
               break
            else:
               board[2] = 'X'
               break
       else:
            print("Hmmm... let me think")
            board[7] = 'X'
            break

def scenario2(board, y)
  
  if y == 2:
      if board[6] == 'O':
          print("Hmmm... let me think")
          board[2] = 'X'
          break
      elif board[0] == 'O':
          print("Hmmm... let me think")
          board[8] = 'X'
          break
      elif board[2] == 'O':
          print("Hmmm... let me think")
          board[6] = 'O'
          break
      elif board[8] == 'O':
          print("Hmmm... let me think")
          board[0] = 'X'
          break
  elif y == 4:
      if board[3] == 'O':
          print("Hmmm... let me think")
          board[0] = 'X'
          break
      if board[5] == 'O':
          print("Hmmm... let me think")
          board[2] = 'X'
          break
      if board[1] == 'O':
          if board[6] == 'O':
                print("Hmmm... let me think")
                board[8] = 'X'
                break
          elif board[8] == 'O':
                print("Hmmm... let me think")
                board[6] = 'X'
                break
  elif y == 6:
      if board[6] == 'O' and board[8] == '0':
          print("Hmmm... let me think")
          board[1] = 'X'
          break
      if board[6] == 'O' and board[1] == 'O':
          print("Hmmm... let me think")
          board[8] = 'X'
          break
      if board[8] == 'O' and board[1] == 'O':
          print("Hmmm... let me think")
          board[6] = 'X'
          break

                   
                

    





board = [1,2,3,4,5,6,7,8,9]
