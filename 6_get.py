#using get() to get values from dictionaries
#if the value 'points' exist in the dictionaries you get the value
#if not, you get the message/'None' if not defined

alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

#6-1 

person_0 = {
	'name': 'Giovanni', 
	'last name': 'Pepi', 
	'city': 'Campinas', 
	'age': 27
}

name = person_0.get('name')
print(name)
last_name = person_0.get('last name')
print(last_name)
city = person_0.get('city')
print(city)
age = person_0.get('age')
print(age)

# 6 -2 

favorite_numbers = {
	'Giovanni': 100,
	'Isabella': 18,
	'Luke': 666,
	'Jon': 13,
	'My Apartment': 123,
}

# iterate through a dictionary, get the key name
for name in favorite_numbers:
	print(f"{name}\'s favorite number is:")
	# get the value of the key
	number = favorite_numbers.get(name)
	print(number)

# 6-3

words = {
	'iterate': 'Iteration is the repetition of a process in order '
	'to generate an outcome',
	'loop': 'In computer programming, a loop is a sequence of '
	'instructions that is continually repeated until a certain '
	'condition is reached',
	'dictionary': 'A dictionary is a general-purpose data '
	'structure for storing a group of objects. A dictionary has '
	'a set of keys and each key has a single associated value.',
}

for word in words:
	print(f"\n{word.title()} meaning is:")
	meaning = words.get(word)
	print(meaning)
