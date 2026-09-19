def informacion_personal(nom, ape, edad, resi):
    """Imprime con formato los datos recibidos como parametro por pantalla"""
    print("-------------------------------------------------")
    print(f"Sos {nom} {ape}, tenes {edad} años y vivis en {resi}")
    print()

print("___________________________________________________________")
print(" __ EJERCICIO 3: Pide informacion personal y da formato __")
print("___________________________________________________________")
print()
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)
