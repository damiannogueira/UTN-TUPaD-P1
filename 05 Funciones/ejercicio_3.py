# Definir Función
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Programa Principal 
# Aquí utilicé una sintaxis más resumida, la consigna no solicita validar datos
informacion_personal(input("Nombre: "), input("Apellido: "), input("Edad: "), input("Residencia: "))

