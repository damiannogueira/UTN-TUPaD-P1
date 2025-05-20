def fibonacci_recursivo(pos):
    """
    Calcula recursivamente el valor de la serie de Fibonacci en la posición pos.
    - f(0) = 0
    - f(1) = 1
    - Para pos >= 2: f(pos) = f(pos-1) + f(pos-2)
    """
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci_recursivo(pos - 1) + fibonacci_recursivo(pos - 2)

def main():
    # Leemos la posición máxima desde el usuario
    n = int(input("Ingrese hasta qué posición de Fibonacci quiere que le muestre (n ≥ 0): "))
    # Mostramos la serie completa desde 0 hasta n
    print(f"Serie de Fibonacci hasta f({n}):")
    for i in range(n + 1):
        print(f"f({i}) = {fibonacci_recursivo(i)}")

if __name__ == "__main__":
    main()
