'''
Ejercicio 1 · Factorial
Se pide crear una función recursiva que calcule el factorial de un número entero no
negativo y utilizarla para calcular y mostrar en pantalla el factorial de todos los números
enteros entre 1 y el número que indique el usuario.
'''

def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num -1)

numero = int(input("Ingresa un numero  para calcular los factoriales: "))
for n in range(1, numero+1):
    print(f"El Factorial de {n} es: {factorial(n):,}")

'''
Ejercicio 2 · Sucesión de Fibonacci
Se pide crear una función recursiva que calcule el valor de la sucesión de Fibonacci en la
posición indicada. Posteriormente, se pide mostrar la sucesión completa hasta la posición
que especifique el usuario.
'''

def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)

posicion = int(input("Ingresa la posicion hasta la que queres ver la sucesion: "))
for p in range(posicion + 1):
    print(f"La sucesion hasta la posicion {p} es: {fibonacci(p):,}")

'''
Ejercicio 3 · Potencia
Se pide crear una función recursiva que calcule la potencia de un número base elevado a
un exponente entero no negativo, utilizando la fórmula nm = n ∗ n(m−1), con n0 = 1 como
caso base. Se pide probar la función en un algoritmo general.
'''

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

base = (int(input("Ingresa la base: ")))
exponente = (int(input("Ingresa el exponente: ")))

print(f"La potencia de {base} elevado a {exponente} es {potencia(base, exponente)}")

'''
Ejercicio 4 · Conversión de decimal a binario
Se pide crear una función recursiva en Python que reciba un número entero positivo en
base decimal y devuelva su representación en binario como una cadena de texto.
La representación binaria de un número utiliza solamente ceros (0) y unos (1), en base 2.
Para convertir un número decimal a binario, se puede seguir este procedimiento:
1. Dividir el número por 2.
2. Guardar el resto (0 o 1).
3. Repetir el proceso con el cociente hasta que llegue a 0.
4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.
Ejemplo:
Convertir el número 10 a binario:
10 ÷ 2 = 5, resto: 0
5 ÷ 2 = 2, resto: 1
2 ÷ 2 = 1, resto: 0
1 ÷ 2 = 0, resto: 1
Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010".
'''

def decimal_a_binario(n):
    if n == 0:
        return " "
    return decimal_a_binario(n // 2) + str(n % 2)

nume = (int(input("Ingresa el numero a convertir: ")))

print(f"El resultado en binario de {nume} es {decimal_a_binario(nume)}")

'''
Ejercicio 5 · Palíndromo
Se pide implementar una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes y devuelva True si es un palíndromo o False si no lo
es.
Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed().
'''

def palindromo(texto):
    pass
