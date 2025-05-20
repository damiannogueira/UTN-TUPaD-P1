def decimal_a_binario(n: int) -> str:
    """
    Convierte un número entero positivo n a su representación binaria.
    Utilizo Type Hints para que la función devuelva un string.
    """
    if n < 2:
        # Caso base: 0 -> "0", 1 -> "1"
        resultado = str(n)
    # Paso recursivo: dividir por 2 y concatenar el resto
    else:
        resultado = decimal_a_binario(n // 2) + str(n % 2)
    return resultado


def main():
    num = int(input("Introduce un entero positivo: "))
    if num < 0:
        print("Error: solo se admiten enteros >= 0.")
    else:
        binario = decimal_a_binario(num)
        print(f"{num} en binario es {binario}")


if __name__ == "__main__":
    main()
