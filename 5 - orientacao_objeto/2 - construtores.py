"""
Vamos trabalhar com construtores, que é algo que nos permitirá passar os parâmetros como argumentos da classe, nos
permitindo muito mais agilidade.

Vejamos abaixo o funcionamento, utilizando o mesmo exemplo com a classe Workers.
"""

class Workers:
    def __init__(self, name, last_name, birthdate):
        self.name = name
        self.last_name = last_name
        self.birthdate = birthdate


user1 = Workers('Thiago', 'Faria', '02/04/2004')
user2 = Workers('Bruna', 'Alves', '21/06/2003')

print(user1.name)
print(user2.last_name)
