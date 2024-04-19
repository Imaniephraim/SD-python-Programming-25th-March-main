import random

# Lottery Application (List/Set/Dictionary/Comprehension)

# Functions for implementing this app
# 1. Getting the user lucky numbers
# 2. Generating the winner lucky numbers
# 3. Displaying the menu to the users

# Function to generate the winning numbers
def create_lottery_numbers():
    # create a list for the random lucky get_player_numbers
    # values = []
    # for value in range(6):
    #     values.append(random.randint(1, 50))
    # return values

    # create a set for the random lucky numbers
    values = set()
    # Loop as long as the length of values set is less then 6
    while len(values) < 6:
        # Add a random number to the set
        values.add(random.randint(1, 50))
        # Return values set
    return values
# print(create_lottery_numbers())

# A function to get user numbers for the lottery draw
def get_player_numbers():
    # Prompt the user for six numbers
    numbers_csv = input("Enter six numbers separated by commas(no spaces): ")
    # Create a list of numbers from the numbers_csv
    numbers_list = numbers_csv.split(',')
    # Create an empty set to store the number
    numbers_set = set()
    # use a for loop to add the numbers in the empty set
    for number in numbers_list:
        numbers_set.add(int(number))
    return numbers_set

# print(get_player_numbers())

# A function to display the menu to the players
def lottery():
    # Ask the user for the lucky numers
    user_lucky_numbers = get_player_numbers()
    # generate the lottery winning numbers
    lottery_numbers = create_lottery_numbers()
    # print out the winning numbers
    matched_numbers = user_lucky_numbers.intersection(lottery_numbers)
    # create the prize
    prize = 100 ** len(matched_numbers)
    print(f"The winning numbers were{lottery_numbers}")
    print(f"You matched {matched_numbers} and won Ksh {prize}") 
# call the  lottery function
lottery()