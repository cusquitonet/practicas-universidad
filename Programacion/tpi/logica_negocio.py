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


if __name__ == __main__:
    pass