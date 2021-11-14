#list compreheinsion combines the for loop and the creation of new 
#elements into one line and automatically appends each new element

squares = [value**2 for value in range(1,11)]
print(squares)

cubes = [value**3 for value in range(1,11)]
print(cubes)

twenty = [value + 1 for value in range(0,20)]
print(twenty)

million = [value +1 for value in range(0, 1000000)]

odd_numbers = list(range(0, 21, 2))
print(odd_numbers)

Threes = [value for value in range (0, 30, 3)]
print(Threes)

