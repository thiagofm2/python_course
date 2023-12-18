"""
Assim como a função map, a função filter é muito utilizada com listas, porem ao ser aplicada a um iterable ela filtra
os items
"""

values = [10, 12, 13, 45, 6]

def filter_above_twenty(x):
    return x > 20


print(list(filter(filter_above_twenty, values)))

# Ou se não, podemos fazer com uma função lambda, para diminuir o tamanho do código.

print(list(filter(lambda x : x > 20, values)))
