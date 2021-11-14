# 7 -5 7-6

# prompt the user to enter age and assign it to age variable

prompt = "\nPlease enter your age."
prompt += "\nType 'quit' when you are done: "

while True:

    age = input(prompt)
    
    # check if input is compatible (int)
    if age.isnumeric(): 

        #Converts str to int and proceed to check
        age = int(age)

        if age < 3:

            print(f"\nAt {age} years old your ticket is free!\n")

        elif age >= 3 and age < 12:

            print(f"\nAt {age} years old, tickets are $10\n")
        
        elif age >= 12:

            print(f"\nAt {age} years old, tickets are $15\n")
    
    elif age == 'quit':

        print('\nExiting program...')
        break

    elif age == 'QUIT':

        print('\nExiting program...')
        break

    elif age == 'Quit':

        print('\nExiting program...')
        break

    else:
        print("\nPlease enter a valid age. Example: 15. ")

