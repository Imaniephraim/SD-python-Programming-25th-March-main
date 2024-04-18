# Python 3 Strings

# Lets define a string 

# A string is a sequence of characters meaning-> letters, numbers, and other characters like dollar sign, spaces and punctuation marks enclosed by either single quotes or even triple quotes when spanning lines

# lets define a string and assign it to a variable
my_string = "this is my first string"
print(my_string)
    #OR
my_string = 'this is my first string'

# what do we need triple quotes for? we need them whenever we want to eneter a string on multiple lines-> for instance a comment in our code

my_string = """this
is
my
first
string"""
print(my_string)


# indexing
# Python uses indexing to mark the position of an element within a sequence of elements -> a string is a sequence of elements and the elements of a string are the characters themselves . One character element

# The first element of any sequence, when counting from left to right has the index 0, the second has the index 1, the third of the sequence is positioned at index 2

# So when using indexes, remember to start counting 0

# when counting backwords, from right to left, the first index will be -1.

# the last character in a string will have index -1 when looking from right to left
# Indexes are closed by square brackets, when we want to access some letter of a string

# lets see this in practice

string1 = "Cisco Router"

# Now, how to extract the first character of this string? By using an index, of course. And as stated, that would be at index 0.So, to access the elelment of string1,  positioned on index 0 in the string, we should type the following:

#  the name of the variable which is string1, and then without inserting any spaces the index number between brackets, so,

print(string1[0])  # returns C

# Lets find the third character of string1. What index should we use?
print(string1[2]) #returns s

# print the space character
print(string1[5])

# Now for negative indexes, 
# lets access the last character in the string-> will be  index -1
print(string1[-1]) #returns r (last element)

print(string1[-4]) #returns u

# What if we enter an invalid index for our string
# First lets find out string1's length
# we can count how many characters are in that string visually, but what if we have a very very long string, maybe a newspaper page
# python has a solution for this and its called the len() function

print(len(string1)) # returns the number of characters which is 12

# What happens if we enter an invalid index?

# lets try this

# print(string1[20]) # returns an Indexerror : string index out of range

#Python 3 Strings methods
# We've talked about indexing and how we can determine the length of a sequence method, in our case the string, using the len() function

# Now, lets see other operations
# 1. First, one more thing about indexes is that we can find out the index of a character in a give string by using the index method
# Just remember that this method returns the first occurrence of that particular character in the string

a = "Cisco Switch"

# we can clearly see that letter 'i' appears 2 times in the string. So lets find out the index of the first occurrence of '1' in the string

print(a.index("i")) #returns 1

# explanation (syntax)
# we have the name the variable assciated with the string, 'a', then a dot, then the name of the method, 'index()', and then in between the parentheses, we enter the character we want to find out the index for, which is '1'

# Another useful python method is one that helps you find out how many times does a characetr appear in a string or generally speaking, an element inside a particular sequence. This method is called count()

# The syntax for count is similar to the one of index() method
# To use the count method or function just type in the name of the variable, then a dot, then the word count 'count' , then open and close parentheses and finally the letter you want to count surrounded by quotes

print(a.count('c')) #returns

# 3. Another string method find(). This method simply sarches for a sequence of characters inside the string and if it finds a match, then it returns the index where the sequence begins

print(a.find("sco")) # returns 2

#on the otherhand, if python doesn't find a match, then it will return -1, lets see this and serch for the substring 'xyz'
# print(a.find('xyz')) # returns -1

if a.find("x") == -1:
    print("This substring was found")
else:
    print("was found")
    
# we can also use some predifined python methods to turn a string from uppercase to lowercase ot vice-versa
# This can be accomplished by using the lower() and upper() method
print(a)

# to lowercase 
print(a.lower())

# to uppercase
print(a.upper())

