# Diccionario para almacenar cada alumno con su tupla de notas
notas_alumnos = {}

# Repetimos 3 veces para cargar los datos de 3 alumnos
for i in range(3):
    nombre_valido = False
    while not nombre_valido:
        nombre = input(f"Ingresá el nombre del alumno {i + 1}: ").strip()
        if nombre.isalpha():  # Validamos que el nombre contenga solo letras
            nombre_valido = True
        else:
            print("El nombre debe contener solo letras. Intentá de nuevo.")

    # Ingreso de 3 notas válidas
    notas = []
    for j in range(3):
        nota_valida = False
        while not nota_valida:
            try:
                nota = float(input(f"Ingresá la nota {j + 1} de {nombre}: "))
                if 1 <= nota <= 10: # Notas válidas sólo de 1 a 10 (no se evalúa con cero)
                    notas.append(nota)
                    nota_valida = True
                else:
                    print("La nota debe estar entre 1 y 10.")
            except ValueError:
                print("Ingresá un número válido.")

    # Guardamos las notas como una tupla asociada al nombre del alumno
    notas_alumnos[nombre] = tuple(notas)

# Calculo y muestro el promedio de cada alumno
print("\nPromedios por alumno:")
for alumno, notas in notas_alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno}: promedio = {promedio:.2f}")
