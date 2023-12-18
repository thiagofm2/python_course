"""
Vamos imaginar que temos um Marketplace, onde vendemos produtos de Fornecedores terceiros, e a cada venda de um produto
de um fornecedor terceiro, recebemos 10% do valor da venda.
Porém, esta regra deve ser aplicada somente se o valor do produto for maior que R$ 20,00.

"""

price = float(input("Digite o valor de seu produto: "))

while price > 20:
    price = (price * 0.10) + price
    print(f"O valor final do seu produto será de R${price}")
    break
