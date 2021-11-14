# multiple dictionaries in a list

alien_0 = {'color': 'green', 'points': 5, 'speed': 'slow'}
alien_1 = {'colo': 'yellow', 'points': 10, 'speed': 'medium'}
alien_2 = {'color': 'red', 'points': 15, 'speed': 'fast'}

# nesting
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)

# Code to create a fleet of aliens using range()
# Make an empty list for storing aliens

aliens = []

# Make 30 green aliens.
# range () just returns a series of numbers which just tells Python
# how many times we want the loop to repeat
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:5]:
	print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

# changing aliens throughout a game

print('\n Changing colors throughout the game:')

aliens = []

for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien ['color'] == 'yelow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['pooints'] = 15

for alien in aliens[:5]:
	print(alien)
print("...")


# Putting a list in a dictionary

pizza = {
	'crust': 'thick',
	'toppings':['mushrooms', 'extra cheese'],
}

# Summarize the order.

print(f"You ordered a {pizza['crust']}-crust pizza "
	"with the following toppings:")
for topping in pizza['toppings']:
	print("\t" + topping.title())

# example with the favorite language exercise

favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah':['c'],
	'edward':['ruby', 'go'],
	'phil':['python', 'haskell'],
	}

for name, languages in favorite_languages.items():
	if len(languages) > 1:
		print(f"\n{name.title()}'s favorite languages are:")
		for language in languages:
			print(f"\t{language.title()}")
	else:
		print(f"\n{name.title()}'s favorite language is:\n \t{language.title()}")
			
	#dictionary in dictionary

	users = {
		'aeinstein': {
			'first': 'albert',
			'last': 'einstein',
			'location': 'princeton',
		},

		'mcurie': {
			'first': 'marie',
			'last': 'curie',
			'location': 'paris',
		},
	}

	for username, user_info in users.items():
		print(f"\nUsername: {username}")
		full_name = f"{user_info['first']} {user_info['last']}"
		location = user_info['location']

		print(f"\tFull name: {full_name.title()}")
		print(f"\tLocation: {location.title()}")

# 6 - 7

person_0 = {
	'name': 'giovanni', 
	'last name': 'pepi', 
	'city': 'campinas', 
	'age': 27
}

person_1 = {
	'name': 'isabella', 
	'last name': 'prado', 
	'city': 'campinas', 
	'age': 25
}

person_2 = {
	'name': 'luke', 
	'last name': 'pawswalker', 
	'city': 'campinas', 
	'age': 0
}

people = [person_0, person_1, person_2]
print("\nData we have:\n")
for i in people:
	for key, value in i.items():
		print(f"{key.title()}:")
		#check if str or int so it can process the age value
		if type(value) == str:
			print(f"\t{value.title()}")
		else:
			print(f"\t{value}")

# 6-8

pet_dict = { 

	'luke': {
		'name': 'luke',
		'species': 'cat',
		'owner name': 'giovanni, isabella',
		},

	'kiara': {
		'name': 'kiara',
		'species': 'doggo',
		'owner name': 'isabella',
	},

	'lola': {
		'name': 'lola',
		'species': 'doggo',
		'owner name': 'rafaela',
	},
}

for pet, pet_info in pet_dict.items():
	print(f"\nPet Name: {pet.title()}")
	pet_species = pet_info['species']
	owner = pet_info['owner name']
	print(f"{pet.title()} is a {pet_species.title()} owned by {owner.title()}")

# 6 - 9 

favorite_places = {

	'isabella': 'orlando',
	'giovanni': 'home',
	'luke': 'corredor',
}

for k, v in favorite_places.items():
	print(f"{k.title()} favorite place is {v.title()}")
	
# 6 - 10
# using a list inside dictionary to solve this

favorite_numbers = {

	'Giovanni': [100, 50],
	'Isabella': [18, 19],
	'Luke': [666, 13],
	'Jon': [13, 666],
	'My Apartment': [123, 321],
}

for name, numbers in favorite_numbers.items():
	print(f"\n{name.title()}\'s favorite numbers are:")
	for number in numbers:
		print(number)

# 6 - 11

saved_cities = {
	'CAMPINAS': {
		'country': 'brasil',
		'population': 1213792,
		'fact': 'campinas means grass fields in portuguese',
	},

	'sumaré': {
		'country': 'brasil',
		'population': 286211,
		'fact': 'I lived for about 24 years in Sumaré',
	},

	'itu': {
		'country': 'brasil',
		'population': 175568,
		'fact': 'Itu means big waterfall in Tupi Language',
	},
}

for city, data in saved_cities.items():
	print(f"\n{city.title()}:")
	country = data['country']
	population = data['population']
	fact = data['fact']
	print(f"\t{city.title()} is located in {country.title()}, has a population of "
		f"{population}, and {fact}")








