user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
}

# loops for dictionaries need two variables
# items() return the list of key-value pairs

for key, value in user_0.items():
	print(f"\nKey: {key}")
	print(f"Value: {value}")

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}.")

# keys () is useful when you don't need to work with the values

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

for name in favorite_languages.keys():
	print(name.title())

#acessing the value of a key inside a loop

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())
	if name in friends:
		print(f"\t{name.title()}, I see you love {language}!")
	language = favorite_languages[name].title()
	
# keys() can also be used to search if a key was polled
if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

#sorting through Dictionary's keys in particular order

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

# sorted() lists all keys in the dictionary and sort the list
# before the loop
# keys() will return the value of keys
# and finally the loop will print each key

for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll.")

# Looping through all values in a dictionary, when you're interested
# in the values that a dictionary contains, with values()

print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())

# to check for repetitive values use set():
# set() is a collection in which each item must be unique

print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())

# sets can be built directly using braces {}
# dictionary = key + value; sets = only braces and value
# sets don't return items in a specific order

languages = {'python', 'ruby', 'python', 'c'}
print(languages)


# 6 - 4

words = {
	'iterate': 'Iteration is the repetition of a process in order '
	'to generate an outcome',
	'loop': 'In computer programming, a loop is a sequence of '
	'instructions that is continually repeated until a certain '
	'condition is reached',
	'dictionary': 'A dictionary is a general-purpose data '
	'structure for storing a group of objects. A dictionary has '
	'a set of keys and each key has a single associated value.',
	'items()' : 'returns the pair of key-values in a dictionary',
	'keys()' : 'returns the value of each key in a dictionary',
	'sorted()' : 'lists all keys in the dictionary and sort the list',
	'set()' : 'a collection in which each item must be unique.'
	'It can be use to search for reptitive values',

}

for w, m in words.items():
	print(f"\n{w.title()} meaning is: {m}")

# 6 - 5 

rivers = {
	'amazonas' : 'brasil',
	'nilo' : 'egito',
	'mississipi': 'united states of america',
}

for r, c in rivers.items():
	print(f"\nThe {r.title()} runs through {c.title()}.")

for r in rivers.keys():
	print(f"\n{r.title()} is a river in the list.")

for c in rivers.values():
	print(f"\n{c.title()} is a country in which a river is in the list.")

# 6 -6 

pollable = ['jen', 'sarah', 'edward', 'phil', 'coviderson', 'alabamerson']

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

for name in pollable:	
	if name in favorite_languages.keys():
		print(f"\n Thank you for voting {name.title()}!")
	else:
		print(f"\n{name.title()} vote or die bitch.")
