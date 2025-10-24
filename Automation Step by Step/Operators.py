# Operators - Symbols that allow mathematical or logical operations
from math import remainder

from src.LearningPython import first_name

a = 5
b =10
sum = a + b
print(sum)

# Arithemetic Operators +, -,*,/,%

a=1
b=2
c=3
sum = a + b + c
print("Sum is:",sum)

# + with strings will concatenate
first_name  = 'Ayub'
last_name = 'Khan'
name = first_name + ' ' + last_name
print("Name is",name)

# *Operator
a =5
b=1.6
result = a * b
print(result)

# *can also be used to repeat string

a="Python"
b=3
result = a*b
print(result,'->',a)

# / and //

result = 17/2
print(result)

# // prints quotient
result = 17//2
print(result)

# % gives remainder()
result = 17%2
print(result)

# ** Operator
# Left operand is raised to the power of right operand
result = 2**3
print(result)
