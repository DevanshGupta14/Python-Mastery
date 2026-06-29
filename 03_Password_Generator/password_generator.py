import random
import string

# Asking ofpassword length
while True:
    try:
        pass_length = int(input("Enter the length of password: "))
    except ValueError:
        print("Invalid input, Enter natural numbers")
        continue
    
    if(pass_length < 8 and pass_length > 0):
        print("Too small! Increase the length")
    elif(pass_length == 0):
        print("Length of the password can't be zero")
    elif(pass_length < 0):
        print("Length of the pssword can't be negative")
    elif(pass_length > 25):
        print("Too big! Decrease the length")
    else:
        print(f"You have chosen the length of password to be {pass_length}")
        break

# Innclusion of letters
print("Answer in y(Yes) or n(NO)")
while True:
    cap_letter = input("Do you want to use capital alphabets (y/n): ").lower()
    small_letter = input("Do you want to use small alphabets (y/n): ").lower()
    numbers = input("Do you want to use numbers (y/n): ").lower()
    symbols = input("Do you want to use symbols (y/n): ").lower()

    if(cap_letter not in ["y","n"] or small_letter not in ["y","n"] or numbers not in ["y","n"] or symbols not in ["y","n"]):
        print("Invalid input\nEnter y or n only!")

    elif(cap_letter == "n" and small_letter == "n" and numbers == "n" and symbols == "n"):
        print("Invalid input\nAll of them can't be n (one has to be y)")
    else:
        break

print("Generating the password .....")
while True:

    character = ""
    if(cap_letter == "y"):
        character += string.ascii_uppercase
    if(small_letter == "y"):
        character += string.ascii_lowercase
    if(numbers == "y"):
        character += string.digits
    if(symbols == "y"):
        character += string.punctuation 

    random_pass = ''.join(random.choice(character)for _ in range(pass_length))
    print(f"Generated password is {random_pass}")

    while True:
        new_random_pass = input("Do you want to generate new password (y/n): ").lower()
        if(new_random_pass not in ["y","n"]):
            print("Invalid input!!\nEnter y or n only")
        else:
            break

    if(new_random_pass == "n"):
        print(f"Thanku for your trust, here is your password : {random_pass}")
        print("Please choose our service again")
        break
    else:
        print("Generating new password ....")


