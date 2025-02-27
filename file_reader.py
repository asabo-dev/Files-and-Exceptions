# Reading the Content of a File

with open("/Users/quanefiom/Desktop/Github_Projects/Chapter 10/pi_digits.txt") as file_object:
    contents = file_object.read()
    print(contents.rstrip())