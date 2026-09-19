def segundos_a_horas(segundo):
    """Calcula las horas en base a los segundos recibidos"""
    horas = segundo // 3600
    resto = segundo % 3600
    minutos = resto // 60

    return horas, minutos

print("___________________________________________________________")
print(" __         EJERCICIO 5: Pasar segundos a horas         __")
print("___________________________________________________________")
print()

segundos = int(input("Ingrese los segundos: "))
tiempo = segundos_a_horas(segundos)

print("------------------------------------")
print(f"El valor es: {tiempo[0]} horas y {tiempo[1]} minutos")
print()
