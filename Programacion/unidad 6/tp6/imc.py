def calcular_imc(peso, altura):
    """Recibe como parametros peso y altura, y devuelve el IMC de la persona """
    return peso / (altura ** 2)

print("___________________________________________________________")
print(" __              EJERCICIO 8: Calculo IMC               __")
print("___________________________________________________________")
print()
peso = float(input("Ingresa tu peso: "))
altura = float(input("Ingresa tu altura (en mts): "))

imc = calcular_imc(peso, altura)
print("----------------------------------------")

if imc < 18.5:
    print(f"Tu IMC es {imc:.2f} y estas 'BAJO DE PESO'")
elif imc < 25:
    print(f"Tu IMC es {imc:.2f} y estas 'Normal (Saludable)'")
elif imc < 30:
    print(f"Tu IMC es {imc:.2f} y estas 'CON SOBREPESO'")
elif imc < 35:
    print(f"Tu IMC es {imc:.2f} y estas con 'OBESIDAD GRADO I'")
elif imc < 40:
    print(f"Tu IMC es {imc:.2f} y estas con 'OBESIDAD GRADO II'")
else:
    print(f"Tu IMC es {imc:.2f} y estas con 'OBESIDAD GRADO III (Extrema)'")

print()