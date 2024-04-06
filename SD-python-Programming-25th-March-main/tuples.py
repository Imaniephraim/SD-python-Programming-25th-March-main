# Python 3 Tuples - Introduction

# You can consider tuples as immutable lists, meaning their contents cannot be changed by adding, removing or replacing elements

# Tuples can be useful when you want to store some data in the form of a sequence and keep that data untouchable.

# However, unlike sets, tuples are ordered collections of non unique elements, meaning indexes and duplicates are allowed

# Lets start to practice and create our first tuple

# Tuples are enclosed by parentheses(round brackets) and their elements are separated by commas

my_tuple = ()

# Check type
print(type(my_tuple)) #returns <class 'tuple'>

# If you want to create a tuple with a singke elememnt you have to use a trick, meaning that, although you have only one element inside the tuple, you have to write a comma after it, otherwise it will not be regarded as a tuple
my_tuple = (9)
print(type(my_tuple)) #returns <class 'int'>

my_tuple = (9,)
print(type(my_tuple)) #returns <class 'tuple'>

# Now you have a tuple setup. You should always remember this when creating tuples having only one element

# Next, lets populate our tuple with more elements
my_tuple = (1, 2, 3, 4 ,5)

# Just likes string and lists, tuples support indexing, so idf you want to access an elelmnt within the tuple, the indexing rules thta we've seen before are still applicable

# access the first element
print(my_tuple[0])

# Access the last element
print(my_tuple[-1])
print(my_tuple[4])

# since tuples are immutable you cannot modify an element of a tuple
# Lets check this
# my_tuple[0] = 10 #Type error that says: 'tuple' item doesn't support item assignment

# Also, removng elements is not permitted from working with tuples.
# del my_tuple[0] #Type error that says: 'tuple' item doesn't support item deletion

# Another interesting you can do with tuples is tuple assigniment. This means you can assign a tuple variable to a tuple of values and map each variable in the first tuple to the corresponding value in the second tuple 
# lets see this, as well
# Lets define tuple1 with the following elements
tuple1 = ('Cisco', '2600', '12.4')

# And now, lets assign a tuple of variables to tuple1
(vendor, model, ios) = tuple1

# Finally, lets check if the assignment and variable-to-value mapping has been properly performed
print(vendor)
print(model)
print(ios)

# This also called tuple parking and unpacking and you acn see it as a kind of elements. Otherwise, if you ahve it as a kind of mapping between elements of two different tuples

# An important thing to remember is that both typle s should have the same number of elements. Otherwise if you have different number of elements, a value error will be returned.

# tuple2 = (1, 2, 3, 4)
# (x, y, z) = tuple2
# print(x)
# print(y)
# print(z)
# returns ValueError: too many values to unpack (expected 3)


# You can also assign a tuple to  a variable  in another tuple within a single statement, which even more convenient
(a, b, c) = (10, 20, 30)
print(a)
print(b)
print(c)

# Python 3 sets - Methods

# we can use the len() function to find out the number of elements of a tuple
tuple2 = (1, 2, 3, 4)

# Check the number of elements in the tuple -> len()
print(len(tuple2)) # returns 4

# Also we have the min() and max() functions available forf finding the lowest and greatest value 
print(min(tuple2)) #returns 1
print(max(tuple2)) #returns 4

# We can also concatenate and multiply a tuple, using the same old plus and multiplication operators

# Tuple concatenation
print(tuple2 + (5, 6, 7))

# Tuple multiplication
print(tuple2 * 4)

# Since indexing applies to tuples as it does to strings and lists, slicing is also possible with tuples

# Lets see a couple of examples, without entering into details about slicing again, since the rules are basically identical

# (1, 2)
print(tuple2[:2])

# (1, 2)
print(tuple2[0:2])

# (2, 3, 4)
print(tuple2[1:])

# (1, 2, 3, 4)
print(tuple2[:])

# using -ve index
# (1, 2)
print(tuple2[:-2])

# (3, 4)
print(tuple2[-2:])

# (4, 3, 2, 1)
print(tuple2[::-1])

# (1, 3)
print(tuple2[::2])