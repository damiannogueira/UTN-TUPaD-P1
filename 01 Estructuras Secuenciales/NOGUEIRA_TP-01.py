#1
print("Hola Mundo!")

#2 
nombre = input("Por favor ingresa tu nombre: ")
print(f"Hola {nombre}")

#3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido :")
edad = input("Ingrese su edad: ")
lugarResidencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugarResidencia}")

#4
pi = 3.14159
radio = float(input("Ingrese el radio de un círculo"))
area = pi * radio ** 2
perimetro = 2 * pi * radio
print(f"El área del círculo es {area:.2f}, y su perímetro es {perimetro:.2f}")

#5
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos, equivalen a {horas:.2f} horas")

#6
numero = int(input("Ingrese un número del 1 al 10")) #aquí elegí del 1 al 10 (tablas de multiplicar)
print(f"Tabla de multiplicar del {numero}") #Esto podría hacerlo con un bucle for en menos líneas
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

#7
primerNumero = int(input("Ingrese un número entero distinto de cero: ")) #Aun no aprendimos a validar estos datos (con un if, por ejemplo)
segundoNumero = int(input("Ingrese otro número entero distinto de cero: "))
suma = primerNumero + segundoNumero
cociente = float(primerNumero / segundoNumero)
producto = primerNumero * segundoNumero
resta = primerNumero - segundoNumero
print(f"El resultado de sumar ambos números es: {suma}")
print(f"El resultado de dividir el primer número por el segundo es: {cociente:.2f}")
print(f"El resultado de multiplicar ambos números es: {producto}")
print(f"El resultado de restarle segundo número al primero es: {resta}")

#8
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))
indiceCorporal = peso / (altura ** 2) #Deberíamos validar que la altura sea mayor a cero
print(f"Su índice de masa corporal es de: {indiceCorporal:.2f}")

#9
tempCelsius = float(input("Ingrese la temperatura en grados Celsius: "))
tempFahrenheit = (9/5) * tempCelsius + 32
print(f"La temperatura en grados Fahrenheit es: {tempFahrenheit:.2f}")

#10
numUno = float(input("Ingrese el primer número: "))
numDos = float(input("Ingrese el segundo número: "))
numTres = float(input("Ingrese el tercer número: "))
promedio = (numUno + numDos + numTres) / 3
print(f"El promedio de los tres números ingresados es: {promedio:.2f}")
