#copying a list
#slice can be used to include the whole list

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_pizzas = my_foods[:]
print(f'\nMy favorite pizzas are: {my_pizzas}')
friend_pizzas = my_pizzas[:]
print(f'\nMy friend\'s favorite pizzas are: {friend_pizzas}')
my_pizzas.append('Marguerita')
friend_pizzas.append('Lombo')
print(f'\nMy favorite pizzas are: {my_pizzas}')
print(f'\nMy friend\'s favorite pizzas are: {friend_pizzas}')

for pizza in my_pizzas:
	print(f'\nOne of my favorite pizzas is: {pizza}')
