# Definir Funciones
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    cociente = a / b if b != 0 else "No se puede dividir por cero"
    print("Operaciones Básicas:", f"{a} + {b} = {suma}", f"{a} - {b} = {resta}", f"{a} x {b} = {multiplicacion}", f"{a} / {b} = {cociente}", sep = "\n")

# Programa Principal
operaciones_basicas(float(input("Ingrese el primer número: ")), float(input("Ingrese el segundo número: ")))