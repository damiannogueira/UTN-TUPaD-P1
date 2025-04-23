# Lista compras
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a- Agregar jugo a la tercer lista
compras[2].append("jugo")
# b- Reemplazar fideos por tallarines en la segunda lista
compras[1][1] = "tallarines"
# c- Eliminar pan de la primer lista
compras[0].remove("pan")
# d- Imprimir la lista final
print(compras)