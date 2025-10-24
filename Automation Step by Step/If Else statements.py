# if..else statement
# used to create prog that makes decision
#
# if boolean_exp:
# statements

age = 10

if (age >= 18):
  print ("Eligible to drive")
else:
  print ("Not eligible to drive")

print ("I am outside if")

# elif
# if you have more than 2 options to choose from

num = 0
if (num > 0):
  print ("number is positive")
elif (num < 0):
  print ("number is negative")
else:
  print ("number is zero")

# nested if..else
# if..else statment inside another if..else

num = float(input("Enter a number : "))

if num >= 0:

  if num == 0:
    print ("Zero")
  else:
    print ("Positive")

else:
  print ("Negative")

# simple calculator

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
    print("Invalid option selected.")


