# Python 3 Exceptions

# In python, you ,may encounter two main types of errors and exceptions

# A syntax error occurs when you don't follow Python's syntax and maybe you forget to add a xolon, or the indentation is not proper.

# Lets try this and skip the colon following a for statement on purpose
# for i in range(10)
# we got a syntax erroras expected. This is an example of an error in Python

# Now, lets talk about exceptions

# Unlike syntax errors, exceptions are raised during the execution of the program, interrupting the normal flow of the application.

# Lets see a couple of examples

# First, lets use the same for loop to generate one of the many types of exceptions, called NameError

# I will misspell the name of the range() function and wait for python to notice any mistake
# for i in rnnge(10):
    # print(i)
    
# NameError : name 'rnge' is not defined
# What do we have here? A NameError. This means either that i mispelled a word in my code, in this case the name of a function or the variable or function I'm trying to use is not yet defined in any namespace

# Another type of exception raised when trying to divide a number by 0.
# Lets see this

print(4 / 0)

# ZeroDivisioError: division by zero
# Fair enough, we cannot divide a number by xero, so Python raises a special exception for that particular case

# There are many types of exceptions in Python. We won't analyse all of them now, because you will most likely encounter most exceptions as you start creating and trouble shooting  your own real progarms

# However you can find a coprehensive lost of Python 3 exceptions in this links

# https://docs.python.org/3/tutorial/errors.html
# https://docs.python.org/3/library/exceptions.html

# Next -> Python functions - Basics