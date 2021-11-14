#Lists are used to store items in a particular order

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print (bicycles)
print (bicycles[0])

#Using strings methods: 
print (bicycles[0].title())
print (bicycles[0].upper())

#last element can be acessed with -1 
print (bicycles[-1])

#elements can also be acessed from the last position:
print (bicycles[-3])

#using with f-strings:
message = f"My first bicycle was a {bicycles[0].title()}."
print (message)

#Modifying Elements in a list

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Esse código altera o primeiro item da lista

motorcycles[0] = 'ducati'
print(motorcycles)

# Append adds items to the end of the list dinamycally

motorcycles.append('MOTO DO IFOOD')
print(motorcycles)


UpperLeg = []

UpperLeg.append('Quadriceps')
UpperLeg.append('Biceps Femural')
UpperLeg.append('Abdutor')
UpperLeg.append('Adutor')

print(UpperLeg)

#Using insert to insert itens on a position, in this case the beginning of the list

UpperLeg.insert(0, 'Coxa')

print(UpperLeg)

# Removing items from a list
#If you know the position = del; you can no longer acess the deleted item

del UpperLeg[0]
print(UpperLeg)

del UpperLeg[3]
print(UpperLeg)



# pop() removes the last item and you can work with it

print('POP')

popped_UpperLeg = UpperLeg.pop()
print(UpperLeg)
print(popped_UpperLeg)

UpperLeg.insert(0, 'Joelho')
print(UpperLeg)

last_muscle = UpperLeg.pop()
print(f"The last added muscle is {last_muscle.title()}")

# pop() in other positions

first_owned = motorcycles.pop(0)
print(f" The first motorcycle I owned was a {first_owned.title()}.")

# del = delete and not use; pop() = delete from list and use it; either way the item gets removed from the list

#Remove by value using "Remove"
#If the item appears more than once, you should use a loop to remove it 

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

#can also be used to print a reason why it's being removed

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