# Keep in mind ,Although we just applied the lower() and upper methods, the initial string is still the same. No changes have been applied
# This is a great proof that strings are immutable
print(a)
# 5. You can also verify that a string starts or ends with a particular character or substring
# We have two methods for that: startswith()  and  endswith()
print(a.startswith("C"))  #returns True
print(a.endswith("h")) # returns True

# 6. Three very important python methods to keep i mind because of alot of usage when working with strings, are the strip(), split() and join()

# 6.1 The strip method eliminates all white spaces from the start and the end of a string 

# Lets say we have a new string, one with 3 spaces before "Cisco" and four spaces after "Switch"

b = "   Cisco Switch    "

# Lets apply the strip() method
print(b.strip()) #returns a clean strip
print(b) #returns the inital strip

# Now consider that instead of the three spaces on each side of the string, we have 3 dollar signs that we want to remove

# c == "$$$Cisco Switch$$$$"

# We want to remove the leading and the trailing dollar signs. For this we should specify the character we want to remove in between the strip()'s parentheses, so:
# print(c)
# print(c.strip("$"))

# What if we intend to have all spaces removed from the string including those inside the strip()

# lets refer to the string referenced by variable b, which has spaces at the start and end of the string

b = "   Cisco Switch    "

# You can replace() method like this, to get a clean string
print(b.replace(" ", ""))
print(b.replace("i", "*"))

# 6.2 split() method -> As its name implies, this method simply splits a string into substrings. Furthermore, you can specify a delimiter for splitting the string. The result is a list

# Lets say we have a string referenced by a variable d like this
d = "Cisco,Juniper,HP,Avaya,Nortel"

# The network device manufactrures in the string are delimited by commas. So the commas will be regarded as delimiter for the split.
# What if we want to extract each provider from the string in a nice format
# Well, in this case the split method saves the day
# Lets try the following
print(d.split(","))

# Python returns a list where each provider in the string is an element of this list and can be further used into application

# 6.3 join() method used for dealing with string
# lets remember string 'a' -> 'Cisco Switch'

# What if we want to insert a character inbetween every two characters pf a string?So, we want to change this string a to "C_i_s_c_o__S_w_i_t_c_h"

# For this we wil use the join() method the following way and is about different from the syntax we've seen before

# First, you typein the character you want to use as a separator, enclosed with double quotes, Its upto you, so this character would be the underscore in our case

print("_".join(a))

# python 3 strings - Operators & Formatting

# What else can we do with strings?

# For instance, we can concantenate them.Concatenation means unifying two or more strings into a single string

# You can this using the "+" operator, like you would when adding two numbers.

# So, lets try this
# Lets set x with the value "Cisco"
x = "Cisco"

# And y with the value switch
y = "Switch"

# and finally, add them together
space = " "
z = x + space + y
print(z)

# Another thing we can do is string repetition, by using the multiplication operator
print(x * 5)

# you can also verify if a character is in a string or not, using the "in" and "not in" operator

print("o" in x) #returns True
print("o" not in y) #returns True
print("s" in x) #returns False

# Now whats the deal with string formatting

# Lets say we have some kind of string template and we want to constantly modify a few words inside the text but keep the overall template same
# To see what i mean, lets assume we have the following string. Doesn't matter what it stands for just focus on the string itself.

my_string = "Cisco Model: 2600XM, 2 WAN Slots, IOS 12.4"

# We want to keep this string as a template and change the model name, number of slots and IOS version a couple of times, while running our python program. So, this would be a dynamic change each time

# For this we should use the percent operator (%), followed by the letter (s) for string, (d) for digit or (f) for floating point number . Lets see the syntax.

formatted_string = "Cisco Model: %s, %d WAN Slots, IOS %f" %("2600XM", 2, 12.4)
print(formatted_string)

