# AULA 16 - Praticando com Strings e Integers

# nome = 'Thiago'
# idade = 19
# cidade = 'São José dos Campos'
# print(f'O nome do rapaz é {nome}, ele tem {idade} anos de idade e mora na cidade de {cidade}')

"""
É importante lembrar que em um print() sem formated strings, não podemos concatenar strings com outros tipos de dados.
"""

# AULA 17 - Adicionando Input
# nome = input("Digite seu nome: ")
# idade = int(input("Digite sua idade: "))
# cidade = input("Digite a cidade que você mora: ")
#
# print(f'O nome do rapaz é {nome}, ele tem {idade} anos de idade e mora na cidade de {cidade}')

# AULA 18 - Calculando a idade com o input
# ano_nascimento = int(input("Digite o ano em que você nasceu: "))
# calculo = 2023 - ano_nascimento

# print(f"Você tem {calculo} anos de idade.")

# AULA 19 - Entendendo o Slice
"""
Slice é uma forma de conseguirmos obter determinado dado ou valor de alguma outra variável, sem precisar pegar
todo o montante do dado. Por exemplo:
"""
fruta = 'Abacate'
print(fruta[2:6])         # Retorna a string "acat"
print(fruta[-1])          # Retorna a letra 'e', pois pega o inverso.

# AULA 21 - Métodos para Strings

message = 'Isto é uma mensagem'

print(message.lower())      # Tudo em minúsculo.
print(message.upper())      # Tudo em maiúsculo.
print(message.capitalize()) # Primeira letra da frase em maiúsculo.
print(message.find('o'))    # Tudo em minúsculo.
print(message.replace("mensagem","porra"))  # Troca de letras ou palavras.
