# Trabajo practico unidad 9
# Ejercicio 1: Crear un archivo de productos
def crear_archivo():
    continue



# Ejercicio 2: Mostrar productos del archivo productos.txt

def mostrar_productos():
    """
    Lee el archivo de productos y los muestra en pantalla con un formato adecuado
    """
    try:
        with open("productos.txt", "r", encoding="utf-8") as productos:
            for linea in productos:
                presentacion = []
                presentacion = linea.strip().split(",")
                print(f"Producto: {presentacion[0]} | Precio: ${presentacion[1]} | Cantidad {presentacion[2]}")
    except FileNotFoundError:
        print(f"Error: No se encuentra el archivo de productos")

# Ejercicio 3: Agregar productos
def agregar_producto():
    """
    Agrega un producto al archivo productos.txt
    """
    nombre = input("Ingresa el nombre del producto: ")
    while True:
        try:
            precio = float(input("Ingresa su precio: "))
            cantidad = int(input("Ingresa la cantidad: "))
        except ValueError:
            print("Error: El precio y la cantidad deben ser numericos")
        else:
            producto_a_guardar = f"{nombre}, {precio}, {cantidad}\n"
            with open("productos.txt", "a") as productos:
                productos.write(producto_a_guardar)
            print("Producto agregado con exito!")
            break
        finally:
            input("Presiona (Enter) para continuar...")

# Menu presentado al usuario
def mostrar_menu():
    print("\n" + "=" * 42)
    print("TRABAJO PRACTICO UNIDAD 9 - MENÚ PRINCIPAL")
    print("=" * 42)
    print("1. Ejercicio 1: Crear archivo de producto")
    print("2. Ejercicio 2: Agregar nuevo producto")
    print("3. Ejercicio 3: Buscar producto")
    print("0. Salir del programa")
    print("=" * 40)

# Menu principal del trabajo
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            crear_archivo()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            agregar_producto()
        elif opcion == "0":
            print("\n¡Gracias por usar el sistema! Hasta luego.")
            break
        else:
            print("\nOpción no válida. Por favor, intente de nuevo.")

        input("\nPresione ENTER para continuar...")


if __name__ == "__main__":
    main()