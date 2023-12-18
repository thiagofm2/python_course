"""
Vamos entender um pouco sobre a funcionalidade das funções:
Funções basicamente fazem duas coisas: Ou elas fazem uma tarefa, ou elas retornam um valor

Um exemplo de função que faz uma tarefa, é uma função que emite print(), já uma função que retorna um valor é algo do
tipo "dê esse valor".

O exemplo abaixo mostra uma função que somente fazem uma tarefa, no caso realiza o print.
"""

def client1(name):
    print(f'Olá, {name}')


name = input("Digite seu nome: ")
client1(name)

"""
Como podemos ver, ele somente realiza o print do nome do usuário, mas não retorna um valor e nem armazena nada.
Para conferir, podemos fazer um print(client1(name)), e veremos que o resultado será 'None'.

Agora, se quiséssemos que a função RETORNASSE um valor, deveríamos fazer do seguinte jeito:
"""

def client2(name):
    return f'Olá {name}'


name2 = input("Digite seu nome: ")
print(client2(name2))
