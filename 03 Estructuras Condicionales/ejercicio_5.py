contraseña = input("Genere una contraseña, con un mínimo de 8 caracteres y un máximo de 14: ")
if 8 <= len(contraseña) <= 14 :
    print("Has ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")
