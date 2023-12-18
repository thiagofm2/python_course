weight = input("Digite seu peso em kg: ")
height = input("Digite sua altura em centímetros: ")

if ',' in weight:
    weight = weight.replace(',','.')

if ',' in height:
    height = height.replace(',', '.')

imc_calc = float(weight) / ((float(height)/100) ** 2)

print(f'Seu IMC é de: {format(imc_calc,".2f")}')

if imc_calc < 18.5:
    print("Você está em magreza.")
elif 18.5 < imc_calc <= 24.9:
    print("Seu IMC está ideal.")
elif 25 < imc_calc <= 29.9:
    print("Você está em sobrepeso.")
elif 30 < imc_calc <= 39.9:
    print("Você está obeso.")
else:
    print("Você está obeso mórbido.")
