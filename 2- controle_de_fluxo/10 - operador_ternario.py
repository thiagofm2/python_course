"""
Veremos sobre operadores ternários e como ele facilita nosso trabalho resumindo expressões de If e Else.

Faremos um programa para verificar a idade de votação eleitoral de uma pessoa, considerando que a idade minima é de
16 anos de idade.
"""

age = int(input("Digite sua idade: "))
permission = 'Voto permitido' if age >= 16 else 'Voto não permitido.'
print(permission)
