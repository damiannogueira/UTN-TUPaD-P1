# Agenda representada con un diccionario
# Claves: tuplas (día, hora) → Valores: descripción del evento
agenda = {
    ("lunes", "10:00"): "Entrega TP Integrador Programación",
    ("miércoles", "15:30"): "Parcial 2 AySO",
    ("sábado", "20:00"): "Parcial 2 Programación"
}

# Solicito al usuario día y hora para consultar
dia = input("Ingresá el día a consultar: ").strip().lower()
hora = input("Ingresá la hora (formato HH:MM): ").strip()

# Normalizo el día con .strip() y .lower() para evitar errores por formato
clave = (dia, hora)

# Consulto si la tupla (día, hora) está en la agenda
if clave in agenda:
    print(f"Evento agendado el {dia} a las {hora}: {agenda[clave]}")
else:
    print(f"No hay ningún evento agendado el {dia} a las {hora}.")
