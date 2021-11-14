sandwich_orders = ['big mac', 'pastrami', 'lanchinho da noite', 'pastrami', 
'dogao prensado', 'pastrami']
finished_sandwiches = []

print("We ran out of pastrami, so orders with pastrami will be canceled")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"Making a {current_sandwich.title()}. ")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches are ready: ")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} is ready to be taken. ")