# Conjuntos de estudiantes que aprobaron cada parcial (nombres ficticios, pueden modificarse para probarlos)
aprobados_p1 = {"Damián", "Luis", "María", "Carlos", "Pedro"}
aprobados_p2 = {"Luis", "María", "Damián", "Sofía", "Pedro"}

# 1) Estudiantes que aprobaron ambos parciales (es una intersección)
ambos = aprobados_p1 & aprobados_p2  # También se puede usar .intersection()
print("Aprobados en ambos parciales:", ambos)

# 2) Estudiantes que aprobaron solo uno de los dos (es la diferencia simétrica)
solo_uno = aprobados_p1 ^ aprobados_p2  # También se puede usar .symmetric_difference()
print("Aprobados solo en uno de los parciales:", solo_uno)

# 3) Estudiantes que aprobaron al menos un parcial (es la unión de ambos sets)
al_menos_uno = aprobados_p1 | aprobados_p2  # También se puede usar .union()
print("Total de estudiantes que aprobaron al menos un parcial:", al_menos_uno)
