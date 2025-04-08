# EJERCICIO 3:
num_1 = int(input("Ingrese el primer número entero del rango: "))
num_2 = int(input("Ingrese el último número entero del rango: "))
if num_1 > num_2:
    num_1, num_2 = num_2, num_1 #Validamos cuál de los números es el primero del rango
suma = 0
for i in range ((num_1 + 1),num_2):
        suma += i
print(f"La suma de los números comprendidos en el rango (sin incluir los extremos) es : {suma}")