print("Python")

# adicionada espaço de tab = \t

print("\tPython")

# adiciona espaço de uma linha = \n

print("Languages:\nPython\nC\nJavaScript\n")

# combinados

print("Languages:\n\tPython\n\tC\n\tJavaScript\n")

# .rstrip() verifica se há espaço em branco na direita de uma string:
#  para retirar o espaço em branco, basta associar rstrip à variável

favorite_language = 'python '
print(favorite_language)

favorite_language = 'python       '
favorite_language = favorite_language.rstrip()
print(favorite_language)

# strip retira espaço em ambos lados; rstrip direita, lstrip esquerda
# utilizado para limpar dados imputados por usuários

favorite_language = '   python'
favorite_language = favorite_language.lstrip()
print(favorite_language)

favorite_language = '          python       '
favorite_language = favorite_language.strip()
print(favorite_language)
