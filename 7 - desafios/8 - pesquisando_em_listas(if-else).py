car_list = ['BMW X6', 'BMW I5', 'BMW I8']
search = input("Digite o nome do carro que deseja: ")

if search in car_list:
    print(f'{search} está disponível para venda.')
else:
    print('O carro procurado não está disponível.')
