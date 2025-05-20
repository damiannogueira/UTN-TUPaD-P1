def contar_bloques(n):
    """
    Devuelve el total de bloques de una pirámide cuyo nivel más bajo tiene n bloques,
    y cada nivel superior tiene un bloque menos, hasta llegar a 1.
    """
    # Caso base: si sólo hay un nivel con 1 bloque, devuelve 1
    if n == 1:
        total = 1
    # Paso recursivo: los bloques del nivel n más los bloques de la pirámide de nivel n-1
    else:
        total = n + contar_bloques(n - 1)
    return total    


def main():
    n = int(input("Introduce el número de bloques en el nivel más bajo (entero ≥ 1): "))
    if n < 1:
        print("Error: el valor debe ser un entero mayor o igual a 1.")
    else:
        total = contar_bloques(n)
        print(f"Para un nivel base de {n} bloques, se necesitan {total} bloques en total.")


if __name__ == "__main__":
    main()
