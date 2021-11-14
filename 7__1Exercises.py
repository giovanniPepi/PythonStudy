car = input("What car do you wish to rent? ")
print(f"\n Let me see if I can find a {car} for you.")

table = input("Welcome to InGo. How many people are attending the table? ")
table = int(table)

if table > 8:
    print(f"\nSorry, we don't have a table available for {table}.") 
    answer = input("Would you like to enter our waiting list? Y/N ")
    if answer == 'Y':
        print(f"\nYou're on our waiting list. We will call you.")
    elif answer == 'N':
        print(f"\nWe hope we can serve you another time!")
else:
    print(f"\nTable for {table}. Yes, follow me please.")

# 7 - 3

number = input("Please insert a number: ")
number = int(number)

if number % 10 == 0:
    print(f"\n{number} is a multiple of 10!.")
else:
    print(f"\n{number} is not a multiple of 10.")

