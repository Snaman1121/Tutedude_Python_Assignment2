# Task 1: Even or Odd Checker

# 1. Takes an integer input from the user

try:
    number = int(input("Enter an integer: "))
    
    # 2.Checks whether the number is even or odd
    # A number is even if it is divisible by 2 with no remainder

    if number % 2 == 0:
    # 3. Displays the result
        print(f"{number} is an even number.")
    
    # 3. Displays the result
    else:
        print(f"{number} is an odd number.")

except ValueError:
    print("Invalid input. Please enter a valid integer.")