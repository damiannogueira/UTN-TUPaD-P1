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