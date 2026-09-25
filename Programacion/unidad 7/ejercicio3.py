from ejercicio2 import precios_frutas

print("___________________________________________________________")
print("__   EJERCICIO 3: Recuperar frutas de lista de precios   __")
print("___________________________________________________________")
print()

frutas = list(precios_frutas)

print("Listado de frutas")
print("------------------------")

for fruta in frutas:
    print(f"'{fruta}'", end=", ")
print()