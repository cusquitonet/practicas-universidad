print("___________________________________________________________")
print("__               EJERCICIO 5: Manejo de frase            __")
print("___________________________________________________________")
print()

frase = input("Ingresa una frase: ")
lista = frase.split()

unicas = set(lista)

print()
print("-------------------------------------")
print("Las palabras unicas de la frase son: ")
for n in unicas:
    print(f"'{n}'", end=" ")

pares = {}

for palabra in lista:
    if palabra in pares:
        pares[palabra] += 1
    else:
        pares[palabra] = 1

print()
print("-------------------------------------")
print(f"Lista de palabras y cuantas veces aparecen en la frase")
print("-----------------------------------")
for palabra, valor in pares.items():
    if valor == 1:
        print(f"La palabra '{palabra}' se encuentra: {valor} vez.")
    else:
        print(f"La palabra '{palabra}' se encuentra: {valor} veces.")
    