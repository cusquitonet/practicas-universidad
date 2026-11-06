'''
Funciones auxiliares para el TPI
Colocamos estas funciones por separado ya que el mismo codigo se repetia en varias partes del programa, asi generamos menos codigo y
se mantiene lo mas limpio posible el codigo.
'''

def buscar_herramienta(inventario, nombre):
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
    if buscar_herramienta(inventario, nombre) is not None:
        raise ValueError("La herramienta ya existe!")


def validar_opcion(opcion):
    '''
    Valida que la opcion del menu este dentro del rango requerido.
    '''
    if opcion < 1 or opcion > 7:
        raise ValueError('Opción fuera de rango (1 a 7).')


def validar_stock(stock):
    '''
    Valida que no ingrese un numero negativo.
    '''
    if stock < 0:
        raise ValueError('El stock no puede ser negativo.')


def validar_entero_positivo(valor, descripcion):
    '''
    Valida que un número entero sea mayor que 0.
    El parámetro descripcion se usa para armar un mensaje claro.
    '''
    if valor <= 0:
        raise ValueError(f'{descripcion} debe ser mayor que 0.') # Aca la IA me dio una forma de incrustar los textos para print e input.
