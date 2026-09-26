print("___________________________________________________________")
print("__           EJERCICIO 4: Agenda telefonica              __")
print("___________________________________________________________")
print()

contactos = {}

# Aca agrego los contasctos con sus numeros al diccionario
print("Ingresa 5 contactos:")
for i in range(5):
    nombre = input(f"Ingresa el {i + 1} nombre: ")
    tel = input("Ingresa su numero de telefono: ")
    contactos.update({nombre: tel})

# Aca hago la busqueda del nombre dentro del diccionario
print("_____________________________________")
nombre = input("Ingresa un nombre a buscar: ")
if nombre in contactos:
    print(f"Su numero de telefono es: {contactos[nombre]}")
else:
    print("El nombre no esta agendado!")