from array import array

"""
Vamos começar a utilizar o Array (matriz), uma estrutura de dados que é muito confundido com as listas.
Mas quando então utilizar um array? Simples, quando nós possuirmos uma quantidade muito grande de dados a serem
armazenados, como milhares de dados. Utilizando arrays a performance do nosso código melhora.

Array não é uma estrutura de dado padrão do Python, então devemos importá-la antes de iniciar seu uso.
"""

letters = ['a', 'b', 'c', 'd']
numbers1 = [10, 20, 30, 40]
numbers2 = [1.2, 1.3, 1.4, 1.5]

print(letters)
print(numbers1)
print(numbers2)


letterArray = array('u', ['a', 'b', 'c', 'd'])
intArray = array('i', [10, 20, 30, 40])
floatArray = array('f', [1.2, 1.3, 1.4, 1.5])

print(letterArray)
print(intArray)
print(floatArray)

"""
Como podemos ver acima, o método array() precisa de dois parâmetros principais, o type code da lista, ou seja, se é
string, se é inteiro, float etc. E em seguida é necessário a lista em si.
O type code podemos adquirir pesquisando no google sobre este método array para python.
"""
