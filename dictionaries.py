# Python 3 Dictionaries - Introduction

# Lets study another very important data type, that you need for your python adventure,

# A dictionary is an unordered set of 'key values' pairs, separated by comma and enclosed by curly baraces.

# They are very useful for storing information in a specific format. For instance, considering a router, we can store data about the device in the following format:
# 'Vendor': 'Cisco', 'model': '2600', 'ios': '12.4', 'ports': 4

# Dictionaries are mutable, which means we can modify their contents using dictionary-specific procedures. Why do I say dictionary-specific ?Because, unlike strings or lists, dictionaries are not indexed by the position of each element, like we previously had 0 for the first element, 1 for the next and so on...

# DICTIONARIES ARE INDEXED BY THE KEY. The key is the value on the left side of the colon of ech key value pair. We will see this in practice, don't worry.

# For now, lets create an empty dictionary

dict1 = {}

print(dict1) #returns {} -> empty dictionary

# Check the type of dict1
print(type(dict1)) #returns <class 'dict'

# This is how you create an empty dictionary
# Lets add some data to our dictionaries

dict1 = {'Vendor': 'Cisco', 'model': '2600', 'ios': '12.4', 'ports': 4}

# Lets notice a few things here:

# First, because the keys in the dictionary are actually strings, each key is enclosed by quotes. This is the most widely spread data type used for a dictionary.. You may also use number as a key in order to have  some kind of numbering system, like this:

d1 = {1: 'First Element', 2: 'Second Element', 3: 'Third Element'}

# Okay, lets get back to dict1 dictionary

# A key thing to remember here is, that each key in the dictionary must be unique and should be of an immutable type -> this means strings, numbers or tuple as keys but not lists

# On the other hand values don't have to be unique and can be either mutable or immutable data type.

# Python 3 Dictionaries - Methods

# Lets consider dict1

# First lets extract the corresponding values for a specific key. This can be done similarly to accessing elements in a list, only that we don't specify an index, we specify the associated key for the value we want to extract

print(dict1)

# Output '12.4'
print(dict1['ios'])
        # OR
print(dict1.get('ios'))

# Remember, we said that dictionaries are  mutable.
# Lets try to add a new key value pair to our dictionary. This is done by simply assigning a new value to the new key.
# "RAM": "128"

dict1['RAM'] = '128'
print(dict1)

# Change ios to 15.8
dict1['ios'] = '15.8'
print(dict1)

# We can also delete a pair from a dictionary using del command -> delete key 'ports
del dict1['ports']
print(dict1)

# Next, remember the len() function from strings,lists and tuples which can be use here as well to find out the number of key-value pairs inside a dictionary
print(len(dict1)) #returns 4

# You can verify if a certain string is a key in our dictionary or not, like
print("IOS" in dict1) #returns False

# Now, there are three important python methods to deal with keys and values in ad ictionary

# 1. -> The first method is keys(). This method is used to obtain a list having the keys in a dictionsry as elements
print(list(dict1.keys()))

# 2. The second is called values(), this method is used to obtain a list having the values in a dictionary as elements
print(list(dict1.values()))
# 3. -> The third is item(), returns a list of tuples each tuple containing the key and value of each dictionary pair. Lets check this out
print(list(dict1.items()))

# create a python program that captures the anmes and a list of five subjects scores and then stores the information to a dictionary, the program then outputs the average score of the student.

# ask for the student name
name = input("Enter the student name: ")
# ask for the student scores
math = int(input("Enter the score for maths: "))
english = int(input("Enter the score for english: "))
kiswahili = int(input("Enter the score for kiswahili: "))
science= int(input("Enter the score for science: "))
sst = int(input("Enter the score for sst: "))


# add the scores to a list
# scores = [math, english, kiswahili, science, sst]
# scores = []

# scores.append(math)
# scores.append(english)
# scores.append(kiswahili)
# scores.append(science)
# scores.append(sst)

# average = sum(scores) / len(scores)


# Store them in a variable
students = {
        'name': name,
        'math': math,
        'english':english,
        'kiswahili':kiswahili,
        'science':science,
        'sst':sst,
}
# compute the average score
# average = (students['math'] + students['english'] + students['kiswahili'] + students['science'] + students['sst']) / 5

scores_list = list(students.values()) #['Dennis', 'math', 'english', 'kiswahili', 'science', 'sst']) / 5
scores_list_without_name = scores_list[1:] #[89, 90, 92, 67, 67]

average = sum(scores_list_without_name) / len(scores_list_without_name)

# output the average score
# Print(students)

# Next -> conversions