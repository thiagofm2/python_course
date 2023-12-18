"""
Veremos agora sobre como funciona os 'sets'.

Os sets servem quando precisamos de uma estrutura que consiga armazenar muitos dados, porém eles necessitam ser dados
únicos, ou seja, não podem ser duplicados.
Além disso, é importante ressaltar que o set não utiliza index.
"""

# list1 = [10, 20, 30, 40, 50]
# list2 = [10, 20, 60, 70]
#
# num1 = set(list1)
# num2 = set(list2)
#
# print(num1)
# print(num1 | num2)          # Este operador significa Union, ou seja, se juntam sem repetir dados
# print(num1 - num2)          # Este operador se chama Difference, que mostra os dados diferentes entre dois sets.
# print(num1 ^ num2)          # Este operador se chama Symmetric, e ele retira os dados repetidos das duas listas.
# print(num1 & num2)          # Este operador se chama And, e mostra o que está duplicado em um set e em outro.
# print(len(num1))            # Mostra quantos dados tem no set.


# AULA 60 - Funções em sets
# set_example = {1, 2, 3, 4, 5}
# set_example.add(7)                      # Adiciona um valor
# set_example.update([6, 8, 9, 10])       # Adiciona mais de um valor no set
# set_example.remove(10)                  # Remove um item do set
# set_example.discard(3)                  # Também remove um item do set, mas sem reportar erro caso o item não exista.
#
# print(set_example)

# AULA 61 - Sets com strings

set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}
set4 = set1.union(set2)
set5 = set1.difference(set3)
set6 = set1.intersection(set2)
set7 = set1.symmetric_difference(set3)

print(set4)
print(set5)
print(set6)
print(set7)
