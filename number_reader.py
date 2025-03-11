# Use json.load() to read a file back into memory
import json

filename = '/Users/quanefiom/desktop/github_projects/Chapter 10/numbers.json'

with open(filename) as f:
    numbers = json.load(f)
    """
    This function takes in a JSON-formatted string and returns
    a Python object(list), which was stored to a Variable(numbers).
    """

print(numbers)