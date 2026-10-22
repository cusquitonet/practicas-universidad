print("___________________________________________________________")
print("__             EJERCICIO 6: Alumnos y sus notas          __")
print("___________________________________________________________")
print()

# Creo el diccionario vacio
alumnos ={}

for i in range(3):
    aux_notas = [] # Tabla auxiliar para poder pedir las notas. La defino dentro del for asi cada vez que vuelve a iniciar la iteraccion se limpia
    print()
    nombre = input("Ingresa un nombre: ")
    for i in range(3):
        aux_notas.append(float(input(f"Ingresa la nota {i + 1} del alumno: ")))
    notas = tuple(aux_notas) # creo una tupla con los valores de la lista auxiliar
    alumnos[nombre] = notas # Aca recien asigno clave y valor al diccionario

print("-----------------------------------")
print(f"Listado de alumnos con sus notas")
print("-----------------------------------")
for alumno, nota in alumnos.items():
    print(f"El promedio de '{alumno}' es: {sum(nota)/len(nota):.2f}")