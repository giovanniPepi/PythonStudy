
for value in range(1, 5):
	print(value)

#can also be used with only one argument as the end, it will start counting at 0:

for value in range(6):
	print(value)

#converting to a list

numbers = list(range(1, 6))
print(numbers)

#range can also have a third argument 

even_numbers = list(range(2, 11, 2))
print(even_numbers)

odd_numbers = list(range(1, 10, 2))
print(odd_numbers)

# using it to list square numbers. ** = exponents

squares = []
for value in range(1, 11):
	square = value ** 2
	squares.append(square)
print(squares)

cubes = []
for value in range(1, 11):
	cube = value ** 3
	cubes.append(cube)
print(cubes)

#simplified code with one less variable
#sometimes you may want to use one more variable to keep the code easier to read

squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)

cubes = []
for value in range(1, 11):
	cubes.append(value**3)
print(cubes)

#statistics with lists

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

print(f'\nThe first three items in the digits list is {digits[:3]}')
print(f'\n~Three items from the middle of the list are {digits[4:7]}')
print(f'\nThe last three items in the list are: {digits[-3:]}')