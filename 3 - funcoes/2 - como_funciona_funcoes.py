"""
O conceito de funções segue o princípio DRY - Don't Repeat Yourself, para que o código fique limpo, sem redundância
e fácil de ler.
"""

def printHello(response):
    print(f"Olá {response}, seja bem vindo! \nEsta é uma função Python!")

name = input("Digite seu nome: ")
printHello(name)
