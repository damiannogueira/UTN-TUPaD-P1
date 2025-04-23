"""Este ejercicio crea una lista con 5 números enteros (8, 15, 3, 22, 7).
Luego busca el valor máximo de la lista (22 en este caso) utilizando la función max, para finalmente, 
llamar al método remove y eliminar dicho valor encontrado.
Como último paso, muestra por pantalla la lista ya sin el valor que fue eliminado, en este caso el número 22.
"""
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)