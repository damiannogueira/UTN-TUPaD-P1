edad = int(input("Por favor, ingrese su edad: "))
if edad < 12 :
    print("Eres Niño/a.")
elif edad >= 12 and edad < 18 :
    print("Eres Adolescente.")
elif edad >= 18 and edad < 30 :
    print("Eres Adulto/a joven.")
else :
    print("Eres Adulto/a.")