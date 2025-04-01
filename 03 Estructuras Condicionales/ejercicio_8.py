nombre = input("Por favor, ingrese su nombre: ")
opcion = int(input("Elija la opción, 1 para todo en mayúsculas, "
"2 para todo en minúsculas, 3 para primera letra en mayúsculas: "))
if opcion == 1:
    print(f"{nombre.upper()}") # Caso 1 imprimo todo en mayúsculas
elif opcion == 2:
    print(f"{nombre.lower()}") # Caso 2 imprimo todo en minúsculas
elif opcion == 3:
    print(f"{nombre.title()}") # Caso 3 imprimo solo la primera letra en mayúscula, el resto en minúsculas
else:
    print("Elija una opción correcta: 1, 2, o 3.") # Si el usuario ingresa otra opción