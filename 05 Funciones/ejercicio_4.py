# Importar librería math
import math

# Definir Funciones
def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    print(f"El área del círculo es: {area}.")
def calcular_perimetro_circulo(radio):
    perimetro = math.pi * 2 * radio
    print(f"El perímetro del círculo es: {perimetro}.")

# Programa Principal
radio_circulo = float(input("Ingrese el radio del círculo: ")) # La consigna no solicita validar datos
calcular_area_circulo(radio_circulo)
calcular_perimetro_circulo(radio_circulo)