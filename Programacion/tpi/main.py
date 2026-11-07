from logica_negocio import *
from funciones_auxiliares import validar_opcion, convertir_entero


def mostrar_menu():
    '''
    Muestra el texto del menú principal con las siete opciones.
    '''
    print('\n===== CONTROL DE INVENTARIO =====')
    print('1. Cargar herramientas')
    print('2. Mostrar inventario')
    print('3. Consultar stock')
    print('4. Reporte de agotados')
    print('5. Alta de nuevo producto')
    print('6. Actualizar stock (venta / ingreso)')
    print('7. Salir')


def main():
    '''
    Crea el inventario y mantiene el menú activo hasta que se elige la opción 7.
    Es el único lugar que captura los errores que salen de las opciones 3, 5 y 6.
    '''
    inventario = []
    opcion = 0

    while opcion != 7:
        mostrar_menu()
        try:
            texto = input('Seleccione una opción: ')
            opcion = convertir_entero(texto, 'La opción debe ser un número entero.')
            validar_opcion(opcion)

            if opcion == 1:
                cargar_herramientas(inventario)
            elif opcion == 2:
                mostrar_inventario(inventario)
            elif opcion == 3:
                consultar_stock(inventario)
            elif opcion == 4:
                reporte_agotados(inventario)
            elif opcion == 5:
                alta_producto(inventario)
            elif opcion == 6:
                actualizar_stock(inventario)
        except ValueError as e:
            print(f'Error: {e}')

    print('Programa finalizado. ¡Hasta luego!')


main()