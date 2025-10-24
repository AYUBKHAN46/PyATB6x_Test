print('Hello from classes_objects.py')
# Creating Class
class MyClass1:
  # attributes (data and functions)
  pass


class MyClass:
  a = 10

  def func1(self):
    print('Hello')


# Creating Objects
# to access attributes of a class
obj = MyClass()
obj.func1()
print(obj.a)

# we can create multiple objects from a class
obj1 = MyClass()
obj2 = MyClass()

print(obj1.a)
print(obj2.a)

obj1.a = 20
obj2.a = 30

print(obj1.a)
print(obj2.a)

# Python is Object Oriented prog language
# Classes and Objects
# Class is a collection of data and functions
# Object is an instance of a class
# Class is a blueprint for an object


class MyClass2:
  a = 10

  def hello(self):
    print('Hello World')


print(MyClass2.a)


class Calculate:

  def add(self, num1, num2):
    return num1 + num2

  def multipy(self, num1, num2):
    return num1 * num2


cal1 = Calculate()
print(cal1.add(2, 3))
print(cal1.multipy(3, 4))