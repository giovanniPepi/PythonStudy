#Using if statements with lists

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	print(f'Adding {requested_topping}.')

print(f'\nFinished making your pizza!\n')

#what if we run out of green peppers?

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print(f'Sorry, we\'re out of green peppers right now.')
else:
	print(f'Adding {requested_topping}.')

print(f'\nFinished making your pizza!\n')

#checking empty lists
# using IF, Python returns True if the list contains at least one item
#empty lists would return false

requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		print(f'Adding {requested_topping}.')
	print('\nFinished making your pizza!')
else:
	print('Are you sure you want a plain pizza?\n')
	
# multiple lists

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f'Adding {requested_topping}.')
	else:
		print(f'Sorry, we don\'t have {requested_topping}.')

print('\nFinished making your pizza!')

#5_8

usernames = ['john', 'admin', 'carl', 'linda', 'sylvie']

for user in usernames:
	if user == 'admin':
		print(f'Welcome Admin, would you like to see the status report?')
	else:
		print(f'Welcome {user}, thank you for logging in!')

#5-9

usernames = []

if usernames:
	for user in usernames:
		if user == 'admin':
			print(f'Welcome Admin, would you like to see the status report?')
		else:
			print(f'Welcome {user}, thank you for logging in!')
else:
	print(f'\nThere are no registered users!')

#5-10
#Registered users are in lowercase, how to revert back to the original?

current_users = ['John', 'admin', 'Carl', 'linda', 'sylvie']
requested_new_users = ['Carl', 'LordSucker', 'Lord of Darkness', 'EdgeLord']

#converts to lower case to see if user already registered

current_users = [current_user.lower() for current_user in current_users]
new_users = [new_user.lower() for new_user in requested_new_users]

for new_user in new_users:
	if new_user in current_users:
		print(f'\nUsername requested already in use.')
	else:
		print(f'\nUsername {new_user.title()} available.')

#5-11

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
	if number == 1:
		print(f'{number}st')
	elif number == 2:
		print(f'{number}nd')
	elif number == 3: 
		print(f'{number}rd')
	else:
		print(f'{number}th')


