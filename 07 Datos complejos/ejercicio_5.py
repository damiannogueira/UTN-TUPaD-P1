# Inicializo el diccionario vacío para almacenar los contactos
agenda = {}

# Pido al usuario ingresar 5 contactos, validando nombre y número
for i in range(5):
    valido_nombre = False
    while not valido_nombre:
        nombre = input(f"Ingresá el nombre del contacto {i + 1}: ").strip()
        # Usando el método .strip() elimino espacios en blanco al inicio y al final de la cadena (evita errores de tipeo)
        if nombre.isalpha():  # Este método verifica que el nombre tenga solo letras
            valido_nombre = True
        else:
            print("El nombre debe contener solo letras. Intentá de nuevo.")

    valido_numero = False
    while not valido_numero:
        numero = input(f"Ingresá el número telefónico de {nombre}: ").strip()
        # .strip() también se aplica para evitar espacios accidentales antes o después del número
        if numero.isdigit():  # Este método verifica que el número contenga solo dígitos
            valido_numero = True
        else:
            print("El número debe contener solo dígitos. Intentá de nuevo.")

    # Se almacena el contacto en la agenda con el nombre como clave y el número como valor
    agenda[nombre] = numero

# Solicito al usuario que ingrese un nombre para consultar el número
consulta = input("Ingresá el nombre del contacto que querés buscar: ").strip()

# Busco el nombre en la agenda y muestro el resultado si existe
if consulta in agenda:
    print(f"El número de {consulta} es: {agenda[consulta]}")
else:
    print(f"No se encontró ningún contacto con el nombre: {consulta}")
