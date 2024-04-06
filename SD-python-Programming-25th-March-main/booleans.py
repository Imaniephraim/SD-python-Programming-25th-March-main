# Python 3 Booleans - logical Operators

# As a short definition, we can say that boolean defines only two values -> True and False.

# The name boolean comes from George Boole. He was a 19th century English Mathematician philosopher.

# Leaving the history aside  and returning to python, you can think of these two values as being equivalent to 1 and 0.

# In python, True is written as a capital letter and False with a capital F, keep ythat in mind.

# We've a;ready seen true and false in some examples during lectures, so they are not completely new to you at this point in the course.

# Basically, they are used to evaluate whether an expression if true or false and can be further used in conditional or loop structures, as we will see that later in the course.

# For now lets evaluate some basic expressions and see how Python evaluates each of them.

print(1 == 1) #returns True

print(1 == 2) #returns False

print("python" != "Python") #returns True 

print(3 <= 4) #returns True 

# ok, You got the idea. These were some pretty basic evaluations we have done.

# Now, there are three main boolean operations, each of them having a specific operator namely "and", "or" and "not"

# 1. "and" -> means both the operands should be true in order to have the entire expression evaluated as True

print((1 == 1) and (2 == 2)) # returns as True

print((1 == 1) and (2 == 3)) #returns False

# The conclusion here is that when using AND operator, If both expressions are true, the the result will also be True, on the  other hand, if atleast one expression is evaluated as false, then the result will be False

# 2. "or" -> it works as follows; If atleast one of the expressions evaluates to True, then the final result is True. If they are both False, then the final result is False
# So, when using or it is enough if only one expression is True, in order to have True as the final result
print((1 == 1) or (2 == 2)) #returns True
print((1 == 1) or (2 != 2)) #returns True
print(((1 == 1) or (2 != 3)) and ("jave" == "java")) #returns 

# 3. "not"-> Using NOT means simply denying an expression. If that expression is True, then denying it will to False and vice versa

print(not(1 ==1 )) #returns False
print(not(1 == 2)) #returns True

# One more thing to keep in my mind here:Some python values always evaluate False. They are:
# None
# 0.0
# empty string ""
# empty list []
# empty set set()
# empty tuple ()
# empty dictionary {}

# Python provides the bool() function to help us evaluate values and expressions as True or False. So, lets use this function to check the always False values
print(bool(None)) #returns False
print(bool(0)) #returns False
print(bool(0.0)) #returns False
print(bool("")) #returns False

# All some other values of python are considered to be true
print(bool(0.1)) #returns True
print(bool(" ")) # returns True

# Real world example -> Login system...

# User credentials in the DB Database
user_name_in_db = "Dennis"
password_in_db = "P@$$w0rd"

# User credentials provided during login attempt
user_name = "dennis"
password = "P@$$w0rd"

# Lets check if user credentials are correct
if (user_name == user_name_in_db) and (password == password_in_db):
    print("Login Successful!")
else:
    print("Wrong username or password, Please try again!!!")
    
# Next -> Lists