"""
Podemos manipular strings de forma dinâmica com o For loops, por exemplo para acrescentar espaço em uma palavra,
simplesmente usando poucas linhas, para criar um título.
"""

word = input("Digite uma palavra: ")
for letter in word:
    print(f"{letter.upper()} ", end='')
