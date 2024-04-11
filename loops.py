# Python 3 loops - For loops

# For loop

# The for statement is used whenever we want to iterate over a sequence and execute a pice of code for all or ome elements of that sequence - list or dtring, or whatever you hve.

# Lets start with an example of iterating or looping over a sequence and, first, lets define a list.

vendors = ['Cisco', 'HP', 'Nortel', 'Avaya', 'Juniper']

# Now lets see how we can work with for loop

# First, you'll notice that there are some similarities to the if, elif, else syntax, meaning that the colon is again used to signal that an indented code follows the for statement, speaking about indentation, we MUST indent the code inside the for-loop

# Syntax
# We start by typing in the for keyword, then we enter the starting variable, which is a user- defined temporary variable, so you can name it however you like, then we type in the 'in' keyword, to tell Python that we are going to iterate over the sequence following the key wordand finally, we enter the sequence itself, followed by a colon:

for each_vendor in vendors:
    print(each_vendor)
    
    
#We can also iterate over a string

my_string = 'Cisco'

for letter in my_string:
    print(letter)
    print(letter * 2)
    print(letter * 3)
    
# Now its time to see how to use a for loop to iterate over a range. Remember the range data type, that can be use to generate an iterator over which we can iterate and then extract some values.
    
# Lets consider a range starting at 0 and going up to, but not including, 10, with the default step of 1. That would return the integers 0 all the way to 9, in an ascending order

# Lets create this range
my_range = range(10)

# Now, lets use a for loop to iterate over this range 
for i in my_range:
    print(i)
    
    
print("======================================")

# Output -> 0 1 2 3 4 5 6 7 8 9
# Challenge -> output this -> 0 2 4 6 8 10 12 14 16 18
my_range = range(10)
for i in my_range:
    print(i * 2)
    
# Now lets see a more common use of the range function inside a for statement. What if we want to iterate over a list using indexes? What do i mean by that? Okay, we still have the vendors list in memory

print(vendors)

# Now  remember the len() function from earlier? Lets apply it to our list
print(len(vendors)) #returns 5

# We know that range(5) return the integer starting with 0 upto but not including 5, right?Moreover, we can convert this range to a list, using list() function. Lets do this
print(list(range(5))) #returns range [0, 1, 2, 3, 4]

# We can look at the elements of the lists as being the indexes of each elementsof our list, vendors. So, element 'Cisco' will be positioned at index o, 'HP at index 1 and so on
# This means that if we want to get a list of indexes to iterate over, using the for loop, we can use range (len(range))
print(range(len(vendors)))

# For now lets create a for loop that prints out each element of the vendors list by its index

# Challenge
for element_index in range(len(vendors)):
    print(vendors[element_index])
    
# output:
# Cisco
# HP
# Nortel
# Avaya
# Juniper