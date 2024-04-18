# Create an empty list for storing the movies
movies = []

# Create a function to add a movie
def add_movie():
    # get the movie properties(title, director, release_year) from the user
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    release_year = input("Enter the movie release year: ")
    
    # add the movie dictionary to our movies list
    movies.append({
        'title': title,
        'director': director,
        'release_year': release_year
    })
    
# Create a function to list all the movies
def list_movie():
    for movie in movies:
        print_movie(movie)

# Create a function to find a movie by its title
def find_movie():
    
    # ask user for the movie title they are searching for
    title = input("Enter the title of the movie you are searching for: ")
    
    for movie in movies:
        if movie['title'] == title:
            print_movie(movie)

# Create a helper function for displaying the movies in a nice format
def print_movie(movie):
    print(f"{movie['title']}  directed by {movie['director']}, released {movie['release_year']}.")
# Create the menu option
MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title or 'q' to quit"

# Display the movies app to the user
def menu():
    # get the user choice/option
    selection = input(MENU_PROMPT)
    
    while selection != 'q':
        if selection == 'a':
            add_movie()
        elif selection == 'l':
            list_movie()
        elif selection == 'f':
            find_movie()
        else:
            print("Unknown command! Please try again!!!")
            
        selection = input(MENU_PROMPT)
        
# Call the menu function here
