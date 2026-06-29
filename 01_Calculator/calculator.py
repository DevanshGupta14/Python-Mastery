

while True:
    
    op = input("Enter +,-,*,/ or exit for exiting: ").lower()
    if(op == "exit"):
        print("Thanku for using calculator")
        break

    try:
        num1 = float(input("Enter first no.: "))
        num2 = float(input("Enter second no.: "))
    except ValueError:
        print("Enter valid numbers")
        continue

    if(op == "+"):
        print(f"\nSum is {num1 + num2}")
    elif(op == "-"):
        print(f"\nDifference is {num1 - num2}")
    elif(op == "*"):
        print(f"\nProduct is {num1 * num2}")
    elif(op == "/"):
        if(num2 == 0.0):
            print("\nSecond number can't be zero")
        else:
            print(f"\nDivision is {num1/num2}")
    else:
        print("\nInvalid operator")
    
    print("\n","-"*35,"\n")




