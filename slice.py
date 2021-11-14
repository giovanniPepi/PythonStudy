players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

print(players[1:4])
print(players[:4])
print(players[2:])

#Output the last three items on a list:

print(players[-3:])

#third argument tells how many items to skip

print(players[1:3:1])

#Looping trhough slices

print('\nHere are the frist three players on my team:')
for player in players[:3]:
	print(player.title())

