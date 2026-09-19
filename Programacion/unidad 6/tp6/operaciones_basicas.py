def operaciones_basicas(num1, num2):
    """ Rebive dos parametros y realiza los 4 calculos matematicos
    principales con ellos"""

    #Genero una lista para poder devolver los valores ordenados
    lista = []
    lista.append(num1 + num2)
    lista.append(num1 - num2)
    lista.append(num1 * num2)
    lista.append(num1 / num2)
    return lista

print("___________________________________________________________")
print(" __           EJERCICIO 7: Operaciones basicas          __")
print("___________________________________________________________")
print()
numero1 = float(input("Ingresa el primero numero: "))
numero2 = float(input("Ingresa el segundo numero: "))

# Creo una lista como auxiliar para generar un mejor formato de salida
operaciones = [
    "suma",
    "resta",
    "multiplicacion",
    "division"
]

lista = operaciones_basicas(numero1, numero2)

# El for recorre las dos listas para poder generar un cuadro con los valores
# que utiliza el print para la presentacion
for indice, operacion in enumerate(operaciones):
    print("-------------------------------------------")
    print(f"La {operacion} de {numero1} y {numero2} es {lista[indice]:.2f}")

print()