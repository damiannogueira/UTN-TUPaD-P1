#Definir Función
def saludar_usuario(nombre):
    return (f"Hola {nombre}!")

#Programa Principal
nombre_usuario = input("¿Cuál es tu nombre?: ")
saludo = saludar_usuario(nombre_usuario)
print(saludo)