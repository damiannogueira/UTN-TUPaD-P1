# Diccionario original: país → capital
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Francia": "París",
    "Italia": "Roma",
    "España": "Madrid",
    "Brasil": "Brasilia"
}

# Construcción del nuevo diccionario: capital → país
capitales_paises = {}

# Recorremos el diccionario original e invertimos clave y valor
for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

# Mostramos el diccionario original y luego el invertido
print("Diccionario original (pasís → capital):")
for pais, capital in paises_capitales.items():
    print(f"{pais}: {capital}")
print("\nDiccionario invertido (capital → país):")
for capital, pais in capitales_paises.items():
    print(f"{capital}: {pais}")
