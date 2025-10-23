num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
choice = int(input("Select your option 1. Addition 2. Subtraction 3. Multiplication 4. Division: "))

if choice == 1:
    result = num1 + num2
    print("The result is", result)
elif choice == 2:
    result = num1 - num2
    print("The result is", result)
elif choice == 3:
    result = num1 * num2
    print("The result is", result)
elif choice == 4:
    if num2 != 0:
        result = num1 / num2
        print("The result is", result)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid Option Selected.")