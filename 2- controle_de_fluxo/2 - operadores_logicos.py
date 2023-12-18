""""
Nesta aula iremos praticar os operadores lógicos, pensando em um algoritmo que seja utilizado em um banco, com a
finalidade de conceder um empréstimo a um cliente.
Para isto, o banco precisa analisar se o cliente possui o nome limpo e uma renda mensal superior a R$ 5.000,00.

Podemos usar os operadores 'and' ou 'or', além dos operadores booleanos True ou False.
"""

mensal_worth = int(input("Digite o valor de sua renda mensal: "))
print("Possui nome limpo? \n1 - SIM \n2 - NÃO")
clean_name = int(input("Selecione uma das opções acima: "))


if mensal_worth >= 5000 and clean_name == 1:
    print("Empréstimo Aprovado.")
elif clean_name != 1 and clean_name != 2:
    print("A opção selecionada é inválida.")
else:
    print("Empréstimo negado.")
