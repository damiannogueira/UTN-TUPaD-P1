# Definir Funciones

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2) # Fórmula para clacular IMC
    print(f"Su IMC es de {imc:.2f}")

# Programa Principal

calcular_imc(float(input("Ingrese su peso en kg: ")), float(input("Ingrese su altura en metros: ")))