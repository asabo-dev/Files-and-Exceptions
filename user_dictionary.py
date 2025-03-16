# EXERCISE 10-13
# Store user information in a dictionary.
# First check if user info is stored already.

import json

def get_stored_user_info():
    """Get stored user information if available."""
    filename = '/Users/quanefiom/desktop/github_projects/Chapter 10/user_dictionary.json'
    try:
        with open(filename) as f:
            user_info = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return user_info 
    
def get_user_info():
    """Prompt for a new user information."""
    user_info = {}
    information = True
    # Set flag for while loop

    while information:
        #Prompt user for information
        username = input("What is your username? ")
        name = input("What is your name? ")
        age = input("How old are you? ")
        location = input("Where do you live? ")

        # Store user data under their username
        user_info[username] = {"Name": name, "Age": age, "Location": location}

        more_info = input("Is there any additional info? (y/n) ")
        if more_info.lower() == 'n':
            information = False

        filename = '/Users/quanefiom/desktop/github_projects/Chapter 10/user_dictionary.json'

        with open(filename, 'w') as f:
            json.dump(user_info, f)
        return user_info
    
def display_user_info():
    """Display user information."""
    user_info = get_stored_user_info()
    if user_info:
        for key, value in user_info.items():
            print(f"{key}: {value}")
    else:
        user_info = get_user_info()
        for key, value in user_info.items():
            print(f"{key}: {value}")

display_user_info()