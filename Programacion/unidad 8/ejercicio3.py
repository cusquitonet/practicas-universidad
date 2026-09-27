a = 10
try:
    b = input("Introduce un número: ")
    result = a / b 
    print(f"Resultado: {result}") 

except:
    print("No se puede dividir un numero por un texto")

try:
    numbers = [1, 2, 3]
    print(numbers[5]) 

except:
    print("El elemento esta fuera del rango de la lista")