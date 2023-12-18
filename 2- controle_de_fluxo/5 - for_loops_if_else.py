"""
Combinar o If e Else com o Loop For é uma ótima forma de solucionar problemas do cotidiano.

Por exemplo, imagine um E-commerce, que possui um sistema de compra que receba as requisições de compra do usuário
e as processa. Então existe a seguinte lógica: O usuário realiza a compra, e os dados devem ser enviados ao E-mail
dele caso a compra seja bem sucedida, porém, caso contrário, o sistema tentará mais duas vezes.
Se nenhuma das 3 tentativas de confirmação de compra acontecer, será retornado uma mensagem ao cliente.

"""

confirmed_bought = True
sale_data = 'Compra no valor de R$ 12.50,00 e a entrega foi confirmada.'

for verifySend in range(3):
    if confirmed_bought:
        print(sale_data)
        print("Os detalhes foram enviados em seu E-mail.")
        break
else:
    print("Falha na compra")
