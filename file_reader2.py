filename = "/Users/quanefiom/Desktop/Github_Projects/Chapter 10/pi_digits.txt"

with open(filename) as file_objects:
    for line in file_objects:
        print(line.rstrip())