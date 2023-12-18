"""
Vamos ver como funciona uma tupla (tuple):

Assim como uma lista, uma tuple serve para armazenar mais de um dado em uma variável, com a diferença de que a tuple
é imutável. Para criar uma tuple, basta trocarmos os colchetes (square brackets) [] de uma lista por parenteses
()
"""

colors_list = ['blue', 'green', 'purple']
colors_tuple = ('blue', 'green', 'purple')


colors_list.append('red')       # Adicionará um elemento a lista.
colors.tuple.append('red')      # RETORNARÁ ERRO

"""
Ou seja, uma tupla não pode sofrer mutações, diferentemente das listas, então ela deve ser usada nos casos onde nós
não iremos alterar os dados que formos usar, por questões de segurança e também de processamento, já que uma lista é
mais pesada de se armazenar, e mais lenta de se utilizar.
"""
