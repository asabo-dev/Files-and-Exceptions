# Saving user input with json
import json

username = input("What is your name?  ")

filename = '/Users/quanefiom/desktop/github_projects/Chapter 10/username.json'

with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")