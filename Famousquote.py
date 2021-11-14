famous_person = 'Albert Einstein'
famous_quote = 'once said "A person who never made a mistake never tried anything new"'

message = f'{famous_person} {famous_quote}'
print(message)

person_name = '    \tGiovanni'
person_last_name = '  Tieghi Pepi\n'
print(f'{person_name}{person_last_name}')

person_name = '    Giovanni '
person_last_name = 'Tieghi Pepi       '
person_name = person_name.lstrip()
person_last_name = person_last_name.rstrip()
print(f'{person_name}{person_last_name}')

