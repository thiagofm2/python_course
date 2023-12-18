"""
No ultimo arquivo, vimos como funciona as xargs, quando queremos criar funções com um número indefinido de argumentos,
o que realmente é algo muito positivo quando não temos uma quantia exata de dados para serem usados em uma função.

Mas imagine que temos uma agência de carros, onde precisamos de um código que armazene diversos argumentos, como a
marca do carro, a cor, o motor, tudo isso sem perder a flexibilidade de poder adicionar mais ou menos dados, ou seja,
precisamos que essa função se ja uma xarg.

Porém, se fizermos algo do tipo:

def agency(*car):
    return car

print(agency(marca='Gol', cor='Branca', motor='1.0))

obteremos um erro, pois apesar de IDENTIFICARMOS os argumentos com parâmetros (marca, cor, motor), na hora em que
definimos a função, passamos somente que ela teria um número de argumentos indefinidos, ou seja, que RECEBERIA
um número aleatório de valores, mas não que seria possível criar um número aleatório de parâmetros para armazená-los.

Para driblar isso é simples, basta adicionarmos somente um * a mais em nossa função:
"""

def agency(**car):
    return car


print(agency(marca='Gol', cor='Branca', motor=1.0))

"""
Com isto, será criado um Dicionário onde irá armazenar a chave (marca, cor, motor) e os valores (Gol, Branca, 1.0).
"""
