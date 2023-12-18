"""
List Comprehension é uma forma mais simples de se escrever quando precisamos criar uma nova lista a partir de uma
existente
"""

# A forma "antiga", seria esta, usando um for e um list separado.
fruits = ['banana', 'apple', 'pear', 'orange']
fruits2 = []

for itens in fruits:
    if 'b' in itens:
        fruits2.append(itens)

print(fruits2)


# Usando o List Comprehensions, ficaria desta forma:
fruits3 = [itens for itens in fruits if 'b' in itens]
print(fruits3)



# AULA 72 - Entendendo List Comprehension com números

values = []

for x in range(6):
    values.append(x * 10)

print(values)

values2 = [ x * 10 for x in range(6)]
print(values2)
