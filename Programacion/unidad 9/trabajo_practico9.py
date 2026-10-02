# Trabajo practico unidad 9
import os

# Ejercicio 1: Crear un archivo de productos ( lo modifique para que verifique si no existe asi valida en todo el programa)
def crear_archivo(ruta="productos.txt"):
    """
    Revisa si no existe el archivo lo crea y le carga datos iniciales
    """
    if os.path.exists(ruta):
        return
    
    print(f"El archivo {ruta} no se encuentra. Sera creado!!")
    datos_iniciales = [
        "huevos,3200.0,60\n",
        "leche,2500.0,12\n",
        "manteca,1800.0,24\n",
    ]
    with open(ruta, "w", encoding="utf-8") as productos:
        productos.writelines(datos_iniciales)
    print("¡Archivo creado con éxito!")

# Ejercicio 2: Mostrar productos del archivo productos.txt
def mostrar_productos():
    """
    Lee el archivo de productos y los muestra en pantalla con un formato adecuado
    """
    try:
        with open("productos.txt", "r", encoding="utf-8") as productos:
            for linea in productos:
                presentacion = linea.strip().split(",")
                print(f"Producto: {presentacion[0]} | Precio: ${presentacion[1]} | Cantidad: {presentacion[2]}")
    except FileNotFoundError:
        print(f"Error: No se encuentra el archivo de productos")

# Ejercicio 3: Agregar productos
def agregar_producto():
    """
    Agrega un producto al archivo productos.txt
    """
    nombre = input("Ingresa el nombre del producto: ").strip()
    # Creo una while True para validar que ingrese un numero en el precio
    while True:
        try:
            precio = float(input("Ingresa su precio: "))
        except ValueError:
            print("Error: El precio debe ser un valor numerico")
        else:
            break
    # Creo una while True para validar que ingrese un numero en la cantidad
    while True:
        try:
            cantidad = int(input("Ingresa la cantidad: "))
        except ValueError:
            print("Error: La cantidad debe ser un valor numerico")
        else:
            break
    # Al salir tengo los datos correctos asi que los uno y le doy forma para poder guardarlo en el txt
    producto_a_guardar = f"{nombre},{precio},{cantidad}\n"
    with open("productos.txt", "a", encoding="utf-8") as productos:
        productos.write(producto_a_guardar)
    print("\nProducto agregado con exito!\n")

# Ejercicio 4: Cargar datos en una lista de diccionarios
def cargar_datos_lista():
    """
    Carga todos los datos del archivo de texto a una lista con diccionarios
    """
    productos = []
    with open("productos.txt", "r", encoding="utf-8") as producto:
        for linea in producto:
            lista_limpia = linea.strip()
            nombre, precio, cantidad = lista_limpia.split(",")
            diccionario = {"nombre": nombre, "precio": float(precio), "cantidad": int(cantidad)}
            productos.append(diccionario)
    print("Datos cargados correctamente!")
    return productos

# Ejercicio 5: Buscar un producto por nombre
def buscar_producto_por_nombre():
    """
    Pide un producto al usuario y lo busca en los datos cargados
    """
    base_datos = cargar_datos_lista()

    nombre = input("Ingresa el nombre del producto a buscar: ").lower()
    encontrado = False

    for producto in base_datos:
        if nombre == producto["nombre"].lower():
            encontrado = True
            print("\n" + "=" * 50)
            print(f"Producto: {producto['nombre'].capitalize()}", end=" | ")
            print(f"Precio:   ${producto['precio']}", end=" | ")
            print(f"Cantidad: {producto['cantidad']}")
            print("=" * 50)
            break  # Detenemos la búsqueda porque ya lo encontramos

    if not encontrado:
        print(f"\nEl producto '{nombre}' no se encuentra en la lista.")

# Ejercicio 6: Guardar datos
def guardar_datos(lista_productos):
    """
    Recibe una lista de diccionarios y sobrescribe el archivo productos.txt.
    """
    with open("productos.txt", "w", encoding="utf-8") as productos:
        for producto in lista_productos:
            # Reconstruimos la línea en formato CSV
            linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            productos.write(linea)

    print("¡Base de datos actualizada correctamente en el archivo!")



# Menu presentado al usuario
def mostrar_menu():
    print("\n" + "=" * 42)
    print("TRABAJO PRACTICO UNIDAD 9 - MENÚ PRINCIPAL")
    print("=" * 42)
    print("El ejercicio 1 se ejecuta siempre al inicio. Revisa si no existe el archivo producto y lo crea")
    print("1. Ejercicio 2: Mostrar lista de productos")
    print("2. Ejercicio 3: Agregar nuevo producto")
    print("3. Ejercicio 4: Cargar datos a una lista")
    print("4. Ejercicio 5: Buscar producto por nombre")
    print("5. Ejercicio 6: Guardar datos actualizados")
    print("0. Salir del programa")
    print("=" * 40)

# Menu principal del trabajo
def main():
    crear_archivo()
    productos_memoria = []
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            mostrar_productos()            
        elif opcion == "2":
            agregar_producto()
            productos_memoria = cargar_datos_lista()
        elif opcion == "3":
            productos_memoria = cargar_datos_lista()
        elif opcion == "4":
            buscar_producto_por_nombre()
        elif opcion == "5":
            if not productos_memoria:
                productos_memoria = cargar_datos_lista()
            guardar_datos(productos_memoria)

        elif opcion == "0":
            print("\n¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Por favor, intenta de nuevo.")

        input("\nPresiona ENTER para continuar...")

# Ejecucion del
if __name__ == "__main__":
    main()