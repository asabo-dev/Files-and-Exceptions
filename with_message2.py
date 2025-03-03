# Use append() to Add Text to a File

filename = '/Users/quanefiom/desktop/github_projects/Chapter 10/programming.txt'

with open(filename, 'a') as file_object:
    contents = "I also love finding meaning in large datasets.\n"
    contents += "I love creating apps that can run in a browser.\n"
    file_object.write(contents)
    

