#print -- Comment # symbol is used
#print()
print("Hello World")

a=7
b=8
print(a,b)
print(a+b)
print(a-b)

name = "Ayub"
print(name)
print("Name:",name)

print("Name:",name.upper())
print("Name:",name.lower())

print("First Line \n\n")
print("Second Line \n\n")


#input statement

name = input("Enter your name: ")
print(name)
print(type(name))

#Variables - Used to store data/values

a=10
b=1.1
#In python the value entered later is considered so here a=7 will be stored and variables
#cannot use keywords like if,else,try,catch for naming
a=7
first_name = 'Ayub'
print(first_name)

#Literals - In above example 10,1.1,Ayub are all literals
#Literals can be numeric, string, boolean
#Eg of numeric 10,0,-10
#Eg of String name = "Python"/char='P'
#Eg of Boolean a = True and b = False, these cannot be inside strings


#Strings
name = "Python"
char='P'
multiline_string = """""
name: Ayub
subject :Python
job: Engineering
 """
print(multiline_string)


# Type Conversion
#implicit and explicit type conversion in

num_int = 5
print(type(num_int))
num_float = 3.14
sum = num_int+num_float
print(sum)
print(type(sum))

# Explicit Type conversion
# int()
# float()
# str()

a = '77'
int_num = int(a)
print(int_num)
print(type(int_num))

num_float = float(a)
print(num_float)
print(type(num_float))









