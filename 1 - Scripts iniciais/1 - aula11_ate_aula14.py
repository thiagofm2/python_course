# AULA 11 E 12 - Print e Adicionando comentários.

print('Hello, World!')      # Código inicial para inauguração do curso.

# O comentário em Python pode ser feito de duas formas, em linha única, como está sendo feito agora com o '#'.
"""
E em multilinhas, utilizando 3 aspas, sejam simples ou normais,
desta forma, tudo que estiver entre estas três aspas será um
comentário. 
"""


#--------------------------------------------------------------------------------------------------------------------


# AULA 13 - Strings e Números
"""
No Python, assim como em outras linguagens de programação, existem os tipos de dados, que são as especificações dos
dados que estamos enviando ou queremos receber do Sistema.

Por exemplo, para textos, dizemos que os tipos de dados que os representam são as Strings, enquanto que para números,
existem dois tipos de dados:
    - Inteiros: que são números sem fração.
    - Floats (flutuantes): que são números fracionados.

E também possuímos os tipos booleanos, que são os tipos que correspondem somente ao valor Sim ou Não, no caso, na
computação representamos estes valores como True ou False, ou 1 e 0.
"""

# AULA 14 - Entendendo sobre Variáveis
"""
Podemos representar as variáveis como Containeres que armazenam dados, e estes dados podem ser de qualquer valor
e tipo, por exemplo.

variavelUm = 2
variavelDois = 'Olá'
"""

# Aula 15 - Modificando o tipo de dados

"""
Imagine que declaremos variáveis em nosso código, mas que no decorrer de nossa aplicação, nos vemos na necessidade
de alterar o tipo de dado, por exemplo, declaramos 3 variáveis, x,y e z.

x = 3
y = 4
z = 5

E então decidimos trocar os tipos da variável x para string, da variável z para float, e somente deixar explicito o
tipo inteiro da variável y
"""

x = str(3)
y = int(4)
z = float(5)

print(x + x)        # Ele faz a concatenação das duas strings "3", gerando o resultado 33.
print(y + y)        # Ele faz a soma correta dos dois inteiros
print(z + z)        # Ele faz a soma correta dos dois floats
