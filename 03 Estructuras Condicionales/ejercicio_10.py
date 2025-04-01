hemisferio = input("Ingrese el hemisferio en el que se encuentra (N/S): ").strip().upper() # Elimino espacios en blanco, considero mayúscula y minúscula.

if hemisferio == "N" or hemisferio == "S": # Sólo puede ingresar letra n/s o N/S
    mes = int(input("Ingrese el número del mes (del 1 al 12): "))
    dia = int(input("Ingrese el día del mes: "))
# Anido un if dentro de otro if
    if hemisferio == "N": # Estaciones para hemisferio norte
        if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
            estacion = "Invierno" # Del 21/12 al 20/03
        elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
            estacion = "Primavera" # Del 21/03 al 20/06
        elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
            estacion = "Verano" # Del 21/06 al 20/09
        else:
            estacion = "Otoño" # Del 21/09 al 20/12
    else: # Estaciones para hemisferio Sur
        if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
            estacion = "Verano" # Del 21/12 al 20/03
        elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
            estacion = "Otoño" # Del 21/03 al 20/06
        elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
            estacion = "Invierno" # Del 21/06 al 20/09
        else:
            estacion = "Primavera" # Del 21/09 al 20/12
    
    print(f"Usted se encuentra en la estación: {estacion}")
else:
    print("Hemisferio no válido.") # Si ingresa un caracter != n/s o N/S
