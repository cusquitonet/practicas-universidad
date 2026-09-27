'''
    Ejercicio 2:
    Utilizando el código del ejercicio 1, arreglar los errores para que la ejecución del programa
    sea correcta sin necesidad de usar excepciones.
'''

a = 10
b = input("Introduce un número: ")
if b.isdigit(): # Valido que el dato ingresado sea un numero y ahi permito que haga la operacion y la muestre
    b = int(b)
    result = a / b
    print(f"Resultado: {result}") # El print debe ir dentro del if para que no genere otro error
else:
    print("El dato ingresado no es un numero!")

numbers = [1, 2, 3]
if len(numbers) == 5:
    print(numbers[5])
else:
    print("La lista tiene menos elementos de lo solicitado")