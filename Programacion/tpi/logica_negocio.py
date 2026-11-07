from funciones_auxiliares import *

def mostrar_inventario(inventario):
    '''
    Muestra todas las herramientas con su stock actual.
    Si el inventario está vacío, lo informa con un mensaje.
    '''
    if len(inventario) == 0:
        print('Todavía no hay herramientas cargadas.')
        return

    print('--- Inventario ---')
    for producto in inventario:
        print(f"{producto['herramienta']}: {producto['cantidad']} unidades")


def reporte_agotados(inventario):
    '''
    Muestra las herramientas cuyo stock es igual a 0.
    Distingue entre inventario vacío y ninguna herramienta agotada.
    '''
    if len(inventario) == 0:
        print('Todavía no hay herramientas cargadas.')
        return

    hay_agotados = False
    print('--- Herramientas agotadas ---')
    for producto in inventario:
        if producto['cantidad'] == 0:
            print(producto['herramienta'])
            hay_agotados = True

    if not hay_agotados:
        print('Ninguna herramienta tiene stock cero.')


def consultar_stock(inventario):
    '''
    Busca una herramienta por nombre y muestra su stock.
    Si el nombre está vacío, el ValueError sube hasta main().
    '''
    if len(inventario) == 0:
        print('Todavía no hay herramientas cargadas.')
        return

    nombre = input('Nombre de la herramienta a consultar: ')
    validar_nombre(nombre)

    producto = buscar_herramienta(inventario, nombre)
    if producto is None:
        print('Esa herramienta no se encuentra en el catálogo.')
    else:
        print(f"Stock de {producto['herramienta']}: {producto['cantidad']} unidades")


def alta_producto(inventario):
    '''
    Agrega una herramienta nueva al final del inventario.
    Cualquier dato inválido lanza ValueError, que sube hasta main().
    No agrega nada hasta que nombre y stock sean válidos.
    '''
    nombre = input('Nombre del nuevo producto: ').strip()
    validar_nombre_nuevo(inventario, nombre)

    stock = convertir_entero(input('Stock inicial: '), 'El stock debe ser un número entero, sin letras ni decimales.')
    validar_stock(stock)

    inventario.append({'herramienta': nombre, 'cantidad': stock})
    print(f'Producto "{nombre}" agregado con {stock} unidades.')


def actualizar_stock(inventario):
    '''
    Registra una venta o un ingreso de unidades para una herramienta existente.
    Los pasos van en orden y el stock se modifica recién al final.
    Los ValueError suben hasta main().
    '''
    # 1. Inventario vacío
    if len(inventario) == 0:
        print('Todavía no hay herramientas cargadas.')
        return

    # 2. Nombre
    nombre = input('Nombre de la herramienta: ')
    validar_nombre(nombre)

    # 3. La herramienta debe existir
    producto = buscar_herramienta(inventario, nombre)
    if producto is None:
        print('Esa herramienta no existe en el inventario.')
        return

    # 4. Tipo de movimiento (se compara como texto, sin int())
    print('Tipo de movimiento: 1. Venta  2. Ingreso')
    tipo = input('Elija el tipo: ').strip().lower()
    if tipo != 'venta' and tipo != 'ingreso':
        print('Tipo de movimiento inválido. Debe ser venta o ingreso.')
        return

    # 5. Unidades
    unidades = convertir_entero(input('Cantidad de unidades: '), 'El stock debe ser un número entero, sin letras ni decimales.')
    validar_entero_positivo(unidades, 'Las unidades')

    # 6 y 7. Validar la venta y recién entonces modificar el stock
    if tipo == '1' or tipo == 'venta':
        if unidades > producto['cantidad']:
            raise ValueError('No hay stock suficiente para esa venta.')
        producto['cantidad'] = producto['cantidad'] - unidades
        print(f"Venta registrada. Stock de {producto['herramienta']}: {producto['cantidad']}")
    else:
        producto['cantidad'] = producto['cantidad'] + unidades
        print(f"Ingreso registrado. Stock de {producto['herramienta']}: {producto['cantidad']}")


def cargar_herramientas(inventario):
    '''
    Carga varias herramientas con su stock inicial.
    Los errores se capturan acá mismo y se vuelve a pedir solo el dato inválido.
    Una herramienta se agrega recién cuando nombre y stock son válidos.
    '''
    # 1. Cuántas herramientas se van a cargar
    cantidad_valida = False
    while not cantidad_valida:
        try:
            texto = input('¿Cuántas herramientas distintas va a cargar? ')
            cantidad = convertir_entero(texto, 'La cantidad debe ser un número entero, sin letras ni decimales.')
            validar_entero_positivo(cantidad, 'La cantidad de herramientas')
            cantidad_valida = True
        except ValueError as e:
            print(f'Error: {e}')

    # 2. Una vuelta por cada herramienta
    for i in range(cantidad):
        print(f'--- Herramienta {i + 1} de {cantidad} ---')

        # 2a. Nombre: reintenta solo el nombre
        nombre_valido = False
        while not nombre_valido:
            try:
                nombre = input('Nombre: ').strip()
                validar_nombre_nuevo(inventario, nombre)
                nombre_valido = True
            except ValueError as e:
                print(f'Error: {e}')

        # 2b. Stock: reintenta solo el stock, el nombre se conserva
        stock_valido = False
        while not stock_valido:
            try:
                texto = input('Stock inicial: ')
                stock = convertir_entero(texto, 'El stock debe ser un número entero, sin letras ni decimales.')
                validar_stock(stock)
                stock_valido = True
            except ValueError as e:
                print(f'Error: {e}')

        # 2c. Recién ahora se agrega
        inventario.append({'herramienta': nombre, 'cantidad': stock})
        print(f'Herramienta "{nombre}" cargada con {stock} unidades.')
