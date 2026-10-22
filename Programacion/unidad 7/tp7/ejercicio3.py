from ejercicio2 import precios_frutas # Importo el diccionario del ejercicio anterior

print("___________________________________________________________")
print("__   EJERCICIO 3: Recuperar frutas de lista de precios   __")
print("___________________________________________________________")
print()

# Tomo el diccionario y saco sus claves a una lista
frutas = list(precios_frutas)

print("Listado de frutas")
print("------------------------")

for fruta in frutas:
    print(f"'{fruta}'", end=", ")
print()