# EXERCISE 10-11 Prompt for favorite number and store in json file.
import json

filename = '/Users/quanefiom/desktop/github_projects/Chapter 10/favorite_number.json'

favorite_number = input("What is your favorite number? ")

with open(filename, 'w') as f:
    json.dump(favorite_number, f)
    
