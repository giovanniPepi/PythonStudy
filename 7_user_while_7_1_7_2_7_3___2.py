# input is treated as str by default
# using int()

age = input("How old are you? ")
age = int(age)


height = input("How tall are you, in cm? ")
height = int(height)

if height >= 100:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# Modulo Operator '%'
# can be used to check if a number is divisi ble by another number

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

