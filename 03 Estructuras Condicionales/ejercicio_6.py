import random
from statistics import mode, median, mean

# Defino la lista de números aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calculo la moda, mediana y media
moda = mode(numeros_aleatorios)  # Moda
mediana = median(numeros_aleatorios)  # Mediana
media = mean(numeros_aleatorios)  # Media

# Determino si hay sesgo positivo, negativo o ninguno
if media > mediana and mediana > moda: 
    sesgo = "Sesgo positivo"
elif media < mediana and mediana < moda:
    sesgo = "Sesgo negativo"
elif media == mediana and media == moda:
    sesgo = "No hay sesgo"

# Imprimo los resultados utilizando f-strings
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")
print(f"Resultado del sesgo: {sesgo}")

