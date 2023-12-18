""""
Nessa aula veremos como funciona o condicionamento no Python, usando o If e o Else.

Vamos imaginar um exemplo onde nós fazemos o controle da velocidade de uma estrada, onde o motorista deve andar
dentro de um limite de velocidade, sem excedê-lo, nem andar muito abaixo deste.
"""

speed = int(input("Digite a velocidade do carro: "))        # Criamos uma variável que recebe o valor da velocidade

if speed > 110 :
    print("A velocidade está acima do limite, reduza.")     # Condição para analisar velocidade acima do limite
elif speed < 70:
    print("A velocidade está abaixo do limite, acelere.")   # Condição para analisar velocidade abaixo do limite
else:
    print("A velocidade está aceitável.")                   # Resposta caso velocidade esteja ideal
