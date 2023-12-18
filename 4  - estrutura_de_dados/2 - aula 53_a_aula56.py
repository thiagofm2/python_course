# AULA 53 - Looping dentro de uma lista

# values = [50, 20, 3, 5, 9]
#
# for numbers in values:
#     print(f'The number printed now is: {numbers}')




# AULA 54 - Verificando itens em uma lista

# colors = ['blue', 'orange', 'red', 'green']
# input_user = input("Pesquise por alguma cor em estoque: ")
#
# if input_user.lower() in colors:
#     print("A cor está em estoque")
# else:
#     print("A cor não está em estoque")




# AULA 55 - Agregando duas listas com Zip

"""
Já vimos como concatenar duas listas, ou seja, como juntar os itens de duas listas em uma só, mas nós também podemos
juntar as listas de uma forma diferente caso precisamos organizar os elementos em determinada posição.
Por exemplo, se quisermos que os elementos da lista se juntem por sua posição:

list1 = [1, 2, 3, 4]
list2 = ['primeiro', 'segundo', 'terceiro', 'quarto']

e queremos obter um resultado do tipo [(1, 'primeiro'), (2, 'segundo'), (3, 'terceiro'), (4, 'quarto')]
ou seja, quando quisermos juntar os elementos pelos índices.
"""

list1 = [1, 2, 3, 4]
list2 = ['primeiro', 'segundo', 'terceiro', 'quarto']
group_lists = zip(list1, list2)

print(list(group_lists))




# AULA 56 - Input em uma lista

user_fruits = input('Digite as frutas que estarão em sua lista (separados por vírgula): ')
fruits_list = user_fruits.split(', ')

print(fruits_list)
