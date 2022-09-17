from mimetypes import guess_all_extensions
import random
import math
# input from user
print("::::::::::Wellcome Guessing Game Try It::::::::::::")
lower = int(input("Enter lower bound : "))
upper = int(input("Enter upper bound : "))

# taking random value between l and u by user
x = random.randint(lower,upper)
print("\n\t You've only ", round(math.log(upper-lower+1,2)),"Chance to guess the integer !\n" )
# intizilizing the number of guessinf
i = 0
while i<math.log(upper-lower+1,2):
    i +=1
    # guess number by user
    guess = int(input("Guess a Number : "))
    if x == guess:
        print("Congratulations you did it in ", i , " try ")
        break
    elif x > guess:
        print("Too small !")
    elif x < guess:
        print("Too high !")
        
if i>=math.log(upper-lower+1,2):
    print("\n The number is %d "%x)
    print("\t Better Luck Next Time !")
    

