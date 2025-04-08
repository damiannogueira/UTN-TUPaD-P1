# EJERCICIO 8
print("Ingresa 100 números enteros:")
pares = 0
impares = 0
positivos = 0
negativos = 0
ceros = 0
i = 0
for i in range (i+1,101): # 100 números desde 1 a 101
    num = int(input(f"Número {i}: "))
    if num == 0:
          ceros += 1
    elif num > 0:
        positivos += 1
    else:
        negativos += 1

    if num % 2 == 0:
            pares += 1
    else:
        impares += 1
    
print(f"Cantidad de números pares: {pares}.")
print(f"Cantidad de números impares: {impares}.")
print(f"Cantidad de números positivos: {positivos}.")
print(f"Cantidad de números negativos: {negativos}.")
print(f"Cantidad de ceros (ni par ni impar): {ceros}")        
