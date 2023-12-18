"""
Listas são formas de armazenarmos uma grande quantidade de dados em uma única variável.
"""

cities = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador']
numbers = [5, 8, 9, 6]

print(cities)

"""
Para acessar um item específico da lista, nós acessamos pelo index do item, lembrando que toda lista começa pelo
index 0.
"""

print(cities[1])        # Rio de Janeiro

"""
O mesmo vale com valores negativos, onde no caso acessaremos os últimos elementos:
"""

print(cities[-1])       # Salvador

"""
Podemos trocar um dado em uma lista através do index
"""

cities[2] = 'São José dos Campos'
print(cities)

"""
Existem diversas funções para listas, como o .append(), que adiciona um item no final da lista, o .remove(), que remove
o item da lista que passarmos entre parênteses. Temos o insert(), que insere o item que quisermos na posição que 
que informarmos.
.pop() remove um item e o retorna. O .sort() retorna a lista em ordem alfabética.

Podemos juntar duas listas também, ou seja, concatená-las:
"""

concatedLists = cities + numbers
print(concatedLists)

"""
Podemos criar listas dentro de listas, e acessar os itens através dos index:
"""

listOflist = [[2,3,4], [5,6,7]]
print(listOflist[1][2])         # 7

"""
Podemos extrair variáveis de dentro de listas, como ocorre de maneira semelhante no Javascript com o destructuring, onde
podemos extrair dados de listas e anexá-los em variáveis.
É importante lembrar que o número de variáveis deve ser compatível com o número de elementos dentro de uma lista, e
caso não necessitemos separar todos os elementos dentro de uma variável, podemos simplesmente criar uma variável com
asterisco na frente que receba todos os outros elementos.
"""

city1, city2, *others = cities
print(city1)
print(city2)
print(others)


