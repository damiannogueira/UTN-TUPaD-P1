frase = input("Por favor, ingrese una frase o una palabra: ")
# Compruebo si el último caracter es vocal (lower lo utilizo para verificar tanto mayúsculas como minúsculas)
if frase[-1].lower() in 'aeiouáéíóú':
    frase += "!" # Le agrego ! si termina en vocal y lo imprimo
    print(frase)
else:            # Caso contrario lo imprimo como el usuario lo ingresó
    print (frase)
    