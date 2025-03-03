filename = '/Users/quanefiom/desktop/github_projects/Chapter 10/programming.txt'

with open(filename, 'w') as file_object:
    """There are several parameters that can be passed to open()
    such as: 'w' for write function, 'r' for read() which is default, 'a' for append().
    """
    file_object.write("I love Python.")

