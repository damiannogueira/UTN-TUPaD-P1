def potencia(base: int, exponente: int) -> int:
    """
    Calcula base^exponente de forma recursiva usando:
        n^m = n * n^(m-1)
    Asume exponente >= 0.
    Utilizo Type Hints para que la función me devuelva un entero
    """
    if exponente == 0:
        resultado = 1
    else:
        resultado = base * potencia(base, exponente - 1)
    return resultado


def main():
    b = int(input("Introduce la base (entero): "))
    e = int(input("Introduce el exponente (entero no negativo): "))
    
    if e < 0:
        print("Error: el exponente debe ser un entero no negativo.") 
    else:
        resultado = potencia(b, e)
        print(f"{b}^{e} = {resultado}")


if __name__ == "__main__":
    main()
