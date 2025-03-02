# EXERCISE 10-2
# Using replace() method to change text from a file.

message = "I love dogs."
message = message.replace('dogs', 'cats')
"""You can use the replace() method to repplace any word in a string with a different word."""
#print(message)

file_name = '/Users/quanefiom/desktop/github_projects/Chapter 10/learning_python.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()
    for line in lines:
        line = line.replace('Python', 'C')
        print(line.strip())