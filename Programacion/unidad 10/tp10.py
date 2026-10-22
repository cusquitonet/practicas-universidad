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

print()
print("============================================")
print("==== Ejercicio 1: Calculo del Factorial ====")
print("============================================")
print()

numero = int(input("Ingresa el numero a calcular: "))
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

print()
print("============================================")
print("==== Ejercicio 2: Sucesion de Fibonacci ====")
print("============================================")
print()

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

print()
print("============================================")
print("==== Ejercicio 3: Potencia de un numero ====")
print("============================================")
print()

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

print()
print("===================================================")
print("==== Ejercicio 4: Conversion decimal a binario ====")
print("===================================================")
print()

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

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

print()
print("=================================")
print("==== Ejercicio 5: Palindromo ====")
print("=================================")
print()

palabra = input("Ingrese una palabra: ")

valor = es_palindromo(palabra)
if valor == True:
    print("La palabra es un palindromo!")
else:
    print("La palabra no es un palindromo!")

'''
Ejercicio 6 · Suma de dígitos
Se pide escribir una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
Restricciones:
No se puede convertir el número a cadena de texto.
Se deben usar operaciones matemáticas (%, //) y recursión.
Ejemplos:
suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
suma_digitos(9) → 9
suma_digitos(305) → 8 (3 + 0 + 5)
'''

def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

print()
print("======================================")
print("==== Ejercicio 6: Suma de digitos ====")
print("======================================")
print()

num = int(input("Ingresa el numero: "))
print(f"La suma de los digitos de {num} es {suma_digitos(num)}!")

'''
Ejercicio 7 · Pirámide de bloques
Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último
nivel con un solo bloque.
Se pide escribir una función recursiva contar_bloques(n) que reciba el número de bloques
en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.
Ejemplos:
contar_bloques(1) → 1 (1)
contar_bloques(2) → 3 (2 + 1)
contar_bloques(4) → 10 (4 + 3 + 2 + 1)
'''

def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

print()
print("==========================================")
print("==== Ejercicio 7: Piramide de bloques ====")
print("==========================================")
print()

nu = int(input("Ingresa la cantidad de bloques de la base: "))
print(f"Necesitas {contar_bloques(nu)} bloques para contruir la piramide.")

'''
Ejercicio 8 · Apariciones de un dígito
Se pide escribir una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.
Ejemplos:
contar_digito(12233421, 2) → 3
contar_digito(5555, 5) → 4
contar_digito(123456, 7) → 0
'''

def contar_digito(numero, digito):
    if numero < 10:
        return 1 if numero == digito else 0
    ultimo_digito = numero % 10
    coincidencia = 1 if ultimo_digito == digito else 0
    return coincidencia + contar_digito(numero // 10, digito)

print()
print("===============================================")
print("==== Ejercicio 8: Apariciones de un digito ====")
print("===============================================")
print()

numer = int(input("Ingresa un numero entero: "))
digito = int(input("Ingresa el digito a buscar: "))

print(f"El digito {digito} se encuentra {contar_digito(numer, digito)} veces.")
