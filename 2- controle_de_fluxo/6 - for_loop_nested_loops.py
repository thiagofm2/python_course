"""
Em alguns momentos em nossos códigos, iremos nos deparar com situações onde precisaremos utilizar Nested Loops,
ou seja, Loops dentro de loops.

No exemplo abaixo, veremos como funciona um simples loop que conta de 1 até 5, com outro loop dentro dele que faz
a mesma repetição.
"""

for outsideLoop in range(1,6):
    print(outsideLoop)
    for innerLoop in range(1, 6):
        print(outsideLoop, innerLoop)

"""
Como podemos observar, ele faz primeiro loop, e a cada número do primeiro loop, ele faz o segundo loop dentro do
primeiro.

Vamos imaginar que temos uma lista com 5 produtos, onde cada produto tem 3 atributos, e queremos exibir estes 
produtos com cada atributo que eles possuem. Nesse caso, um Inner Loop é essencial e prático para a exibição dessa 
informação. Como por exemplo:
"""

for products in range(1,6):
    print(f"Produto - {products}")
    for attribute in range(1, 4):
        print(f"Produto {products} - Atributo {attribute}")
