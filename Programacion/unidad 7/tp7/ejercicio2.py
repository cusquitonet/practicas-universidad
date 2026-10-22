from ejercicio1 import precios_frutas # Importo el diccionario del ejercicio anterior para su uso

print("___________________________________________________________")
print("__    EJERCICIO 2: Modificacion de lista de precios      __")
print("___________________________________________________________")
print()

# Actualizo los valores del diccionario
precios_frutas.update(
    {
        'Banana' : 1330,
        'Manzana' : 1700,
        'Melón' : 2800
    }
)

print(f"Listado de precios modificado")
print("-----------------------------------")
for fruta, valor in precios_frutas.items():
    print(f"La fruta '{fruta}' custa: {valor}")
    