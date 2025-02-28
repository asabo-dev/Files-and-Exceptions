filename = "/Users/quanefiom/Desktop/Github_Projects/Chapter 10/pi_digits.txt"

with open(filename) as file_objects:
    lines = file_objects.readlines()

for line in lines:
    print(line.rstrip())