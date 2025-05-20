def contar_digito(numero, digito):
    """
    Devuelve cuántas veces aparece 'digito' (0–9) en el entero positivo 'numero',
    usando sólo %, // y recursión.
    """
    if numero < 10:
        # Caso base: un solo dígito
        total = 1 if numero == digito else 0
    else:
        # Paso recursivo: cuenta en el resto y añade 1 si el último dígito coincide
        total = contar_digito(numero // 10, digito) + (1 if numero % 10 == digito else 0)
    return total


def main():
    numero = int(input("Introduce un número entero positivo: "))
    digito = int(input("Introduce un dígito (0–9): "))
    if numero < 0 or not (0 <= digito <= 9):
        print("Error: el número debe ser ≥ 0 y el dígito entre 0 y 9.")
    else:
        contador = contar_digito(numero, digito)
        print(f"El dígito {digito} aparece {contador} veces en {numero}.")


if __name__ == "__main__":
    main()
