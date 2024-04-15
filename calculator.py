import math
# Scientific Calculator

# Display a menu to the user for them to enter their choice

while True: 
    print("\n\t\t\tCPL Scientific Calculator")

    print("\nChoose an Operation From The Menu\n\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus\n6. Power of a number\n7. Square Root of a Number\n8. Logarithm\n9. Sin\n10. CoSine\n11. Tangent\n")
    
    # ask the user for their choice
    operation = int(input("Enter Your Choice: "))
    
    # check the user choice and perform the operation that maps to that choice
    # 1. Addition
    if operation == 1:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The sum of {num1} and {num2} is {num1 + num2}")

        
        # Ask the user to go back to the main menu
        back = input("Go back to the main menu? (Y/N): ")
        
        if back =="Y":
            continue
        else:
            break
    #2. Subtraction 
    elif operation == 2:
         num1 = float(input("Enter the first number: "))
         num2 = float(input("Enter the second number: "))
         print(f"The difference of {num1} and {num2} is {num1 - num2}")

        
         # Ask the user to go back to the main menu
         back = input("Go back to the main menu? (Y/N): ")
        
         if back =="Y":
            continue
         else:
            break
        
    #3. Multiplication 
    elif operation == 3:
         num1 = float(input("Enter the first number: "))
         num2 = float(input("Enter the second number: "))
         print(f"The multiplication of {num1} and {num2} is {num1 * num2}")

        
         # Ask the user to go back to the main menu
         back = input("Go back to the main menu? (Y/N): ")
        
         if back =="Y":
            continue
         else:
            break 
        
    #4. Division
    elif operation == 4:
         num1 = float(input("Enter the first number: "))
         num2 = float(input("Enter the second number: "))
         print(f"The division of {num1} and {num2} is {num1 / num2}")

        
         # Ask the user to go back to the main menu
         back = input("Go back to the main menu? (Y/N): ")
        
         if back =="Y":
            continue
         else:
            break
        
    #5. Modulus 
    elif operation == 5:
         num1 = float(input("Enter the first number: "))
         num2 = float(input("Enter the second number: "))
         print(f"The modulus of {num1} and {num2} is {num1 % num2}")

        
         # Ask the user to go back to the main menu
         back = input("Go back to the main menu? (Y/N): ")
        
         if back =="Y":
            continue
         else:
            break
        
    #6. Power of a number 
    elif operation == 6:
         base = int(input("Enter the base number: "))
         power = int(input("Enter the exponent/power: "))
         print(f"The power of {base}   raised to {power} is {pow(base, power)}")

        
         # Ask the user to go back to the main menu
         back = input("Go back to the main menu? (Y/N): ")
        
         if back =="Y":
            continue
         else:
            break   
        
