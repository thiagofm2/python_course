# workers = set(['Ana', 'Marcos', 'Alice', 'Pedro', 'Sofia', 'Bruno', 'Melissa'])
# night_time = set(['Ana', 'Marcos', 'Alice', 'Melissa'])
# day_time = set(['Pedro', 'Sophia', 'Bruno'])
# has_car = set(['Marcos', 'Alice', 'Bruno', 'Melissa'])
#
# print(f'Os funcionários que possuem carro e trabalham de noite são: {has_car & night_time}')
# print(f'Os funcionários que possuem carro e trabalham de dia são: {has_car & day_time}')
# print(f'Os funcionários que não possuem carro: {workers - has_car}')

workers = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sofia', 'Bruno', 'Melissa']
night_time = ['Ana', 'Marcos', 'Alice', 'Melissa']
day_time = ['Pedro', 'Sophia', 'Bruno']
has_car = ['Marcos', 'Alice', 'Bruno', 'Melissa']

list1 = set(has_car).intersection(night_time)
list2 = set(has_car).intersection(day_time)
list3 = set(workers).difference(has_car)

print(f'Os funcionários que possuem carro e trabalham de noite são: {list1}')
print(f'Os funcionários que possuem carro e trabalham de dia são: {list2}')
print(f'Os funcionários que não possuem carro: {list3}')
