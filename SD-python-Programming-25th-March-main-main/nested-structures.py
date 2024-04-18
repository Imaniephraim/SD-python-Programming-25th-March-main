# Python 3 Nesting - if /For/ while

# You can use nesting with control flow statements like:if, for and while to enable a certain behaviour and logic inside your python program.
# Think of nesting as using an if statement inside another if statement, a for loop inside another for loop, or a while loop within another while loop.

# Lets use some basic examples to see what i mean


# First lets refer to if statement and code 

# When nesting an if statement inside another if statement, we are actually telling python that the indented code the nested if statement should be executed only if both the inner statement and outer statement are evaluated as true. Lets see what we mean by that

x = "Cisco"

if"i" in x:
    if len(x) > 3:
        print(x, len(x))
        
# This code is the same as using the same thing as using the 'and' logical operator between the two expressions
if ("i" in x) and (len(x) > 3):
    print(x, len(x))
    
# Now, lets take a look at a nested for loop
# Lets assume we have two list and we want to multiply each element if the first list by each element of the second list. For this we should iterate over both lists at the same time then take each elemnet into account, do the multiplications and return the result.

# Let me write this and we dicuss it afterwards

list1 = [4, 5, 6]
list2 = [10, 20, 30]

for i in list1:
    for j in list2:
        print(i * j)
        
    
print("=================================") 
#  Lets say that after doing the multiplication we did for each element of list1, we want to also print that element of list1, just to have it printed out after each iteration

list1 = [4, 5, 6]
list2 = [10, 20, 30]

for i in list1:
    for j in list2:
        print(i * j)
    print(i)
    
#  Now, let me write a nested while structure and then we analyse it, as always
x = 1

while x <= 10:
    z = 5
    x += 1
    while z <= 10:
        print(z)
        z += 1
        
#  The result is 5 6 7 8 9 10 printed out 10 times
# The first while loop does the same thong as it did before. It checks whether x is less than or equal to 10, and, as long as this expression is True, it increments x by one unit - The new thing here is nested while loop gets executed each time the first while loop is executed

# The last thing here I'll add is nesting a different structure. So, lets try nesting an if statement inside a for loop, as an example

for number in range(10):
    if 5 <= number <= 9:
        print(number)
        
#  Next -> Break, Continue, Pass
