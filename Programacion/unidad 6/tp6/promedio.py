def calcular_promedio(numeros):
    """Recibe una lista de numeros (Pueden ser enteros o flotantes)
    y devuelve su promedio"""
    return sum(numeros) / len(numeros)

''' 
Creo una lista para guardar los parametros a pasar, asi se puede modiciar
la cantidad de numeros a pasar a la funcion sin tener que modificar todo el texto
'''
numeros = []

print("___________________________________________________________")
print(" __         EJERCICIO 10: Calculo de promedio           __")
print("___________________________________________________________")
print()
'''
Creo el for para cargar los datos y reducir lineas de codigo, si se desea pedir mas valores 
solo hay que cambiar el valor de range
'''
for i in range(3):
    numeros.append(float(input("Ingresa un numero: ")))

promedio = calcular_promedio(numeros)

print("----------------------------------------")
print(f"El promedio es: {promedio:.2f}")
print("----------------------------------------")