print('Hello from constructors.py')
# constructor is a class function with double underscore
# __init__() func gets called whenever an object is created
# we can use it to initialize all variables at the time of object creation


class Employee:

  def __init__(self, name, id):
    self.name = name
    self.id = id

  def printEmpDetails(self):
    print('Emp Name: ', self.name)
    print('Emp ID: ', self.id)


emp1 = Employee('John', 1001)
emp2 = Employee('Elena', 2001)
emp1.printEmpDetails()
emp2.printEmpDetails()
