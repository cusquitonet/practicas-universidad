print("___________________________________________________________")
print("__         EJERCICIO 7: Registro de capacitacion         __")
print("___________________________________________________________")
print()

# Tabla original sobre la que trabajamos
nombres = [
    "Sofía", "Mateo", "Valentina", "Sofía", "Lucas", 
    "Santiago", "Valentina", "Camila", "Mateo", "Benjamín", 
    "María", "Lucas", "Diego", "Paula", "Nicolás"
]

print("Listado original de participantes")
print("__________________________________")
for nom in nombres:
    print(nom)

# Creo un conjunto para eliminar los duplicados
unicos = set(nombres)

print("__________________________________")
print("  Listado unico de participantes  ")
print("__________________________________")
for unico in unicos:
    print(unico)

asistentes = {}

# aca armo el diccionario asistentes con el nombre como clave y la cantidad de veces que aparece como valor
for nombre in nombres:
    if nombre in asistentes:
        asistentes[nombre] += 1
    else:
        asistentes[nombre] = 1 # Si el asistente todabia no esta en la base lo agrego y le asigno 1 al valor

print("__________________________________")
print("   Asistencias por participante   ")
print("__________________________________")
for nombre, cantidad in asistentes.items():
    print(f"{nombre}: {cantidad} asistencia(s)")