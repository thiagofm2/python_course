"""
Como já podemos ter experenciado anteriormente, sempre que ocorre um erro no Python, ele simplesmente reporta o erro
e cancela o fluxo do código, nos obrigando a ter que reparar o erro antes de dar continuidade, ou até mesmo exibir uma
alternativa/explicação tratada.

Veremos então como tratar estes erros, afim de poder manipular melhor os eventos de nosso código.
"""


# TRABALHANDO COM O TRY E O EXCEPT EM UMA LISTA

try:
    list = [1, 2, 4, 5]
    print(list[10])
except IndexError:
    print("Índice não encontrado. Verifique se a posição do dado acessado está correta.")


# TRABALHANDO COM O TRY E O EXCEPT EM UM INPUT

try:
    value = int(input("Digite um valor numérico: "))
    print(value)
except ValueError:
    print("O valor digitado não é um número.")


# ADICIONANDO ELSE E FINALLY

try:
    value = int(input("Digite um valor numérico: "))
    print(value)
except ValueError:
    print("O valor digitado não é um número.")
# else:
#     if value == 2:
#         print("Belo número. Esta mensagem só executa se não houver erro.")
finally:
    print("Essa mensagem vai executar de qualquer forma")
