"""
Entraremos agora no estudo de Programação Orientada a Objetos com Python. Para iniciar nesse assunto, primeiro devemos
falar sobre as Classes.
    - São utilizadas pra criar objetos (instances);
    - Objetos são partes dentro de uma Class (instancias);
    - Classes são utilizadas para agrupar dados e funções, podendo reutilizá-las;

    Por exemplo:
    Class: Frutas
    Objects: Abacate, Banana...
"""

# CRIANDO A PRIMEIRA CLASSE E COLOCANDO DADOS
# class Workers:
#     name = ''
#     last_name = ''
#     birthdate = ''
#
#
# user = Workers()
# user.name = input("Digite seu nome: ")
# user.last_name = input("Digite seu sobrenome: ")
#
# print(user.name)
# print(user.last_name)


# CRIANDO OBJETOS DENTRO DE UMA CLASSE

class Workers:
    pass            # Este atributo pass, permite com que nós criemos uma classe vazia.


user = Workers()
user2 = Workers()

user.name = input("Digite seu nome: ")
user.last_name = input("Digite seu sobrenome: ")
user2.name = 'Washington'
user2.last_name = 'Brasileiro'

print(user.name)
print(user.last_name)
print(user2.name)
print(user2.last_name)
