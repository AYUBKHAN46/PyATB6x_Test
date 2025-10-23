print('Hello from lists.py')
# list - store list of items
# created by putting items inside square brackets []

list1 = []  # empyt list
numbers = [1, 2, 3, 4]  # list of integers
colors = ['red', 'blue', 'green']  # list of strings
mixed_list = [1, 2, 3.8, 'red']

print(mixed_list)

# a list can have another list as its item
my_list = ['python', 'java', [1, 2, 3], 'raghav']

# access elements from a list

numbers = [1, 2, 3, 4, 5]
print(numbers)
print(numbers[2])
print(numbers[4])  # error index out of range
print(numbers[-1])  # last element
print(numbers[-2])  # 2nd last element

# slicing list
print(numbers[2:5])  # 3rd to 5th element
print(numbers[2:])  # 3rd to last
print(numbers[:-2])  # beginning to 3rd
print(numbers[:])  # beginning to end

# lists are mutable - items can be changed
my_colors = ['blue', 'green', 'red', 'yellow']
print(my_colors)
my_colors[2] = 'pink'
print(my_colors)

my_colors[1:3] = ['orange', 'purple']  # 2nd to 3rd item
print(my_colors)

# add items to a list
numbers = [1, 2, 3, 4]
print(numbers)
numbers.append(5)
print(numbers)
numbers.extend([6, 7, 8])
print(numbers)

# combine lists using +
print(numbers + [9, 10])
# repeat items using *
print(numbers * 3)

# insert items at a desired location insert()
numbers.insert(2, 2.5)
print(numbers)

# delete items - del
del numbers[2]  # delete the 3rd item
print(numbers)
del numbers[2:4]  # delete multiple items
print(numbers)
del numbers
print(numbers)  # error - list not defined

print('----------------------')

numbers = [1, 2, 3, 4, 5]
numbers.remove(1)  # remove item 1
print(numbers)
numbers.pop(2)  # pop item at index position 2
print(numbers)
numbers.pop()  # pop last item
print(numbers)
numbers.clear()  # clear the list
print(numbers)
print('-------------')
# copy list =
list1 = [1, 2, 3]
list2 = list1
print(list2)

list1 = [1, 2, 3]
list2 = list1.copy()
print(list2)

# Loop through a list
fruits = ['apple', 'banana', 'grapes', 'strawberry']

for item in fruits:
  print(item)

# check item in list
print('apple' in fruits)
print('orange' in fruits)

# nested lists
my_list = [1, 2, 3, [1.0, 2.0, 3.0]]
print(my_list[3][1])