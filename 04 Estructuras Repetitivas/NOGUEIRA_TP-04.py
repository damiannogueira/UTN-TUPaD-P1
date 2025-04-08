# EJERCICIO 1:
for i in range (101):
    print(i)

# EJERCICIO 2:
num = int(input("Ingrese un número entero: "))
if num > 0:
    cantidad_digitos = len(str(num))
    print(f"El número ingresado ({num}) tiene {cantidad_digitos} dígito(s).")

# EJERCICIO 3:
num_1 = int(input("Ingrese el primer número entero del rango: "))
num_2 = int(input("Ingrese el último número entero del rango: "))
if num_1 > num_2:
    num_1, num_2 = num_2, num_1 #Validamos cuál de los números es el primero del rango
suma = 0
for i in range ((num_1 + 1),num_2):
        suma += i
print(f"La suma de los números comprendidos en el rango (sin incluir los extremos) es : {suma}")

# EJERCICIO 4:
print("Ingrese números enteros para ser sumados, ingrese cero (0) para finalizar.")
suma = 0
num_entero = int(input("Ingrese un número entero: "))
while num_entero != 0: # Mientras ingrese enteros diferentes de cero el bucle sumará
    suma += num_entero
    num_entero = int(input("Ingresa otro número entero: "))
print(f"La suma total acumulada es: {suma}")

# EJERCICIO 5
import random # Debo importar la librería Random

# Genero un número aleatorio entre 0 y 9:
import random

numero_aleatorio = random.randint(0, 9)
intentos = 0
elegido = -1  # Lo inicializo así para que empiece distinto a los del rango

print("Debes adivinar el número secreto comprendido entre 0 y 9 (sólo enteros).")

while elegido != numero_aleatorio:
    elegido = int(input("Elige un número: "))
    intentos += 1

print(f"¡Muy bien! Adivinaste el número secreto: {elegido}. Te tomó {intentos} intento(s).")

# EJERCICIO 6
print("Estos son los números pares comprendidos entre 0 y 100 en orden decreciente:")
for i in range(100, 0, -2): # Comienzo en 100, termino en 0 (cero no es par), con paso -2 (pares).

    print(i) # Muestro todos los pares, uno por línea.

# EJERCICIO 7
num_usuario = int(input("Ingrese un número entero positivo: "))
while num_usuario < 0: # Validamos que el número sea mayor a cero para generar el rango.
    num_usuario = int(input("Número inválido. Ingrese un número entero positivo: "))
# Si el número ingresaado es mayor a cero, realizo la suma
suma = 0
for i in range(0, num_usuario + 1):
    suma += i

print(f"La suma de los números comprendidos entre 0 y {num_usuario} es: {suma}.")

# EJERCICIO 8
print("Ingresa 100 números enteros:")
pares = 0
impares = 0
positivos = 0
negativos = 0
ceros = 0
i = 0
for i in range (i+1,101): # 100 números desde 1 a 101
    num = int(input(f"Número {i}: "))
    if num == 0:
          ceros += 1
    elif num > 0:
        positivos += 1
    else:
        negativos += 1

    if num % 2 == 0:
            pares += 1
    else:
        impares += 1
    
print(f"Cantidad de números pares: {pares}.")
print(f"Cantidad de números impares: {impares}.")
print(f"Cantidad de números positivos: {positivos}.")
print(f"Cantidad de números negativos: {negativos}.")
print(f"Cantidad de ceros (ni par ni impar): {ceros}")        

# Ejercicio 9
print("Ingresa 100 números enteros:")
i = 0
suma = 0
for i in range (i+1,101): # 100 números desde 1 a 101
    num = int(input(f"Número {i}: "))
    suma += num
media = suma / 100  # Entiendo que media se refiere al promedio de los 100 números
print(f"La media de los números ingresados es: {media :.2f}.") # Promedio con 2 decimales

# EJERCICIO 10
# Le pido al usuario que ingrese un número, pero lo guardo como una cadena
numero = (input("Ingresa un número y yo te invierto los dígitos: "))

if numero.startswith("-"): # Si el número es negativo
    # Uso función Slicing
    invertido = "-" + numero[:0:-1]  # Invertimos sin el signo y lo concatenamos al inicio
else:
    # Uso función Slicing
    invertido = numero[::-1] # Si es positivo sólo invertimos.

print(f"El número invertido es: {invertido}")



#NOGUEIRA DAMIÁN IGNACIO