a = 10
try:
    b = input("Introduce un número: ")
    result = a / b 

except TypeError:
    print("Error de tipo: No se puede dividir un numero por un texto.")

except ValueError:
    print("Error de valor: Debes ingresar un numero, no texto.")

except ZeroDivisionError:
    print("Error matematico: No se puede dividir entre cero.")

else:
    print(f"Resultado: {result}") 

finally:
    print("El codigo ha capturado todos los errores posibles")
try:
    numbers = [1, 2, 3]
    print(numbers[5]) 

except IndexError:
    print("Error de indice: El elemento esta fuera del rango de la lista.")

else:
    print("No ha habido errores.")

finally:
    print("El programa ha terminado!")