receive_number = int(input("Digite um número: "))

verify_pair = lambda x: "É par" if x % 2 == 0 else 'É impar'

print(verify_pair(receive_number))
