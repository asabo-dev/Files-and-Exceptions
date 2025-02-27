# Reading the Content of a File

with open("/Users/quanefiom/Desktop/Github_Projects/Chapter 10/pi_digits.txt") as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# Use the rstrip() method to remove the extra blank lines that appear in the output.
# The rstrip() method removes any whitespace characters from the right side of a string.
# The strip() method removes whitespace from both sides, and lstrip() removes whitespace from the left side.

