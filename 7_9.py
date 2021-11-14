responses = {}

polling_active = True

while polling_active: 

    name = input("\nWhat is your name?: ")
    response = input("\nWhere is your dream vacation located at?: ")

    responses[name] = response

    repeat = input('Would you like to let another person answer? (yes/no)')

    if repeat == 'no':
        polling_active = False

print(f"\n--- Final Poll Responses ---")

for name, response in responses.items():
    print(f"\n{name.title()} dream vacation is going to {response.title()}.")