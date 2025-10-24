print("Hello from tuples.py")

# tuple is similar to a list
# unlike lists, elements once assigned to a tuple
# cannot be changed
# elements are placed inside parenthesis ()

my_tuple1 = ()  # empty tuple
my_tuple2 = (1, 2, 3, 4)  # integers
my_tuple3 = (1, 2, "red", "green", 3.4)  # mixed
my_tuple4 = (1, 2, ('apple', 'banana'), 3, 4)  # nested tuple
my_tuple5 = (1, 2, ['python', 'java'])
print(my_tuple1)

# one item in a tuple
t1 = ('Python')
print(type(t1))
t2 = ("Java", )
print(type(t2))

# Accessing tuple elements
t1 = ('a', 'b', 'c', 'd')
print(t1[0])
print(t1[2])

# Negative indexing
print(t1[-1])  # last item
print(t1[-2])  # 2nd last item

# Slicing to access range of elements
# slicing operator :
my_tuple = ('H', 'e', 'l', 'l', 'o')
print(my_tuple[1:4])  # 2nd to 4th element
print(my_tuple[:-3])  # beginning to 2nd
print(my_tuple[2:])  # 3rd to end
print(my_tuple[:])  # start to end

# Changing element of a tuple
# tuples are immutable - elements cannot be changed
# However if tuple contains mutable elements like lists, they can be changed
my_tuple = (1, 2, 3, ['h', 'e', 'l', 'l', 'o'])
print(my_tuple)
my_tuple[3][3] = 'o'
print(my_tuple)

# + and *
# concatenate tuples using +
# repeat tuple items using *
my_tuple = (1, 2, 3)
print(my_tuple + (4, 5, 6))
print(my_tuple * 3)

# Looping throught a tuple

for item in my_tuple:
  print(item)

# Deleting a tuple
# we cannot delete items in a tuple
# we can delete the tuple itself
del my_tuple
print(my_tuple)