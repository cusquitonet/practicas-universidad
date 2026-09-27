'''
    Ejercicio 6:
    Escribir un programa que pida al usuario un número, y:
    ● Si el valor ingresado es válido, lo imprima por pantalla.
    ● Si el valor ingresado no es numérico, imprima por pantalla “Debe ingresar un número
        válido”.
    ● Si contiene algún otro tipo de error, imprima por pantalla “Se produjo un error
        inesperado” junto con el error que surgió.
'''

try:
    numero = int(input("Ingresa un numero: "))

except ValueError:
    print("Debes ingresar un numero entero")

except Exception as e:
    print(f"Se produjo un error inesperado: {e}")

else:
    print(f"El numero ingresado es: {numero}")
