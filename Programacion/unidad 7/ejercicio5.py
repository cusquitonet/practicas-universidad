print("___________________________________________________________")
print("__               EJERCICIO 5: Manejo de frase            __")
print("___________________________________________________________")
print()

# Pido al usuario la frase a analizar
frase = input("Ingresa una frase: ")
lista = frase.split() # Creo una lista auxiliar y separo cada palabra en ella

unicas = set(lista) # Aca limpio la lista pasandola a un conjunto para conseguir elementos unicos

print()
print("-------------------------------------")
print("Las palabras unicas de la frase son: ")
for n in unicas:
    print(f"'{n}'", end=" ")

pares = {}

# Aca paso las palabras al diccionario como clave y las veces que aparece como valor
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
    if valor == 1: # Este if no es necesario pero lo puse para mejorar el formato de los print
        print(f"La palabra '{palabra}' se encuentra: {valor} vez.")
    else:
        print(f"La palabra '{palabra}' se encuentra: {valor} veces.")
    