# Pytho 3 - working with files
# We use the open() function when working with files .

# The open() functiom takes in two arguments ->
# 1. name of the file you're opening
# 2. mode at which you are opening the file with

# syntax
# open(file_name, mode)

# We have several modes
# 1. read -> 'r' : open a file for reading data, and raises an error if the file doesn't exist
# 2. append -> 'a' : opens a file to append it, creates the files if it doesn't exists
# 3. write -> 'w' : opens a file to write to it, overwrites the existing data, creates the file if it does not exist 
# 4. create -> 'x' : creates a new file

# Reading data from a file

# Lets create a new file

# fruits_file = open('fruits.txt', 'x')


# reading from a file
# my_file = open('fruits.txt', 'r')

# file_contents = my_file.read()

# my_file.close()

# print(file_contents)

# appending to a file
# student = "Bradley"

# my_file = open('students.txt', 'a')
# my_file.write(student + "\n")

# my_file.close()

# writing to a file
# new_student = 'Elvis'

# my_file = open('students.txt', 'w')

# my_file.write(new_student + "\n")

# my_file.close()

# context managers -> with

# read fruits
with open('fruits.txt', 'r') as f:
    file_content = f.read()
    print(file_content)
    
    
# Challenge time
# 1. Write a Python script which asks the user for input (infinite loop with exit possibility) and writes the input to a file.

# SOLUTION
# is_running = True

# while is_running:
#     print("Please choose from the menu")
#     print("1. Add your input")
#     print("q. Quit")
    
#     # get user input
#     user_input = input("Enter your choice: ")
    
#     # Check for the user input
#     if user_input == '1':
#         data_to_store = input("Please provide input data: ")
        
#         with open('sample.txt', 'a') as file:
#             file.write(data_to_store + '\n')
            
#     elif user_input == 'q':
#         is_running = False
        
# 2. Add another option to your UI user Interface: The user should be able to output the data stored in the file in the terminal
is_running = True

while is_running:
    print("Please choose from the menu")
    print("1. Add your input")
    print("2. Output data")
    print("q. Quit")
    
    # get user input
    user_input = input("Enter your choice: ")
    
    # Check for the user input
    if user_input == '1':
        data_to_store = input("Please provide input data: ")
        
        with open('sample.txt', 'a') as file:
            file.write(data_to_store + '\n')
    elif user_input == "2":
        with open('sample.txt', 'r') as file:
            contents = file.read()
            print(contents)
    elif user_input == 'q':
        is_running = False
# 3. Store user input in a list(instead of directly it to a file) and write that list to the file -> using JSON and pickle


 