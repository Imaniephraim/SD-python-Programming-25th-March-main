USER_CHOICE = """

Enter:

- 'a' to add a new book

- 'l' to list all the books

- 'r' to mark a book as read

- 'd' to delete a book

- 'q' to quit

Your Choice: """

def menu():

    user_input = input(USER_CHOICE)

    

    while user_input != 'q':

        if user_input == 'a':

            pass

        elif user_input == 'l':

            pass

        elif user_input == 'r':

            pass

        elif user_input == 'd':

            pass

        else:

            print("Invalid choice, Please Try again!!!")

        

        user_input = input(USER_CHOICE)

# call the menu function here

menu()