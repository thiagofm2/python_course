"""
Veremos sobre o While Loop, uma outra forma de se fazer um loop em Python, ideal para quando precisarmos fazer um
loop baseado em uma condição.

Vamos imaginar que precisamos de um algoritmo para uma loja que iniciará uma promoção.
A promoção inicia-se com R$90,00, e a cada dia que passa vai-se acumulando mais R$5,00, ou seja, vai ficando mais
barato.
Precisamos colocar no código o balanço entre o valor pago no produto e o lucro que o vendedor terá, pois ele não
pode sair no prejuízo de vender um produto por preço mais barato do que pagou.
"""

pricePaidForProduct = 20
productPrice = 100
day = 1

while productPrice > pricePaidForProduct:
    day += 1
    productPrice -= 5
    print(f'No dia {day}, o preço do produto será de: R$ {productPrice}')
