"""
Vamos ver um pouco sobre a Map Function.
    - Ela é muito utilizado com listas;
    - É utilizada para aplicar uma função a um iterable, por item (list, tuple, dict, etc.).
"""

list1 = [1, 2, 3, 4]

def multi(x):
    return x * 2


list2 = map(multi, list1)

print(list(list2))

# AULA 69 - Função Map com Lambda

print(list(map(lambda x: x * 2, list1)))          # Transformamos todo o código anterior em uma única linha
