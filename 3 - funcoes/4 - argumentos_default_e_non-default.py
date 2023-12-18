"""
Em algumas ocasiões, quando definimos uma função com parâmetros, caso chamarmos ela sem passar um argumento em um
desses parâmetros, obteremos um erro de sintaxe do Python.
Para driblar estes erros, podemos nos atentar aos padrões de parâmetro do Python:

Default = Quando definimos o valor direto no parâmetro;
Non-Default = Quando não definimos o valor direto no parâmetro;

por exemplo, se criarmos uma função de boas vindas, onde seja NECESSÁRIO que o usuário passe dois parâmetros, caso
ele passe somente 1, ele obterá um erro:

def boas_vindas(nome, quantidade):
    print(f'Olá, {nome}')
    print(f'Temos {quantidade} de chocolates em estoque)


boas_vindas(nome)               ---> RETORNARÁ ERRO, POIS NÃO PASSOU O ARGUMENTO REFERENTE A QUANTIDADE


O exemplo acima foi de um parâmetro Non-Default, ou seja, um valor que não foi definido direto, mas que se esperava
um valor sendo passado como argumento.
Abaixo temos um exemplo de parâmetro Default:
"""

def boas_vindas(nome, quantidade=6):
    print(f'Olá, {nome}')
    print(f'Temos {quantidade} chocolates em estoque')


boas_vindas('Thiago')

"""
É importante lembrarmos que os argumentos Non-Default DEVEM sempre estar no final dos parâmetros, após o argumento
Default
"""
