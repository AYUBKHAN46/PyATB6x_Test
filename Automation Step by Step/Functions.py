print("Hello from functions")

# a block of code which runs only when called
# we can pass data to a func - parameters
# func can return data as result

# def func_name(parameters):
# statements


def hello(name):
  print("Hello", name)


hello("Python")
hello("Eric")

# func to add 2 numbers


def add(num1, num2):
  return (num1 + num2)


print(add(2, 4))
print(add(5, 6))

# Built-in functions
# print(), input(), range()

# variables

x = 10


def my_func():
  x = 5
  print('value of x inside func is: ', x)


my_func()
print('value of x outside func is: ', x)

# Arguments (Parameters)


def hello(name, msg):
  print("Hello", name + ', ' + msg)


hello("Python", "Good Morning")

# default arguments


def hello(name, msg="How are you"):
  print("Hello", name + ', ' + msg)


hello("Python", "Great to see you")


# Positional arguments
def hello(name, msg):
  print("Hello", name + ', ' + msg)


hello("Eric", "Good Evening")
hello(msg="How are you", name="Elvis")

# Arbitrary arguments
# when we are not sure about the num of arguments


def hello(*names):
  print("Hello", names)


hello('Eric', "Monica", "Elvis")

# Anonymous func | Lambda functions
# we can define a func without a name
#
# lambda arguments: expression

sum = lambda a, b, c: a + b + c
print(sum(2, 3, 4))

# Recursive functions
# a func can call other func and also itself
# a func that calls itself - recursive func
# procees - recusrsion
#
# prog to find sum of natural numbers
# 1+2+3+..n


def calculate_sum(n):
  if n == 1:
    return 1
  else:
    return n + calculate_sum(n - 1)


sum = calculate_sum(10)
print(sum)