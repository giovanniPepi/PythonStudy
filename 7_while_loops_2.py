#'break' exits a loop without running any remaining code

prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you're finished.) "

while True: 
    city = input(prompt)

    if city =='quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

# 'continue' returns to the beginning of the loop
# based on the result of a conditional test

# this code will print only odd numbers: 

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
