cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

#'==' is an equality operator and checks if the values on the left and
#right side of the operator match

#equality is case sensitive; if case matters you can convert:

car = 'Audi'
car.lower == 'audi'

#checking for inequality !=

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
	print("Hold the anchovies!")

answer = 17

if answer != 42:
	print('That is not the correct answer. Please try again!')
	
#checking wether a value is not in a list

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
	print(f'{user.title()}, you can post a response if you wish.')


car = 'subaru'
print("is car == 'subaru'? I predict True.")
print(car == 'subaru')

age = 27

if age >= 27:
	print(f'You\'re old at {age}!')
else:
	print(f'You\'re young at {age}!')

ages = [18, 27, 117, 10, 15, 16, 17, 30, 45, 99, 24, 20, 110]

for age in ages:
	if age >= 27 and age <=100:
		print(f'\nYou\'re old at {age}!')
	else:
		if age <=26:
			print(f'\nYou\'re young at {age}!')
		else:
			print(f'\nHoly shit how are you even alive at {age}?')

pizzas = ['Portuguesa', 'Marguerita', 'Siciliana', 'Calabresa']

for pizza in pizzas:
	if pizza == 'Portuguesa':
		print(f'Delicious {pizza}')
	else:
		print(f'Disgusting {pizza}')

#inverso

pizzas = ['Portuguesa', 'Marguerita', 'Siciliana', 'Calabresa', 'portuguesa']

for pizza in pizzas:
	if pizza != 'Portuguesa':
		print(f'\nDelicious {pizza}')
	else:
		print(f'\nDisgusting {pizza}')

#lower

pizzas = ['Portuguesa', 'Marguerita', 'Siciliana', 'Calabresa', 'portuguesa']

for pizza in pizzas:
	if pizza.lower() == 'portuguesa':
		print(f'\nDelicious {pizza}')
	else:
		print(f'\nDisgusting {pizza}')

#or

pizzas = ['Portuguesa', 'Marguerita', 'Siciliana', 'Calabresa', 'portuguesa']

for pizza in pizzas:
	if pizza.lower() == 'portuguesa' or pizza.lower() == 'siciliana':
		print(f'\nDelicious {pizza}')
	else:
		print(f'\n  Disgusting {pizza}')

#and (all will be False)

pizzas = ['Portuguesa', 'Marguerita', 'Siciliana', 'Calabresa', 'portuguesa', 'Portuguesa Siciliana']

for pizza in pizzas:
	if pizza.lower() == 'portuguesa' and pizza.lower() == 'siciliana':
		print(f'\nDelicious {pizza}')
	else:
		print(f'\n  Disgusting {pizza}')

#checking if item is on a list

cores = ['Azul', 'Verde', 'Vermelho', 'Amarelo', 'Violeta']

cor = 'Azul Turquesa'

if cor in cores:
	print(f'A {cor} está na lista')
else:
	print(f'A cor {cor} não está na lista')

# Not in a list

cor = 'Azul Turquesa'

if cor not in cores:
	print(f'\nA cor {cor} não está na lista')
else:
	print(f'\nA cor {cor} está na lista')

print('\n ')

#Continuing If... 

age = 17

if age >= 18:
	print('You\'re old enough to vote!')
	print('Haver you registered to vote yet?\n')
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!\n")

#elif

age = 12

if age < 4:
	print('Your admission cost is $0.')
elif age <18:
	print('Your admission cost is $25.')
else:
	print('Your admission cost is $40.')

#a simpler way: 

age = 12

if age < 4:
	price = 0
elif age <18:
	price = 25
else:
	price = 40

print (f'\nYour admission cost is ${price}.\n')

#adding another elif to discount

age = 70

if age < 4:
	price = 0
elif age <18:
	price = 25
elif age < 65:
	price = 40
else:
	price = 20

print (f'\nYour admission cost is ${price}.\n')

#doing the same without 'else'
#avoid usign else as it is a 'catchall'statement for anything that does
#not pass the test and could be used for invalid/malicious purposes

age = 70

if age < 4:
	price = 0
elif age <18:
	price = 25
elif age < 65:
	price = 40
elif age >= 65:
	price = 20
	
print (f'\nYour admission cost is ${price}.\n')

# multiple conditions

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
	print('Adding mushrooms.')
if 'pepperooni' in requested_toppings:
	print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
	print('Adding extra cheese.')
	
print(f'\nFinished making you pizza!')