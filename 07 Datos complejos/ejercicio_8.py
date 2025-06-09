# Diccionario inicial con repuestos de autos (funcional a lo que me dedico) y sus cantidades en stock
stock_repuestos = {
    "lampara h7": 15,
    "lampara h4": 10,
    "relay 12v": 5
}

# Solicito al usuario ingresar el nombre de un repuesto para consultar o modificar
repuesto = input("Ingresá el nombre del repuesto: ").strip().lower()
# .strip() elimina espacios al principio y final
# .lower() convierte todo a minúsculas para evitar diferencias como "H7" vs "h7"

if repuesto in stock_repuestos:
    print(f"Stock actual de {repuesto}: {stock_repuestos[repuesto]} unidades")

    # Si el repuesto existe, permitimos agregar unidades
    try:
        cantidad = int(input(f"¿Cuántas unidades querés agregar al stock de {repuesto}? "))
        if cantidad > 0:
            stock_repuestos[repuesto] += cantidad
            print(f"Se agregaron {cantidad} unidades. Nuevo stock de {repuesto}: {stock_repuestos[repuesto]}")
        else:
            print("La cantidad debe ser un número positivo.")
    except ValueError:
        print("Debés ingresar un número entero válido.")

else:
    # Si el repuesto no existe, se ofrece agregarlo como nuevo producto
    try:
        nuevo_stock = int(input(f"{repuesto} no está en el stock. ¿Cuántas unidades querés registrar? "))
        if nuevo_stock >= 0:
            stock_repuestos[repuesto] = nuevo_stock
            print(f"Repuesto '{repuesto}' agregado al stock con {nuevo_stock} unidades.")
        else:
            print("El stock no puede ser negativo.")
    except ValueError:
        print("Debés ingresar un número entero válido.")

# Mostramos el stock actualizado completo
print("\n Stock actual de repuestos:")
for rep, cant in stock_repuestos.items():
    print(f"{rep}: {cant} unidades")
