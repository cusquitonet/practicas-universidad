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
    numero = int(input("Ingresa un numero: ")) # Pido el numero y lo paso a entero

except ValueError: # Capturo el error si no pone un numero
    print("Debes ingresar un numero entero") 

except Exception as e: # Este except cubro otro errores que puedan aparecer
    print(f"Se produjo un error inesperado: {e}")

else: # Si todo va bien muestra el numero
    print(f"El numero ingresado es: {numero}")
