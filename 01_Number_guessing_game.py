import math
import random


lower = int(input("Enter lower bound:"))
upper = int(input("Enter upper bound:"))

x = random.randint(lower,upper)
print("\nYou have only ",round(math.log(upper-lower+1,2))," chances to guess the integer!\n")

count = 0

while count<math.log(upper-lower+1,2):
    count+=1
    guess = int(input("Enter your guess:"))

    if x==guess:
        print("You did it in ",count, " try")
        break
    elif x>guess:
        print("You guess to small")
    elif x<guess:
        print("You guess to big")
    
if count>=math.log(upper-lower+1,2):
    print("\n The number is %d"%x)
    print("\tBetter luck next time!")