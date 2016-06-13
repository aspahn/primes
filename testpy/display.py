print("This is the board: ") 
board = [1,2,3,4,5,6,7,8,9]
for j in range(3):
   print(" --- "*3)
   print("| " + str(board[j*3]) + "  | " + str(board[j*3+1]) + "  | " + str(board[j*3+2])+  " | ")

