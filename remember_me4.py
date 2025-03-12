# First check if username has been stored.
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
    
def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        filename = '/Users/quanefiom/desktop/github_projects/Chapter 10/username.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")

greet_user()