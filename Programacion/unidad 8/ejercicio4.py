'''
    Ejericio 4:
    Repetir el ejercicio 3, pero usando excepciones múltiples que hagan alusión a los tipos de
    errores detectados.
'''

a = 10
try:
    b = input("Introduce un número: ")
    result = a / b 
    print(f"Resultado: {result}")

# Aqui pongo las distintas excepciones que puede generar el try
except TypeError:
    print("Error de tipo: No se puede dividir un numero por un texto.")

except ValueError:
    print("Error de valor: Debes ingresar un numero, no texto.")

except ZeroDivisionError:
    print("Error matematico: No se puede dividir entre cero.")

numbers = [1, 2, 3]
try:
    print(numbers[5]) 

except IndexError: # Es el unico error que puede generar esta porcion de codigo
    print("Error de indice: El elemento esta fuera del rango de la lista.")