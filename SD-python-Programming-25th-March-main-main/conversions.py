# Python 3 Conversions Between Data Types

# The last thing we should cover on the data types topic ofcourse is conversions between data types 

# This means you'll learn how to convert from one data type, a number for example, to another daata type, like a string.

# There are specific funcyions that accomplish these tasks. Lets see them in action.

# First lets try to convert an integer or floating point number to a string. This can be achieved by using the str() method

num = 2
f = 2.5

# Check type of the variables
print(type(num)) #<class 'int'>
print(type(f)) #<class 'float'>

# Now converting the number to a string
num2 = str(num)
print(num2, type(num2))

f2 = str(f)
print(f2, type(f2))

# Now lets try backwords and convert a string to an integer, using int()
str1 = "5"
print(str1, type(str1))

int1 = int(str1)
print(int1, type(int1))

# You can also convert integers to floating-point numbers, using the float() function and vice-versa, using the same int() function

num2 = 2

f = float(num2)
print(type(f), f)

# Now the other way round from float to interger, using int()
f = 2.9999
int1 = int(f)

print(type(int1), int1)

# Now, moving to sequences, lets convert a tuple into a list, using the list() function.
tuple1 = (1, 2, 3)
print(type(tuple1), tuple1)

# Convert the tuple to a list
list1 = list(tuple1)
print(type(list1), list1)

# We have the set() function works for turning a list into a set
list1 = [1, 2, 3]
set1 = set(list1)
print(type(set1))
print(set1)

# The last thing i'll show you here is how to convert between different numerical representation of members and I a, erferring to decimal, binary, and hex notation, so, base -10, base-2, and base-16 numbers
# For this, we'll need the bin(), hex() and int() functions.

num = 10

# Convert to binary (0, 1)
num_bin = bin(num)
print(f"10 in binary = {num_bin}")

# Convert to hex
num_hex = hex(num)
print(f"10 in hexadecimal  = {num_hex}")

# Now, to convert from binary and hex format back to decimal notation, we will use the int() function
bin_to_num = int(num_bin, 2)
print(bin_to_num)

hex_to_num = int(num_hex, 16)
print(hex_to_num)

# Next -> Python 3 Conditionals - if / elsif / else 