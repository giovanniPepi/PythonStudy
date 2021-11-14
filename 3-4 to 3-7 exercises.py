
dinner_invite = ['Albert Einstein', 'Plato', 'Alexander the Great', 'Someone\'s uncle']
print(dinner_invite)

print(f"Welcome the the epic dinner, {dinner_invite[0]} !")
print(f"Welcome the the epic dinner, {dinner_invite[1]} !")
print(f"Welcome the the epic dinner, {dinner_invite[2]} !")
print(f"Welcome the the epic dinner, {dinner_invite[3]} !")

cannot_come = dinner_invite.pop(3)
print(f"{cannot_come} will not be able to attend the epic dinner. Those who are comming are: {dinner_invite}")

dinner_invite.insert(3, 'Gandhi')
print(dinner_invite)

print(f"Welcome the the epic dinner, {dinner_invite[0]} !")
print(f"Welcome the the epic dinner, {dinner_invite[1]} !")
print(f"Welcome the the epic dinner, {dinner_invite[2]} !")
print(f"Welcome the the epic dinner, {dinner_invite[3]} !")

print(f"We have found a bigger dinner table!")

dinner_invite.insert(0, 'Zeus')
dinner_invite.insert(3, 'Caesar')
dinner_invite.append('Hitler')
print(dinner_invite)

print(f"Welcome the the epic dinner, {dinner_invite[0]} !")
print(f"Welcome the the epic dinner, {dinner_invite[1]} !")
print(f"Welcome the the epic dinner, {dinner_invite[2]} !")
print(f"Welcome the the epic dinner, {dinner_invite[3]} !")
print(f"Welcome the the epic dinner, {dinner_invite[4]} !")
print(f"Welcome the the epic dinner, {dinner_invite[5]} !")
print(f"Welcome the the epic dinner, {dinner_invite[6]} !")

print('Now only 2 people will be invited')

removido = dinner_invite.pop(0)
print(f"I'm sorry {removido}, you're no longer invited. ")
removido = dinner_invite.pop(1)
print(f"I'm sorry {removido}, you're no longer invited. ")
removido = dinner_invite.pop(4)
print(f"I'm sorry {removido}, you're no longer invited. Also fuck you.")
removido = dinner_invite.pop(1)
print(f"I'm sorry {removido}, you're no longer invited. ")
removido = dinner_invite.pop(2)
print(f"I'm sorry {removido}, you're no longer invited. ")
print(dinner_invite)

del dinner_invite[0]
del dinner_invite[0]
print(dinner_invite)
