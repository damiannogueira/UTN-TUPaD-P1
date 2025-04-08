# Ejercicio 9
print("Ingresa 100 números enteros:")
i = 0
suma = 0
for i in range (i+1,101): # 100 números desde 1 a 101
    num = int(input(f"Número {i}: "))
    suma += num
media = suma / 100  # Entiendo que media se refiere al promedio de los 100 números
print(f"La media de los números ingresados es: {media :.2f}.") # Promedio con 2 decimales
