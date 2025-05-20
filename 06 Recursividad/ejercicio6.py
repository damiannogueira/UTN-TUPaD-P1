def suma_digitos(n):
    """
    Devuelve la suma de los cifras de un entero positivo n
    usando sólo operaciones matemáticas y recursión.
    """
    if n < 10:
        # Caso base: sólo un dígito
        total = n
    # Paso recursivo: suma el último dígito y recorta el número
    else:
        total = suma_digitos(n // 10) + (n % 10)
    return total

def main():
    n = int(input("Introduce un entero positivo: "))
    if n < 0:
        print("Error: sólo se admiten números >= 0.")
    else:
        total = suma_digitos(n)
        print(f"La suma de los dígitos de {n} es {total}")

if __name__ == "__main__":
    main()
