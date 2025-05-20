def es_palindromo(palabra):
    """
    Devuelve True si 'palabra' es un palíndromo, False en caso contrario.
    No usa slicing para invertir ni reversed().
    """
    def verificar(i, j):
        if i >= j:
            # Caso base: índices cruzados o iguales → ES palíndromo
            resultado = True
        elif palabra[i] != palabra[j]:
            # Si los caracteres en los extremos no coinciden → NO es palíndromo
            resultado = False
        else:
            # Paso recursivo: seguir hacia el centro
            resultado = verificar(i + 1, j - 1)
        return resultado

    return verificar(0, len(palabra) - 1)


def main():
    p = input("Introduce una palabra (sin espacios ni tildes): ")
    if es_palindromo(p):
        print(f"'{p}' ES un palíndromo")
    else:
        print(f"'{p}' NO es un palíndromo")


if __name__ == "__main__":
    main()


