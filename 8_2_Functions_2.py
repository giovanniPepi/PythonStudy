# Positional arguments are based on the order of the arguments provided

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('cat', 'luke')
describe_pet('doggo', 'kiara')
# Wrong order:
describe_pet('luke', 'cat')

# Keyword arguments name-value to pass a function
# the order in which they are passed doesn't matter

describe_pet(animal_type='cat', pet_name='luke')
describe_pet(pet_name='luke',  animal_type='cat')

# Using default values

def describe_pet2(pet_name, animal_type ='cat',):
    """Display information about a pet."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet2(pet_name = 'luke')
describe_pet2('lukeeeeeeee')

describe_pet2('willie')
describe_pet2(pet_name = 'willie')
describe_pet2('harry', 'hamster')
describe_pet2(pet_name='harry', animal_type='hamster')
describe_pet2(animal_type='hamster', pet_name='harry')
describe_pet2()