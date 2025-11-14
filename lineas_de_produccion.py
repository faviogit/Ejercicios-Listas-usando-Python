#produccion de  3 lineasen 4 dias
produccion = [
    [100, 120, 110, 130], #linea 1
    [90, 115, 105, 125],  #linea 2
    [95, 110, 100, 120]   #linea 3
]
print("Produccion de las lineaa x lineas:")
for fils in produccion:
    print(fila)

for i, fila in enumerate(produccion):
    total_linea = sum(fila)
    print(f"Total producido por la linea {i+1}: {total_linea} unidades")