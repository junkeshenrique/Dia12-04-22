lado1 = float(input("Informe o tamanho em metros do lado 1 da casa:"))
lado2 = float(input("Informe o tamanho em metros do lado 2 da casa:"))
area = lado1 * lado2
print(f"A area total da casa é de {area:.0f} metros quadrados.")
watts = area * 18
print(f"Serão necessários {watts:.0f} watts para iluminar corretamente toda a casa.")
