# Pizza toppings loop

prompt = (f"\nPlease type which topping you'd like with your pizza")
prompt += (f"\nType 'quit' after you finish. ")

while True: 
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"\n{topping.title()} added!")

print(topping)
