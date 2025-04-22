# Definir Funciones

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32 # Fórmula para convertir Celsius a Fahrenheit
    print(f"La temperatura {celsius:.2f} en Grados Celsius, convertida a Fahrenheit es: {fahrenheit:.2f}")

# Programa Principal
celsius_a_fahrenheit(float(input("Ingrese la temperatura en Grados Celsius: ")))
