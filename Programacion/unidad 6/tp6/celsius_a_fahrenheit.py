def celsius_a_fahrenheit(celcius):
    """Recibe la temperatura en grados Celsius(°C)
    y la devuelve en grados Fahrenheit(°F)"""
    fah = (celcius * (9 / 5)) + 32
    return fah

print("_______________________________________________________________________")
print(" __ EJERCICIO 9: Convertir de grados Celsius(°C) a Fahrenheit(°F) __")
print("_______________________________________________________________________")
print()
grados = int(input("Ingresa la temperatura: "))

fahrenheit = celsius_a_fahrenheit(grados)

print("----------------------------------------")
print(f"La temperatura es {fahrenheit:.2f} grados Fahrenheit (°F)")
print()