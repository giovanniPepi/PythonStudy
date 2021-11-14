#defines alien color

alien_color = 'red'

if alien_color == 'green':
	print(f'\nYou have earned 5 experience points.')

alien_color = 'green'

if alien_color == 'green':
	print(f'\nYou have earned 5 experience points.')

#5-4

alien_color = 'red'

if alien_color == 'green':
	print(f'\nYou have earned 5 experience points.')
else:
	print(f'\nYou have earned 10 experience points.')

alien_color = 'green'

if alien_color == 'green':
	print(f'\nYou have earned 5 experience points.')
else:
	print(f'\nYou have earned 10 experience points.')

#5-5

alien_color = 'green'

if alien_color == 'green':
	print(f'\nYou have earned 5 experience points.')
elif alien_color == 'red':
	print(f'\nYou have earned 15 experience points.')
elif alien_color == 'yellow':
	print(f'\nYou have earned 10 experience points.')

alien_color = 'red'

if alien_color == 'green':
	print(f'\nYou have earned 5 experience points.')
elif alien_color == 'red':
	print(f'\nYou have earned 15 experience points.')
elif alien_color == 'yellow':
	print(f'\nYou have earned 10 experience points.')

alien_color = 'yellow'

if alien_color == 'green':
	print(f'\nYou have earned 5 experience points.')
elif alien_color == 'red':
	print(f'\nYou have earned 15 experience points.')
elif alien_color == 'yellow':
	print(f'\nYou have earned 10 experience points.')

#5-6 Stages 

person_age = [0, 2, 4, 6, 8, 10, 12, 15, 20, 25, 30, 40, 50, 60, 70, 99, 110]

for age in person_age:
	if age < 2:
		print(f'\b{age} You\'re a baby!')
	elif age >=2 and age <4:
		print(f'\b{age} You\'re a toddler!')
	elif age >= 4 and age < 13:
		print(f'\b{age} You\'re a kid!')
	elif age >= 13 and age < 20:
		print(f'\b{age} You\'re a teenager!')
	elif age >= 20 and age <65:
		print(f'\b{age} You\'re an adult!')
	elif age >=65 and age <80:
		print(f'\b{age} You\'re a fucking elder!')
	elif age >=80:
		print(f'\b{age} How the fuck are you even alive???')

#5-7

favorite_fruits = ['banana', 'ameixa', 'maçã']

fruit = 'banana'

if fruit in favorite_fruits:
	print(f'You really like {fruit}!')

fruit = 'ameixa'

if fruit in favorite_fruits:
	print(f'You really like {fruit}!')

fruit = 'melancia'

if fruit in favorite_fruits:
	print(f'You really like {fruit}!')

fruit = 'maçã'

if fruit in favorite_fruits:
	print(f'You really like {fruit}!')

fruit = 'Pitaya'

if fruit in favorite_fruits:
	print(f'You really like {fruit}!')

fruit = 'Figo'

if fruit in favorite_fruits:
	print(f'You really like {fruit}!')