"""
Vamos utilizar as funções Lambda.
    - É uma função pequena e sem nome;
    - Pode ter vários argumentos, mas somente uma expressão;
    - É muito utilizada dentro de outras funções;
    - Deixa o código mais limpo.
"""

def somar(x):                       # Assim declaramos uma função padrão, onde desejamos retornar um número + 10
    return x + 10


add10 = lambda x: x + 10            # Uma alternativa com função lambda, onde criamos ela e declaramos em uma variável

print(somar(2))
print(add10(2))


# AULA 67 - Lambda dentro de uma função

def somar2(x):
    funcLamb = lambda x: x + 10
    return funcLamb(x) * 4


print(somar2(5))
