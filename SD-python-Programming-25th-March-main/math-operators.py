# Python 3 Numbers - Math operators

# Python defines three numerical types namely:
#  -> Integers 
#  -> Floating point numbers
#  -> Complex numbers

# The complex numbers are usually used in some advance math operations and are not off great interest for our current needs. Instead we will work more with integers and floating point numbers and thats why we will focus in these numerical types and their corresponding operators and functions

# Lets define a variable and assign it an integer and another variable associated with a floating point number, or float.

# Consider the following variables 
num1 = 10
num2 = 2.51

# check the type of this variables -> Python provides the type function of this
print(type(num1))  # returns  <class 'int'>
print(type(num2))  #returns <class 'float'>

# Lets see what operatorions we are able to perform using integers and floating point numbers

#1. Arithmetic operators
x = 20
y = 6

# 1. Addition -> '+'
print(x + y)
# 2. Subtraction -> '-'
print(x - y)
# 3. Multiplication -> '*'
print(x * y)
# 4. Division -> '/'
print(x/y)
# 5. Integer division -> '//' (returns the integer from a division)
print(x//y)
# 6. Modulo -> '%' (this means finding out the remainder after the division of one number by another)
print(x % y)
# 7. Raising to a power -> '**'
print(x ** y)


print("==================")

# Challenge time 
# write a python program that asks the user for the radius of a circle and then returns the perimeter and area of the circle


# declare PI
PI = 22 / 7
# Prompt user to input the circle
radius = float(input("Please enter the radius: "))

perimeter = PI * (radius + radius)
area = PI * (radius * radius)

# output the area and perimeter
print(f"The perimeter and the area of a circle whose radius is {radius}cm, is {perimeter}cm and {area}cm\u00b2  respectively")

#2.  Comparison operators ->  used to compare values and return boolean values(True or false)
a = 20
b = 6

# less than -> '<'
print(a < b)
# greater than -> '>'
print(a > b)
# less than  or equal to-> '<='
print(a <= b)
# greater than or equal to -> '>='
print(a >= b)
# equal to -> '=='
print(a == b)
# not equal to -> '!='
print(a != b)


# Order of evaluation in python

# Lets talk about the order of evaluation of these operators inside a mathematical expression
# What if we have to deal with multiple operators within the same expression? which operations priority over

# well the order is as follows:
# 1, Firstly the raisng to a power has the highest priority
# 2. then we have multiplication, division and modulo operations with equal priorities 
# 3. addition and subtraction also with equal priorities

# Lets see an example
# 100 - 5 ** 2 / 5 * 2 = 90

# Conversions
# Lets see how we can convert an integer to a float and vice versa
# Well, Python has two functions available for these operations. Lets see them

print(int(1.7)) # returns 1 (truncation)
print(int(19.9999)) # returns 19( truncation)
# The result is one because the int() function will round down the number in between the parentheses to the nearest integer, which is 1.

print(float(2)) #returns 2.0
# The result is 2.0. The float() function will add 0, converting 2 from integer to a floating point number

# Finally, lets have a look at a few functions which may come in handy in the future when working with numbers

# 1. abs() : returns the absolute value .This is actually the distance between the number that we provide and zero
print(abs(5)) # returns 5
print(abs(-15)) #returns 15

# 2. max()
# returns the largest number between 2 numbers
print(max(2, 10)) #returns 10

# 3. min() : returns the smallest number between 2 numbers
print(min(2, 10)) #returns 2

# 4. pow() : another way of raising a number to a power using built in python function
# e.g pow(a, b) where a is the base number and b is the exponent
print(pow(10, 3))  #returns 1000
      
# Challenge time
# write a python program that prompts the user to enter their name and age. The program will the output the decades the minutes the user has used. Print out the results in a nice format
# (A decade is a period of 10 years e.g 22 years old -> 2 decades)

# Prompt user to enter name
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

# convert age into decades
decade = age // 10

# convert age into minutes
minutes = age * 365 * 0.25 * 24 * 60

# output the age in decades and minutes
print(f"Hello, {name}, you have lived for {decade} decade(s), and have {minutes} minutes  which means you are {age} years old")