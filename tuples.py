#Tuples are immutable lists
#tuples use () instead of brackets []

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

#tuples are defined by a comma; you could build a tuple with one element: 

my_t = (3,)
print(my_t)

#Tuples can also be looped

for dimension in dimensions:
	print(dimension)

#Tuples are immutable but can be reassigned to new values

print('Original dimensions:')
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)

print('\nModified dimensions:')
for dimension in dimensions:
	print(dimension)

#Exercise 4-13

menu = ('Prato Feito', 'Pão', 'Salada', 'Suco', 'Sorvete')

print('\nAs opções de hoje são:')
for prato in menu:
	print(prato)

menu = ('Prato Feito', 'Feijoada', 'Salada', 'Suco', 'Sopa')

print('\nAs opções de amanhã serão:')
for prato in menu:
	print(prato)





