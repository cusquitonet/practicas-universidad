print("___________________________________________________________")
print("__         EJERCICIO 7: Registro de capacitacion         __")
print("___________________________________________________________")
print()

nombres = [
    "Sofía", "Mateo", "Valentina", "Sofía", "Lucas", 
    "Santiago", "Valentina", "Camila", "Mateo", "Benjamín", 
    "María", "Lucas", "Diego", "Paula", "Nicolás"
]

print("Listado original de participantes")
print("__________________________________")
for nom in nombres:
    print(nom)

unicos = set(nombres)

print("__________________________________")
print("  Listado unico de participantes  ")
print("__________________________________")
for unico in unicos:
    print(unico)

asistentes = {}


for nombre in nombres:
    if nombre in asistentes:
        asistentes[nombre] += 1
    else:
        asistentes[nombre] = 1

# Ejemplo de cómo recorrer un diccionario para la presentación
print("__________________________________")
print("   Asistencias por participante   ")
print("__________________________________")

for nombre, cantidad in asistentes.items():
    print(f"{nombre}: {cantidad} asistencia(s)")