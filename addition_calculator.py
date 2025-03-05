# EXERCISE 10-7. Addition Calculator

print("Enter two integers and add them together.")
print("Enter 'q' to quit at any time.")

while True:
    first_number = input("Enter the first number: ")
    if first_number == 'q':
        break
    second_number = input("Enter the second number: ")
    if second_number == 'q':
        break

    try:
        addition = int(first_number) + int(second_number)
    except ValueError:
        print("Make sure you enter two integers.")
    else:
        print(f"The result is: {addition}")

print("---The End---")
