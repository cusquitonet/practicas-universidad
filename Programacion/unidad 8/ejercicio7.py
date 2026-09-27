'''
    Ejercicio 7:
    Repetir el ejercicio 6, pero añadiendo la posibilidad de que el usuario intente ingresar un
    nuevo número luego de encontrar un error.
'''

while True: # Agregando esta linea podremos pedir el numero hasta que el usuario ponga un numero
    try:
        numero = int(input("Ingresa un numero: "))

    except ValueError:
        print("Debes ingresar un numero entero")

    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")

    else: # Cuando el numnero es correcto lo muestra
        print(f"El numero ingresado es: {numero}")
        break # Esta linea corta el while y sale. esta en el else ya que es donde apunta el try si no tiene errores.