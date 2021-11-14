import random

comida_01 = {
    'pastel': 'R$8',
    'lanche da feira': 'R$25',
    'comida padaria': 'R$25',
}

comida_02 = {
    'pizza nostra': 'R$65',
    'dominos': 'R$80',
    'mana poke': 'R$40',
}

comida_03 = {
    'olive garden': 'R$180',
    'cocô bambu': 'R$200',
    'outback': 'R$200',
}

def escolher_comida (preço):
    """Retorna o que comer com base no preço"""
  
    if preço == '1':
        print (f"Hoje comeremos {random.choice(list(comida_01.items()))}.")

    elif preço == '2':   
        print (f"Hoje comeremos {random.choice(list(comida_02.items()))}.")

    elif preço == '3':
        print (f"Hoje comeremos {random.choice(list(comida_03.items()))}.")
    else:
        print(f"Digite um valor válido: 1, 2 ou 3.")


while True:

    preço = escolher_comida(input(f"\nEscolha o nível de preço. Níveis de preço 1 = R$1 a R$30, 2 = R$30 a R$80, 3 = R$80 em diante.\n"))




