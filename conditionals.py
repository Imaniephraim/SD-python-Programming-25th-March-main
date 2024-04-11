# Python 3 Conditionals - if / elsif / else 

# In python we have the if, elif and else statements for decision making.

# Using these statements python evaluates expressions and runs a piece of code accordingly meaning;if an expression is evaluated as true, then the code indented below the if will be executed. Otherwise python goes further and evaluates the elif or else statements if any

# Unlike any other programming languages that use curly braces or other delimeters, Python uses indentation to define code blocks, meaning if, for and while, functions and classes.

# using indentation means that whitespaces are used as delimeters for codeblocks

# e.g in other languages
# if (condition) {
#     code to execute goes here
# }

# In python
# if condition:
#      code to execute goes here

# Another thing to remember is that after if / for / while statement or function or class definiton, you must use a xlon, so that python will know that it should expect an indented blockright afetr that statement.

# Now lets start working with if , elif, and else statement

# Lets say we define a variable x = 10 and we want to make a decision based on that value. Mybe the value of x will change at some point during execution of the program and we want to handle that change in some particular way and run a piece of code.

# Lets use the if statementto execute a block of code, if the epression we provide will be evaluated as true 

x = 10

if x > 5:
    print("x is greater than 5.")
    print(x * 2)
    
x = 4
if x > 5:
    print("x is greater than 5.")
    print(x * 2)

print("Outside the if...")    


# Now, lets see how to use the else and return to our variable x which is equal to 4 

# lets print "x is greater then 5" if x is indeed greater than 5, and, "x is not greater than 5". in other case .This can e accomplished in the following way

x = 4

if x > 5:
    print("x is greater than 5.")
else:
    print("x is  Not greater than 5.")
        
# The else statement  is used to cover all other cases not covered by the if statement above it. So, if the expression following the if keyword is true, the indented code below it will be executed. Otherwise, if the expression is evaluated as false, the inednted code below else gets executed.

# But what if we want to be more granular and specify more cases and possible outputs in our program? Then we could use the elif statement 

# Lets say we want to print "x is greater than 5." if x is indeed greater than 5, "x is equal to 5.", incase x is equal to 5 at some point and "x is less than 5" for all other cases. we should then add the elif statement in between the if and else statements

# The else staetment should always be the last in an if / elif / else block

x = 4
if x > 5:
    print("x is greater than 5.")
elif x == 5:
    print("x is equal to 5.")
else:
    print("x is less than 5.")
    