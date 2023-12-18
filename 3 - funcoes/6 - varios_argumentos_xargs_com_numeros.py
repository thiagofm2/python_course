"""
Vamos imaginar que precisamos criar uma função, mas não sabemos ao certo quantos argumentos terão de ser usados, ou
seja, teremos um número indefinido de argumentos.
Isso é o que é chamado de xargs, onde podemos usar vários argumentos.
"""

def soma(*numbers):
    resultado = 0
    for num in numbers:
        resultado += num
    return resultado


print(soma(3,4,5))

"""
Como podemos ver, para definir uma xarg, basta colocarmos um * antes do parâmetro da função, para dizer para o 
Python que aquilo é um parâmetro com quantidade indefinida.

Após isso, podemos passar vários números alí como argumento da função, e como queremos somá-los, nós fazemos um loop
for dentro da função, onde ela faz um giro por cada número passado como argumento e faz um cálculo de soma com ele.
"""
