#Importo la funcion PI del modulo math para usar siempre el mismo valor
from math import pi

def calcular_area_circulo(radio):
    return pi * (radio ** 2)
    """ Calcula el area con el parametro radio y lo devuelve """

def calcular_perimetro_circulo(radio):
    return 2 * pi * radio
    """ Calcula el perimetro con el parametro radio y lo devuelve """

print("___________________________________________________________")
print(" __ EJERCICIO 4: Calculo Area y Perimetro de un circulo __")
print("___________________________________________________________")
print()
radio = float(input("Ingresa el radio del circulo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print("--------------------------------------------------------")
print(f"El area del circulo es {area:.2f} y su perimetro es {perimetro:.2f}")
print()