import sys

for p in range(int(sys.argv[1]), int(sys.argv[2])):
     for i in range(2, p):
            if p %  i == 0:
               print(str(p) + " is not a prime number")
               break
            else:
               print(str(p) + " is a prime number")
               break  
