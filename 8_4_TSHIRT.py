def make_tshirt(phrase = 'I love Python', size = 'GG'):
    '''Creates a large Tshirt with a random phrase.'''
    print(f"Creating a T shirt size {size} with the phrase "
    f"{phrase.title()}.")

make_tshirt()
make_tshirt(size = 'M')
make_tshirt(phrase='1987 MONKE REMEMBA CLUB')