'''
Funciones auxiliares para el TPI
Colocamos estas fuciones por separado ya que el mismo codigo se repetia en varias partes del programa, asi generamos menos codigo y
se mantiene lo mas limpio posible el codigo.
'''

def buscar_herramientas(inventario, nombre):
    '''
    Busca una herramienta por su nombre en la lista de herramientas.
    Devuelve la herramienta si se encuentra, de lo contrario devuelve None.
    '''
    for producto in inventario:
        if producto['herramienta'].strip().lower() == nombre.strip().lower():
            return producto
    return None

def validar_nombre(nombre):
    '''
    Valida que el nombre de una herramienta no esté vacío.
    '''
    if nombre.strip() == "":
        raise ValueError("El nombre de la herramienta no puede estar vacío.")

def validar_nombre_nuevo(inventario, nombre):
    '''
    Valida que el nombre de la herramienta no esté vacío y no exista en el inventario.
    '''
    validar_nombre(nombre)
    if buscar_herramientas(inventario, nombre) is not None:
        raise ValueError("La herramienta ya existe!")

# Agregamos un if __name__ para hacer pruebas sobre las funciones. (Estas las hicimos nosotros pero le pedimos a la IA que las revise y nos ofrecio un par de mejoras que agregamos).
if __name__ == "__main__":
    inventario = [
        {'herramienta': 'Martillo', 'cantidad': 10},
        {'herramienta': 'Destornillador', 'cantidad': 5}
    ]

    print("--- INICIANDO PRUEBAS ---")

    # 1. Prueba de buscar_herramientas (encontrada con mayúsculas/espacios)
    resultado = buscar_herramientas(inventario, '  martillo  ')
    if resultado is not None and resultado['herramienta'] == 'Martillo':
        print("[OK] buscar_herramientas: Encontró la herramienta correctamente.")
    else:
        print("[ERROR] buscar_herramientas: Falló la búsqueda.")

    # 2. Prueba de buscar_herramientas (no encontrada)
    resultado = buscar_herramientas(inventario, 'llave inglesa')
    if resultado is None:
        print("[OK] buscar_herramientas: Manejó bien una herramienta inexistente.")
    else:
        print("[ERROR] buscar_herramientas: Encontró algo que no debería estar.")

    # 3. Prueba de validar_nombre (nombre vacío)
    try:
        validar_nombre("   ")
        print("[ERROR] validar_nombre: No detectó el espacio vacío.")
    except ValueError:
        print("[OK] validar_nombre: Detectó correctamente el nombre vacío.")

    # 4. Prueba de validar_nombre_nuevo (herramienta duplicada)
    try:
        validar_nombre_nuevo(inventario, 'Martillo')
        print("[ERROR] validar_nombre_nuevo: Permitió registrar un duplicado.")
    except ValueError:
        print("[OK] validar_nombre_nuevo: Detectó que la herramienta ya existe.")

    print("--- FIN DE LAS PRUEBAS ---")