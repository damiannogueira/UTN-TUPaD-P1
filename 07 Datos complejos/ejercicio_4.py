# Inicializo un diccionario vacío para guardar los contactos
agenda = {}

# Solicito al usuario ingresar 5 contactos con su número de teléfono
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i + 1}: ")
    numero = input(f"Ingresá el número telefónico de {nombre}: ")
    agenda[nombre] = numero  # Se guarda el par nombre-número en el diccionario

# Solicito al usuario que ingrese un nombre para consultar el número
consulta = input("Ingresá el nombre del contacto que querés buscar: ")

# Verifico si el nombre existe en la agenda y muestro el resultado
if consulta in agenda:
    print(f"El número de {consulta} es: {agenda[consulta]}")
else:
    print(f"No se encontró ningún contacto con el nombre: {consulta}")
