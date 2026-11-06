import logica_negocio
from funciones_auxiliares import validar_opcion

def main():
    inventario = []
    opcion = 0
    while opcion != 7:
        try:
            opcion = int(input('Seleccione una opción: '))
            validar_opcion(opcion)
            if opcion == 1:
                cargar_herramientas(inventario)
            elif opcion == 2:
                mostrar_inventario(inventario)

        except ValueError as e:
            print(f'Error: {e}')



if __name__ == "__main__":
    main()

