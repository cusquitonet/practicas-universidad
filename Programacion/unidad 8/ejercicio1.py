'''
    Ejercicio 1:
    Identifica los errores del código usando comentarios (#) en las líneas afectadas. Indica el tipo
    de error y una breve explicación de por qué ocurre.
    Ejemplo: c = a / b # Error: TypeError. 'b' es un string y no permite la división[cite: 14]
'''

a = 10
b = input("Introduce un número: ")
result = a / b # Error: TypeError. b es un str y no puede dividir un int
print(f"Resultado: {result}") # Error: NameError. Si eliminamos la linea anterior aqui da un error por no estar definido result
numbers = [1, 2, 3]
print(numbers[5]) # Error. IndexError. Intenta mostrar un valor que esta fuera del rango de la lista
