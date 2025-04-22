# Definir Funciones

def tabla_multiplicar(numero):
    for i in range (1,11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")


# Programa Principal

tabla_multiplicar(int(input(f"Ingrese un número del 1 al 10 para ver su tabla de multiplicar: ")))
