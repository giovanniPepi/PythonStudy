visit = ['Guarujá', 'Orlando', 'Roma', 'New York', 'Paris']
print(f'\nCidades para visitar: {visit}')

print(f'\nCidades para visitar em ordem alfabética: {sorted(visit)}')
print(f'\nLista original: {visit}')

print(f'\nCidades para visitar em ordem \
	alfabética inversa: {sorted(visit, reverse=True)}')
print(f'\nLista original: {visit}')

visit.sort(reverse=True)
print(f'\nCidades para visitar em ordem alfabética inversa: {visit}')
print(f'\nLista original foi alterada pelo reverse(): {visit}')

visit = ['Guarujá', 'Orlando', 'Roma', 'New York', 'Paris']
print(f'\nLista original: {visit}')

visit.sort()
print(f'\nCidades para visitar em ordem alfabética: {visit}')
print(f'\nLista original foi alterada: {visit}')


visit.sort(reverse=True)
print(f'\nCidades para visitar em ordem alfabética inversa: {visit}')

dinner_invite = ['Albert Einstein', 'Plato', 'Alexander the Great',\
 'Someone\'s uncle']
print(f'The number of invited people to the epic dinner\
 is {len(dinner_invite)}')

cidades_regiao = ['Sumaré', 'Campinas', 'Americana', 'Nova Odessa', \
'Vinhedo', 'Valinhos', 'Santa Barbara D\'oeste', 'Itatiba']
print(f'\nAs cidades da região são: {cidades_regiao}')

print(f'\nAs cidades da região em ordem alfabética\
 são: {sorted(cidades_regiao)}')
print(f'\nAs cidades da região em ordem alfabética inversa\
 são: {sorted(cidades_regiao, reverse=True)}')

cidades_regiao.sort()
print(f'\nAs cidades da região em ordem alfabética são: {cidades_regiao}')

cidades_regiao.sort(reverse=True)
print(f'\nAs cidades da região em ordem alfabética inversa\
 são: {cidades_regiao}')