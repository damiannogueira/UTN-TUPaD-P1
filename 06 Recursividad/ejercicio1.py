def factorial(n):
    """
    Calcula recursivamente el factorial de n.
    Caso base: 0! = 1 y 1! = 1
    Paso recursivo: n! = n * (n-1)!
    """
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    # Leemos el límite superior desde el usuario
    límite = int(input("Ingrese un número entero positivo: "))
    # Calculamos y mostramos factoriales desde 1 hasta el límite dado previamente
    for i in range(1, límite + 1):
        print(f"{i}! = {factorial(i)}")

if __name__ == "__main__":
    main()
