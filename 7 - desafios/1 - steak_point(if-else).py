try:
    meat_temperature = int(input("Qual a temperatura da carne? "))
except ValueError:
    print("O valor digitado não é válido.")
else:
    if meat_temperature < 48:
        print("É recomendado que a carne fique por mais tempo assando.")
    elif 48 <= meat_temperature < 54:
        print("A carne está mal passada.")
    elif 54 <= meat_temperature < 60:
        print("A carne está ao ponto para mal passada.")
    elif 60 <= meat_temperature < 65:
        print("A carne está ao ponto")
    elif 65 <= meat_temperature < 70:
        print("A carne está ao ponto para bem passada")
    elif meat_temperature == 70:
        print("A carne está bem passada")
    else:
        print("A carne queimou.")
finally:
    print("Programa encerrado.")
