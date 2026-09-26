print("___________________________________________________________")
print("__             EJERCICIO 6: Alumnos y sus notas          __")
print("___________________________________________________________")
print()

alumnos ={}

for i in range(3):
    aux_notas = []
    print()
    nombre = input("Ingresa un nombre: ")
    for i in range(3):
        aux_notas.append(float(input(f"Ingresa la nota {i + 1} del alumno: ")))
    notas = tuple(aux_notas)
    alumnos[nombre] = notas

print("-----------------------------------")
print(f"Listado de alumnos con sus notas")
print("-----------------------------------")
for alumno, nota in alumnos.items():
    print(f"El promedio de '{alumno}' es: {sum(nota)/len(nota):.2f}")