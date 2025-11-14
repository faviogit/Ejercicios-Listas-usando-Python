productos = ["Arroz", "Azúcar", "Aceite", "Fideos", "Sal"]

stock = []

for i in range(len(productos)):
    cantidad = int(input(f"Ingrese la cantidad de... {productos[i]}: "))
    stock.append(cantidad)

print("Productos que tienen menos de 20 unidades en stock:")
for i in range(len(stock)):
    if stock[i] < 20:
        print(f"- {productos[i]} tiene {stock[i]} unidades")

total = sum(stock)

print(f"Cantidad total de productos que tiene la tienda es: {total}")