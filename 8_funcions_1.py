# def is used to define a function

def greet_user(username):
    # This is a docstring that defines what the function does
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')

def display_message():
    """Display a message about exercise 8-1."""
    print("I'm learning about functions in Python! "
    "WHERE LAMBO?")

display_message()

def favorite_book(title):
    """Display the title of favorite book"""
    print(f"One of my favorite book is {title.title()}")

favorite_book('Filosofia bastter.com')