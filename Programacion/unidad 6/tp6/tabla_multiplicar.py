def tabla_multiplicar(numero):
    """Genera la tabla de multiplicacion para el numero recibido"""
    print("----------------------------------------")
    print(f"Tabla del {numero}")
    for n in range(11):
        print(f"{numero} X {n} = {numero * n}")
    print()

print("___________________________________________________________")
print(" __          EJERCICIO 6: Tabla de multiplicar          __")
print("___________________________________________________________")
print()
numero = int(input("Ingresa un numero para calcular su tabla: "))

tabla_multiplicar(numero)