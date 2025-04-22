# Definir Funciones

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    print(f"El promedio de los tres números ingresados es: {promedio:.2f}")

# Programa Principal
print("Esta es una calculadora para obtener el promedio de tres números.")
calcular_promedio(float(input("Ingrese el primer número: ")), float(input("Ingrese el segundo número: ")), float(input("Ingrese el tercer número: "))) 