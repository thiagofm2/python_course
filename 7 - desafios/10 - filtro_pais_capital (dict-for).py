country_capital = {
    'Brasil':'Brasília',
    'Japão':'Tóquio',
    'China': 'Pequim',
    'Rússia': 'Moscou',
    'Alemanha': 'Berlim'
}

user_search = input("Procure por um país: ")
if user_search in country_capital.keys():
    capital = country_capital.get(user_search)
    print(f"O País {user_search} está cadastrado! Sua capital é: {capital}")
else:
    print("País não encontrado.")
