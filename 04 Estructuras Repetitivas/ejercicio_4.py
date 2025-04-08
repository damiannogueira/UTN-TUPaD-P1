# EJERCICIO 4:
print("Ingrese números enteros para ser sumados, ingrese cero (0) para finalizar.")
suma = 0
num_entero = int(input("Ingrese un número entero: "))
while num_entero != 0: # Mientras ingrese enteros diferentes de cero el bucle sumará
    suma += num_entero
    num_entero = int(input("Ingresa otro número entero: "))
print(f"La suma total acumulada es: {suma}")