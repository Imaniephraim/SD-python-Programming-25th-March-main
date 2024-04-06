# Python 3 - variable

# what is a variable How to define a variable and what it is good for

# A variable is nothing more than just a reserved location in computer's memory, used to store information - values to be precise

# This means that when we create a variable you reserve some space in memory.

# You can store different types of data using a variable - you can store a string number, a list or any other data type you can think of.

# unlike other programming languages, in python you don't have to expicitly declare a variable instead the declaration is done automatically when you assign a value to that variable, no matter what type of data you decide to assign to that memory location

# e.g String username = "Dennis"; in a language like java 
# in python => username = "Dennis"

# Furthermore, you can later access the value referenced by that variable and use it in other areas of your python application.

# Lets think of how you should properly name a variable in python 

# There are several rules to consider and follow for a clean and compliant code and also for avoiding any conflict with Python's in-built names 

# First, a variable name should always start with a letter, usually lowercase and never start with a number or symbol. However, there is an exception to this rule - some variable names start with an underscore '_' or double underscore '__', but these are python specific structures

# The variable name may contain lowercase or uppercase letters, numbers, and the underscore but not as the first character.

# Also don't include spaces or any other special characters inside variable names -> this means no dollar signs,commas,parenthesis,question marks e.t.c

# REMEMBER Python name are case sensitive so a variable name 'my_Var' is a different variable from 'my_var' , with a lowercase 'v'
# Age != age != AGE

# Furhermore, variables and variable names should have a considerable length, for easy remembrance and reference in code.

# The last thing on variables, is that there are some python reservered names which can't be used as variables ex:def, while, for, if, list, str

# Lets see how to assign a value to a variable

# The rule is to use the "=" sign -> This should be regarded as an assignment operator, rather than the usual equal sign in math

# On the left sign of the equal sign you type the variable name, and in the right side you type the value you wan't to assign to that variable

# It doesn't matter if you leave a space btwn each side of the equal sign.Actually, I would advise on leaving a space on ech side of the equal sign, for better readabilityof code.
num1=7
# num1 = 7 reccomended

# You are able to do multiple assignment, so you can assign a value to multiple variables, at the same time. The syntax for this would be:
a = b = c = x = y = 10
print(a)
print(b)
print(c)
print(x)
print(y)

print("========================")

# Also you can assign a different value for each variable within the same line of code like this:
a, b, c = 10, 20, 30
print(a)
print(b)
print(c)

# next -> Data types