# Handling the ZeroDivisionError Exception

try:
    print(5/0)
    """The 'try' block runs if the code does not return an error e.g print(5/1).
    But if the code returns an error then the 'except' block runs.
    """
except ZeroDivisionError:
    print("You can't divide by zero!")
