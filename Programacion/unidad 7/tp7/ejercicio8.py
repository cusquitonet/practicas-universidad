def consulta_producto(stock):
    """ Permite consultar si el producto existe y tiene stock """
    prod = input("Ingresa el nombre del producto: ").capitalize()
    if prod in stock:
        print(f"Stock de {prod}: {stock[prod]}")
    else:
        print("El producto no existe.")

def actualizar_stock(stock):
    """Se utiliza para actualizar el stock y si no existe el producto permite cargarlo"""
    prod = input("Ingresa el nombre del producto: ").capitalize()
    cantidad = int(input("Ingresa la cantidad: "))
    
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

# Base de productos en un diccionario
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

# Parte principal del programa
while True:
    print("Menu de opciones.")
    print("1. Consulta de stock")
    print("2. Agregar unidades al stock")
    print("3. Agregar un nuevo producto")
    print("4. Salir")

    opcion = int(input("opcion: ")) # Aca pido al usuario que ingrese la opcion y la paso a numero para ser evaluada

    if opcion == 1:
        consulta_producto(stock_productos)
    elif opcion == 2: 
        actualizar_stock(stock_productos)
    elif opcion == 3: # Las opciones 2 y 3 van a la misma funcion ya que esta si no existe el producto permite crearlo
        actualizar_stock(stock_productos)
    elif opcion == 4:
        print("Saliendo!!")
        break
    else:
        print("Ingresa una opcion valida!")
