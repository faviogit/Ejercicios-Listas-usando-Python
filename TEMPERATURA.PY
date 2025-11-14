temperatura = [30, 32, 31, 29, 28, 35, 33]

promedio = sum(temperatura) / len(temperatura)

maxima = max(temperatura)

dia_max = temperatura.index(maxima) + 1
print("temepetaturas resgistradas:" , temperatura)
print("el promedio de las temperaturas es:",promedio)
print("la temperatura maxima es:",maxima ,"en el dia:", dia_max)