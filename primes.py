num = int(raw__input("Please enter a number: "))
for i in range(2, num):
      if num % i == 0:
         print(str(num) + " is not a prime number")
         break
      else:
         print(str(num) + " is a prime number")
         break  
