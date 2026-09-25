print("___________________________________________________________")
print("__           EJERCICIO 4: Agenda telefonica              __")
print("___________________________________________________________")
print()

contactos = {}

print("Ingresa 5 contactos:")
j = 1
for i in range(5):
    nombre = input(f"Ingresa el {j} nombre: ")
    tel = input("Ingresa su numero de telefono: ")
    j += 1
    contactos.update({nombre: tel})

print("_____________________________________")
nombre = input("Ingresa un nombre a buscar: ")
if nombre in contactos:
    print(f"Su numero de telefono es: {contactos[nombre]}")
else:
    print("El nombre no esta agendado!")