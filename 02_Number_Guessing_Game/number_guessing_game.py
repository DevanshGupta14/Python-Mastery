import random

print("Choose Difficulty\n")
print("1. Easy (1-50)\n2. Medium(1-100)\n3. Hard(1-500)")
while True:
    difficulty = int(input("Enter 1,2,3 from the difficulty levels: "))
    if(difficulty not in [1,2,3]):
        print("Invalid choice, enter either 1 or 2 or 3")
    else:
        break

min_number = 1
if(difficulty == 1):
    print("You have chosen easy(1-50)")
    print("You only have 5 attemps to guess correctly")
    max_number = 50
    max_attempts = 5

elif(difficulty == 2):
    print("You have chosen medium(1-100)")
    print("You only have 10 attemps to guess correctly")
    max_number = 100
    max_attempts = 10

else:
    print("You have chosen hard(1-500)")
    print("You only have 15 attemps to guess correctly")
    max_number = 500
    max_attempts = 15


random_num = random.randint(min_number,max_number)

for i in range(1,max_attempts+1):

    try:
        num = int(input(f"Enter the number between {min_number} and {max_number} : "))
    except ValueError:
        print("Enter valid number")
        continue
    
    if(num == random_num):
        print(f"Congratulations!!\nYou guessed the correct number after {i} attempts")
        print("Thanku for playing the game")
        print("\n","-"*35,"\n")
        break
    else:
        if(i==max_attempts):
            print("You have exhausted all of your attemps")
            print(f"Correct number is {random_num}")
            print("Thank u")
            break

        if (num > random_num):
            if(num - random_num <= 10):
                print("high, but nearby")
            else:
                print("Too high")
        else:
            if(random_num - num <= 10):
                print("low, but nearby")
            else:
                print("Too low")
        print("Try again")
        print(f"Attempts left = {max_attempts-i}")
    
    while True:
        choice = input("If you want to exit the game enter exit, if not enter play: ").lower()
        
        if(choice == "exit"):
            print("Thanku for playing the game")
            print("\n","-"*35,"\n")
            break
        elif(choice == "play"):
            print("Here's your next attempt")
            break
        else:
            print("Enter play or exit ONLY!!")
    
    if(choice == "exit"):
        break

    print("\n","-"*35,"\n")


