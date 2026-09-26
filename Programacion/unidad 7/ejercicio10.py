print("___________________________________________________________")
print("__           EJERCICIO 10: Paises y sus capitales        __")
print("___________________________________________________________")
print()

# Diccionario que contiene los datos necesarios
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Colombia": "Bogotá",
    "España": "Madrid",
    "México": "Ciudad de México",
    "Francia": "París",
    "Italia": "Roma",
    "Alemania": "Berlín",
    "Japón": "Tokio",
    "Canadá": "Ottawa",
    "Estados Unidos": "Washington D.C.",
    "Australia": "Camberra",
    "Reino Unido": "Londres",
    "Egipto": "El Cairo"
}

# Muestro el listado original
print("Listado original (Pais y su capital)")
print("_____________________________________")
for pa, ci in paises_capitales.items():
        print(f"'{pa}' y su capital '{ci}'.")

capitales_paises = {}

# Aca doy vuelta el diccionario intercambiando cada clave y su valor
for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

# Muestro el listado invertido
print("_____________________________________")
print("Listado invertido (Capital y su pais)")
print("_____________________________________")
for cap, pai in capitales_paises.items():
        print(f"'{cap}' es capital de '{pai}'.")
