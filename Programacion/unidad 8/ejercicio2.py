'''
    Ejercicio 2:
    Utilizando el código del ejercicio 1, arreglar los errores para que la ejecución del programa
    sea correcta sin necesidad de usar excepciones.
'''

a = 10
while True:
    b = input("Introduce un número: ")
    if b.isdigit():
        b = int(b)
        break
    else:
        print("Ingrese un numero!")

result = a / b
print(f"Resultado: {result}")
numbers = [1, 2, 3]
print(numbers[2])