print("===============================")
# Now lets translate this:
# The %s means that this is a placeholder for a string we will specify in between the parentheses, at the end of this line.
# The %d operator follows the same logic but for a number instead of a string.
# The %f refers to a floating point number, a number with a decimal point.
# Now, moving in, the first value from within the parentheses is going to be associated with the first format operator in the string.
# The second value from within the parentheses is going to be associated with the  second format operator in the string, and so on, for all the format operators you have in your string.
# Also do not forget to insert the % sign between the string and the parentheses containing the values.
# This operator maps the format operators inside the string with the values inside the parentheses.
# "2691XM" , 4, 12.3
# "7200XM" , 8, 15.4
# "1841M" , 1, 12.2

formatted_string = "Cisco Model: %s, %d WAN Slots, IOS %f" %("2691XM", 4, 12.3)
print(formatted_string)
formatted_string = "Cisco Model: %s, %d WAN Slots, IOS %f" %("7200", 8, 15.4)
print(formatted_string)
formatted_string = "Cisco Model: %s, %d WAN Slots, IOS %f" %("1841", 1, 12.2)
print(formatted_string)

# Something you might have noticed is the addition of several decimal places when dealing with floating point numbers. In oreder to deal with this behaviour you can easily chose the number of decimal places that you want to print out

# Simply insert a dot and a value in between the percent operator and the letter f
print("Cisco Model: %s, %d WAN Slots, IOS %.1f" %("2600XM", 2, 12.4))

# Instead of formatting operators like the one we have just seen, we can use another notation, replacing %s, %d or %f with a pair of curly brackets
formatted_string =("Cisco Model: {}, {} WAN Slots, IOS {}".format("2600XM", 2, 12.4))

print(formatted_string)

# We can use some sort of indexing when dealing with this type of string formatting 

# Lets assign a value for each of this pair of curly braces
print("Cisco Model: {0}, {1} WAN Slots, IOS {2}".format("2600XM", 2, 12.4))

# f-string formatting
first_name = "John"
user_age = 20
print(f"My name is {first_name}, and I am {user_age}, years old.")

# Python 3 String - Slices

# Slices allow us to extract various parts of a string (or a list or any other sequence of elements)

# The syntax for a string slice is the folowing 
# mystring[10:15]
# We have  the name of the variable pointing to the string, followed by a pair of square brackets, in between the brackets, we have a colon, on the left side of the colon, we specify the index at which to start the slicing process. The slice will go up to, BUT NOT INCLUDE, the index specified on the right side of the colon.

string1 = "0 E2 10.110.8.9 [160/5] Via 10.119.254,0:01:00, Ethernet2"

# Lets extract the first IP address in the string, 10.119.8.9
string1[5:15]
print(string1[5:15])

# Now what if we don't specify th esecond index inside the brackets? Well, then the string slice would start at the index specified before the colon and would end at the end of the string.
# This way we would get the rest of the string starting from the character at index. Lets test this as well
print(string1[5:])

# What if we only use the second index, the one after the colon not specifying the first index?
# Then the slice would simply start at the beginning of the string and would go upto BUT NOT INCLUDE the caharcter at the index specified we enter after the colon
# lets see this:
print(string1[:15])

# What if we don't enter any indexes at all
print(string1[:])

# what about negative indexes?
# Lets try extracting a couple of slices using negative indexing or negative values for our indexes

print(string1[-2]) # t

# What if  we want to extract a slice containing the substring "Ethernet", this time using negative indexes
print(string1[-9:-1])

# What if we want to obtain the last 5 characters of our string ?
print(string1[-5:])

# What if we want to slice string1 starting at the beginning of the string and leave out the last 5 characters
print(string1[:-5])

# one more thing about slices
# You can specify a third element within the square brackets, after the indexes, also separated by colon.This is called a step
# variable_name[start_index:stop_index:step]

# For instance if you would lke to skip every second character of the string and obtain a new string with these elements removed, you can write the following slice:
print(string1[::2])

# The last thing, is how to print out the string in reverse order, using slices and indexes.
# For this we will again use a slice and a step
# But, what would be the value of that step?
# Well, since we want to get the string in reverse order, we should start with the last character of the string, right?so, lets try it...
print(string1[::-1])