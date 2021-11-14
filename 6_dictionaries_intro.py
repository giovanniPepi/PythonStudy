#Dictionaries have key + value. Keys can be anything, even
#another dictionary

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

#using it

new_points = alien_0['points']
print(f'\nYou just earned {new_points} points!')

alien_0['x position'] = 0
alien_0['y position'] = 25
print(alien_0)

# changing values

alien_0['color'] = 'yellow'
print(f"\nThe alien is now {alien_0['color']}.")

# //

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	# This must be a fast alien.
	x_increment = 3

# New position is hte old position plus increment. 

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New Position: {alien_0['x_position']}")

# deleting a key-value pair

alien_0 = {'color': 'green', 'points': 5}
del alien_0 ['points']
prin0t(alien_)

# Dictionary of similar objects - press enter after opening the first {

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")




