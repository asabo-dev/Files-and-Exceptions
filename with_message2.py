# Writing Multiple Lines

filename = '/Users/quanefiom/desktop/github_projects/Chapter 10/programming.txt'

with open(filename, 'w') as file_object:
    contents = "I love programming.\n"
    contents += "I love creating new games.\n"
    contents += "I also love working with data.\n"
    file_object.write(contents)
    

