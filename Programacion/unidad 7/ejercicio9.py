print("___________________________________________________________")
print("__           EJERCICIO 9: Agenda de actividades          __")
print("___________________________________________________________")
print()

# Creo el diccionario de valores necesarios
agenda = {
    ("Lunes", "10:00"): "Reunión de equipo",
    ("Martes", "15:00"): "Consulta médica",
    ("Viernes", "18:00"): "Gimnasio"
}

# Pido al usuario que ingrese el dia y la hora
dia = input("Ingresa el día: ").capitalize()
hora = input("Ingresa la hora (HH:MM): ")

consulta = (dia, hora) # Creo la consulta con una tupla

# Realizo la consulta contra el diccionario
if consulta in agenda:
    print(f"La actividad es: {agenda[consulta]}")
else:
    print("No hay actividades programadas para esa hora")