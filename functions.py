#  Python functions - Basics

# Big, big topic ahead 

# This is a core topic in python and infact in any other programming language. 
# You are going to use functions alot to build ypur applications
# But first of all what is a function?

# Well, lyou can use a function to organise your code in  blocks that can be later be reused. This is helpful if you want better readability of your code, modularity and also time saving when designing and running your code.

# Before we start writing code, rememberthat functions follow the same syntax rules as structures that we've seen so far, but also add some features we are going to analyse very soon

# First, a function is defined using the 'def' keyword, followed by a pair of parentheses and then a colon. After the colon, on the next row, you will type in the code you want to store in this function, indented one level to the right, as we did with 'if' or 'for' statements.

# Lets see this

def my_first_function():
    "This is our first function!"
    print("Hello Python!")
    
# So, assaid before, we have the def keyword, the anme if the function, ny_first_function, then the parenthesis and finally the colon. This is the way you define a function.

# One important thing to remember here is that in between the parenthesis ypu can specify one or several parameters for the function. We wil see how to that in a moment.

# Until then, lets further study our function definition
# Affter the colon, we type in the code we want this function to execute - indented, ofcourse.

# Notice that on the first row the inside the function typed in a string. This is a docstring and its role is to describe function. However, it is entirely optional - maybe you can use it when you define complex functions with complex applocations, to remember the role of the function and how it is connected to other segments of your program

# You can access the docstring by using the help() command
print(help(my_first_function))

# Now, I said earlier that functions are re-usable blocks of code. Lets see why

# After defining a function, with or without any parameters inside the parentheses we can call that function whenever we need to run the code inside it.

# In order to call a function you just need to type in that functions name followed by the parentheses and thats it. Lets see this in action
my_first_function()

# Another advantage of functions is that you can cahnge the code within a function and see the results changing as well, the next time you call that function.
# So we can say, functions are dynamic structures.

# Lets redefine our functions and change the code inside it. Then, on the next call, the result should reflect the update we've just made
def my_first_function():
    print("Hello Java")
    
my_first_function()

# Okay now lets talk abit about parameters and arguments and the difference between the two concepts
# Lets modify our existing function and insert our first parameter into the picture. Remember parameters are written inside the parentheses.

# Lets see how they work

def my_first_function(x):
    print(x)
    
# So in this case, x is passed as a parameter to the function and then added inside the code within the function. This means that whnever we're going to call the function and pass an argument of our choice to the function, that the argument will be further passed to the code inside the function.
    
# As a side note - one thing to keep in mind here is the terminology when using the function

# Parameters are the ones written inside the parentheses when 'calling' the function.

# Most of the time they are used interchangibly but, but you should try to follow and use this terminology, though.

# For now, lets try to return to our function and call it by passing an argument in the function call.

my_first_function("Hello Everyone!")

# So, what we did is we called our function and told Python to use the string inside the parentheses as an argument. Then, the string was passed to print() function and, finally, printed out on the screen.

# You can also enetr multiple parameters within a function definition, like this:
def my_first_function(x, y):
    print(f" Hello {x}")
    print(f"{y}")
    
# So, according to this poece of code, we expect that whenn calling the function and passing two strings as arguments inside the parentheses, they will both be printed out, preceeded by the "Hello" string. Lets see if I'm right

my_first_function("Python", "Java")

# Notice that x was mapped to 'python' and y was mapped to "Java", because that was the order we used when passing the arguments. Pretty intuitive I think.

# Now, we are going to touch on another topic and that is the "return" statement.

# This statement is used to exit a function and return something whenever the function is called.

# Lets create a new function and see how the return statement works. Let me write this first.
def add_two_numbers(x, y):
    sum = x + y
    
# So, we have created a variable inside our function, that will reference the result of adding x and y, which are the function's parameters. Lets see if our function returns something we can call it
add_two_numbers(3, 7)

# So nothing is returned. That's because we haven't specified what exactly are we looking to get back from the function.

# The function in its current form does nothing more than creating a variable named sum and storing the result of adding 3 and 7

# However, it doesn't return anything. It keeps the result secret, for now. That s why we need the return statement.

# Lets see how to use it.

def add_two_numbers(x, y):
    sum = x + y
    return sum

print(add_two_numbers(3, 7))

result = add_two_numbers(23, 27)
print(result)

# So thistime we told python to return the value stored by the sum and we got the expected result in return.

# We can change the function even more and xall it by using another set of arguments.

# Lets add another set of parameters, z, change the expression and then return the value of sum squared

def add_two_numbers(x, y, z):
    sum = (x + y) * z
    return sum ** 2
print(add_two_numbers(1, 2, 3))

# The last thing i shouldadd here is that if you just use the satement, without specifying what exactly do you want to get out of the function , Python will return the 'None' value. So, 'return' without specifying what to return is, actually, the same thing as return None. Lets try this
def greet_user(name):
    greeting = f"Hello, {name}!"
    return greeting
 
print(greet_user("Dennis"))

# Challenge time
# create a python program using 5 or 4 functions that asks the user for their name and age. Then the program should output the user info in a nice format displaying the name age, decades lived and age in seconds that the user has lived

# Prompt use to enter name
def user_name():
    name = input("Enter your name: ")
    return name
    


def user_age():
    age = int(input("Enter your age: "))
    return age 
    
def decades_lived(age):
    return age // 10

def user_age_in_seconds(age):
    in_seconds = age * 360.25 * 24 * 60
    return in_seconds

# A function to display the user info
def display_user_info():
    name = user_name()
    age = user_age()
    decades = decades_lived(age)
    age_in_seconds = user_age_in_seconds(age)
    print(f"Hello {name}, you have lived for {decades} decade(s) and {age_in_seconds} seconds which means you are {age} years old. ")

# call the display_user_info()
display_user_info()

# 2. Create a function that takes in a list of integers and then in returns the smallest odd integer in that list