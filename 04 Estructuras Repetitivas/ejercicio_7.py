# EJERCICIO 7
num_usuario = int(input("Ingrese un número entero positivo: "))
while num_usuario < 0: # Validamos que el número sea mayor a cero para generar el rango.
    num_usuario = int(input("Número inválido. Ingrese un número entero positivo: "))
# Si el número ingresaado es mayor a cero, realizo la suma
suma = 0
for i in range(0, num_usuario + 1):
    suma += i

print(f"La suma de los números comprendidos entre 0 y {num_usuario} es: {suma}.")