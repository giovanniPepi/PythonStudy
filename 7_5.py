# 7 -5 

prompt = "\nPlease enter your age. "
prompt += "Type 'quit' when you are done:  " 

while True:

    age = input(prompt)
    age = int(age)

    if age < 3:

        print(f"Your ticket is free!")
        continue

    elif age >= 3 and age < 12:

        print(f"Your ticket will cost $10")
        continue

    elif age >=12:

        print(f"Your ticket will cost $15")
        continue
        
    
