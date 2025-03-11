# Use json.dump() to store a set of numbers in a file.
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = '/Users/quanefiom/desktop/github_projects/Chapter 10/numbers.json'

with open(filename, 'w') as f:
    json.dump(numbers, f)