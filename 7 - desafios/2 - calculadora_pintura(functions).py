def calc_paint_bucket(height, width, paint_yield):
    square_meter = height * width
    return square_meter / paint_yield


try:
    wall_height = int(input("Digite a altura da parede: "))
    wall_width = int(input("Digite a largura da parede: "))
    bucket_yield = int(input("Digite o rendimento da tinta: "))

    print(calc_paint_bucket(wall_height, wall_width, bucket_yield))
except ValueError:
    print("Resultado digitado não é valido. Digite apenas valores numéricos.")
finally:
    print("Programa encerrado.")
