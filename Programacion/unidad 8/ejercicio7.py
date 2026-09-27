'''
    Ejercicio 7:
    Repetir el ejercicio 6, pero añadiendo la posibilidad de que el usuario intente ingresar un
    nuevo número luego de encontrar un error.
'''

while True:
    try:
        numero = int(input("Ingresa un numero: "))

    except ValueError:
        print("Debes ingresar un numero entero")

    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")

    else:
        print(f"El numero ingresado es: {numero}")
        break