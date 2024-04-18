# Python 3 - User input

# ctrl + / -> shortcut for inserting a comment

# Throughout, you are going to learn how to insert an input into a Python program

# Actually, you are going to use a specific function in order to ask the user for some input, store the information he/she is entering at the prompt themn use that information further into the program.

# This is especially useful when you need to build an interactive application, usually leaving some sort of menu that the user needs to interact with.

# examples of such menus are "Please enter your username: " or "Choose an option from the following list: " and so on...

# The funnction we are talking about is called input()

# lets prompt the user to enter a string that he?she wants to be printed out on the screen.

# Let me write the code and then analyze it inch by inch

user_says = input("Please enter the string you wish to print: ")

# Looking at the above line of code, you may ask yourself: what is this 'user_says' thng?
# well that a python variable and don't worry, we will talk more about variables very soon.
# For now, just keep in mind by using a variable, you can store or save the value entered by the user, for later use.

# The so called storing or saving of the users input is accomplished using the equal sign "=" is called an assignment operator.

# following thhe equal sign, we have the input() function.
# Next, inside input()'s pair of parenthesis, you have to type in a description, a phrase, which is actually a string asking the user for input. This is completely upto you with an appropriate sentence.

# A good practice here is to also eneter a colon and a space after a text, so when a user inputs some data into it it will be clearly separated from the sentence you wrote -> just for easiness of reading 

# Finally, don't forget to close everything you write in between parenthesis, also using either double or single quotes.

# Last but not least, in order to have our text printed out on the screen ad visible to the user, we should use the print() function in python, to print out the content of the user_says variable.

print(user_says)

# shortcut for opening the terminal -> ctrl + j

# Next - variables 