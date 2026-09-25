print("___________________________________________________________")
print("__    EJERCICIO 1: Actualizacion de lista de precios     __")
print("___________________________________________________________")
print()

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

print(f"Listado de precios sin actualizar ")
print("-----------------------------------")
for fruta, valor in precios_frutas.items():
    print(f"La fruta '{fruta}' custa: {valor}")
print()
    
precios_frutas.update(
    {
        'Naranja' : 1200,
        'Manzana' : 1500,
        'Pera' : 2300
    }
)

print(f"Listado de precios actualizado")
print("-----------------------------------")
for fruta, valor in precios_frutas.items():
    print(f"La fruta '{fruta}' custa: {valor}")
    