print(' I am inside loops')

# while loop
# while boolean_exp:
# statements

a = 4
b = 1
while b <=a:
  print(' I am inside while loop ')
  b = b + 1
# 4 iterations

# Sum of natural numbers
n = 10
sum = 0
i = 1
while i <=n:
  sum = sum + i
  i = i + 1

print('Sum is: ', sum)

# while loop with else
# while loop can have an optional esle block
# else is executed when cond in while is False

i = 0
while i <=3:
  print(' I am inside loop ')
  i = i + 1
else:
  print(' I am inside else ')

# for loop

# for val in sequence:
# statements

numbers = range(1, 11)
# range is used to create sequence of numbers
sum = 0

for i in numbers:
  sum = sum + i
print(' Sum is: ', sum)

# for with else
numbers = range(1, 4)
for i in numbers:
  print(' inside for loop ')
else:
  print(' inside else ')

my_list = ['blue', 'green', 7, 8]
for item in my_list:
  print(item)
else:
  print(' items completed ')

# break continue pass
# break and continue can alter the flow
# of a normal loop

numbers = [1, 3, 6, -3, 0, 7, 10]

for i in numbers:
  if (i < 0):
    print(' value is negative')
    break
  print(i)

# continue is used to skip current iteration

i = 0
while i <= 5:
  i = i + 1
  if i == 3:
    print('i is 3')
    continue
  print('value of i is: ', i)

print('----------------')
num = [1, 3, 4, -2, 5, 7]

for val in num:
  if val < 0:
    continue
  print(val)

# pass statement
# when we have a loop or func that is not
# yet implemented

for n in [1, 2, 3, 4]:
  pass

