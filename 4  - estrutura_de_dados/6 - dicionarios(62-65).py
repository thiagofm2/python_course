"""
Veremos um pouco sobre dicionários:

Dicionários são uma estrutura de dados que nos permite armazenar os dados e atribuir a eles um fator identificador, ou
seja, é uma estrutura de dados que funciona no sistema 'Chave-Valor', semelhante aos objetos do javascript ou aos
JSON's.
É uma estrutura de dados importantissima para tornar nosso código organizado em determinados pontos quando precisarmos
armazenar uma quantidade de dados grande mas sem perder a identificação deles.

Vamos imaginar em um sistema escolar que armazena as informações de um aluno, como nome, idade, média escolar
"""

studants = {'name': 'Thiago', 'age': 19, 'avg_grade': 7, 'approve_status': True }
print(studants)
print(studants['avg_grade'])


# AULA 63 - Atualizando itens no dicionário
# studants['name'] = 'Tigas'
# print(studants)
#
# studants.update({'nome' : 'Cleber', 'avg_grade': 6})
# print(studants)
#
# studants.update({'address': 'Rua tal'})
# print(studants)
#
# print(studants.get('endereco', 'Este campo não existe'))
#
# del studants['approve_status']
# print(studants)


# AULA 64 - Looping dentro de um dicionário

for keys, values in studants.items():
    print(keys, values)
