def consulta_producto(stock):
    prod = input("Ingresa el nombre del producto: ")
    if prod in stock:
        print(f"Stock de {prod}: {stock[prod]}")
    else:
        print("El producto no existe.")

def actualizar_stock(stock):
    prod = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    
    if prod in stock:
        stock[prod] += cantidad
        print("Stock actualizado.")
    else:
        stock[prod] = cantidad
        print("Producto nuevo registrado.")

print("___________________________________________________________")
print("__           EJERCICIO 8: productos y stock              __")
print("___________________________________________________________")
print()

stock_productos = {
    "Laptop": 15,
    "Mouse": 40,
    "Teclado": 25,
    "Monitor": 10,
    "Auriculares": 30,
    "Impresora": 8,
    "Tablet": 12,
    "Smartphone": 20,
    "Parlante Bluetooth": 35,
    "Cable HDMI": 50
}

while True:
    print("Menu de opciones.")
    print("1. Consulta de stock")
    print("2. Agregar unidades al stock")
    print("3. Agregar un nuevo producto")
    print("4. Salir")

    opcion = int(input("opcion: "))

    if opcion == 1:
        consulta_producto(stock_productos)
    elif opcion == 2:
        actualizar_stock(stock_productos)
    elif opcion == 3:
        actualizar_stock(stock_productos)
    elif opcion == 4:
        print("Saliendo!!")
        break
    else:
        print("Ingresa una opcion valida!")
