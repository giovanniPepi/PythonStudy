#sort() is used to permanently sort a list
#this works nicely for lowercase values; upper/lower will be dealt in future lessons

cars = ['bmw', 'audi', 'toyota']
cars.sort()
print(cars)

#reverse
#must use uppercase

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

#sorted() temporarily sorts the list, maintains the original list

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"\nHere is the original list: {cars}")

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the reverse sorted list:")
print(sorted(cars, reverse=True))

print(f"\nHere is the original list again: {cars}")

#reverse() to permanently change the list
#use reverse() to change it again

cidades = ['Thais', 'Carlin', 'Ab\'dendriel', 'Venore', 'Kazordoon', 'Edron']
print(f"\n{cidades}")

cidades.reverse()
print(f"\n{cidades}")

cidades.reverse()
print(f"\n{cidades}")

#len() finds the lenght of the list

print(len(cidades))
