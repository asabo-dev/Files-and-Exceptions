# Refactor greet_user()
# Each function handles a specific task, making the code more consice. 
import json

def get_stored_username():
    """Get stored username if available."""
    filename = '/Users/quanefiom/desktop/github_projects/Chapter 10/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = '/Users/quanefiom/desktop/github_projects/Chapter 10/username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        answer = input(f"Hello, is this the correct username: {username} (y/n)? ")
        if answer.lower() == 'y':
            """Check if this is a first time user."""
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()