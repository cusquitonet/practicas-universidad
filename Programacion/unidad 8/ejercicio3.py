'''
    Ejercicio 3:
    Utilizando el código del ejercicio 1, mantener el código con los errores originales e incluir
    bloques try-except para que la ejecución del programa no se frene al encontrar los errores.
'''

a = 10
try: # Ingreso todo el bloque dentro del try para que no genere errores adicionales
    b = input("Introduce un número: ")
    result = a / b 
    print(f"Resultado: {result}") 

except:
    print("No se puede dividir un numero por un texto")

numbers = [1, 2, 3] # La lista no necesita ser evaluada por eso la dejo fuera
try:
    print(numbers[5]) 

except:
    print("El elemento esta fuera del rango de la lista")