dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
temperaturas = []

for dia in dias:
    temp = float(input(f"Ingrese la temperatura del día {dia}: "))
    temperaturas.append(temp)

promedio = sum(temperaturas) / len(temperaturas)

temp_max = max(temperaturas)                 
indice_max = temperaturas.index(temp_max)    
dia_max = dias[indice_max]                   


print("--- Resultados ---")
print("Temperaturas registradas:", temperaturas)
print(f"Temperatura promedio: {promedio:.2f} °C")
print(f"La temperatura máxima fue de {temp_max} °C el día {dia_max}")
