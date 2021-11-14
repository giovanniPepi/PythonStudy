#for loop
#for pulls a name from the list, associate it with a new variable
# 'magician' and print it

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)

for magician in magicians:
	print(f'{magician.title()}, that was a great trick!')
	print(f'I can\'t wait to see your next trick, {magician.title()}\n')
	
#messages outside the indentation are only displayed once

for magician in magicians:
	print(f'{magician.title()}, that was a great trick!')
	print(f'I can\'t wait to see your next trick, {magician.title()}\n')
print("Thank you everyone. That was a great magic show!")

pizzas = ['Portuguesa', 'Frango', 'Frango com Catupiry', 'Milho', 'Marguerita']
for pizza in pizzas:
	print(f'\nI fucking love pizza {pizza}!')
print("\nThat was it, I love them all!")

pets = ['Dog', 'Cat', 'Cockatiel', 'Hamster']
for pet in pets:
	print(f'\nA {pet} would make a great pet!')
print("\nActually every one of these would make great pets!")
