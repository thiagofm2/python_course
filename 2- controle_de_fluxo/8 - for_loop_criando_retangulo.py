"""
Somente a título de teste de conhecimento, criaremos um loop onde printaremos um quadrado ou retangulo na resposta.
"""

rows = 6
columns = 80
symbol = '@'

for horizontal in range(rows):
    for vertical in range(columns):
        print(symbol, end='')
    print()