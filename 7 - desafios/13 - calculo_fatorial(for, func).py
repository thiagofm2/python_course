def fact_calc(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * fact_calc(number - 1)


numb_to_calc = int(input("Digite um número para obter seu fatorial: "))
print(f'O fatorial de {numb_to_calc} é {fact_calc(numb_to_calc)}')
