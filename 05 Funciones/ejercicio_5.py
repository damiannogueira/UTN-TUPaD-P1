# Definir Funciones
def segundos_a_horas(segundos):
    calcular_horas = segundos / 3600
    print(f"{segundos} segundos equivalen a {calcular_horas:.2f} horas.") # Muestro las horas con 2 decimales

# Programa Principal
segundos_a_horas(int(input(f"Ingrese la cantidad de segundos: "))) # La consigna no solicita validar datos