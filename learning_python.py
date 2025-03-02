# EXERCISE 10-1
# Learing Python.

file_name = '/Users/quanefiom/desktop/github_projects/Chapter 10/learning_python.txt'

with open(file_name) as file_object:
    content = file_object.read()
    print(content)

print("---")

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

print("---")

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())