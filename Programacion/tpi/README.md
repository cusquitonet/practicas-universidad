<img width="2856" height="854" alt="logo-utn-siglas" src="https://github.com/user-attachments/assets/719d6351-5bdf-43ac-b23c-e28598737b89" />

# TPI Programación 1: Sistema de Control de Inventario

Trabajo Práctico Integrador de la Tecnicatura Universitaria en Programación a Distancia (UTN).

- **Estudiante:** Ahumada Cristian - Ahumada Tomas
- **Profesor:** Rigoni Cinthia
- **Tutor:** Zabala Martina
- **Repositorio:** https://github.com/cusquitonet/practicas-universidad/tree/master/Programacion/tpi
- **Video explicativo:** ['acceso al video']

## Descripción

Programa de consola en Python que permite controlar el inventario de una ferretería: cargar herramientas, consultar y actualizar su stock y detectar productos agotados. Los datos viven en memoria mientras el programa se ejecuta y no se guardan al cerrarlo.

El inventario es una lista de diccionarios llamada `inventario`, donde cada herramienta tiene las claves `'herramienta'` y `'cantidad'` (el stock). Se crea dentro de `main()` y se pasa por parámetro a cada función, sin variables globales.

## Menú

| Opción | Función | Qué hace |
|---|---|---|
| 1 | `cargar_herramientas` | Carga múltiple de herramientas con su stock inicial |
| 2 | `mostrar_inventario` | Lista todas las herramientas con su stock |
| 3 | `consultar_stock` | Busca una herramienta por nombre y muestra su stock |
| 4 | `reporte_agotados` | Lista las herramientas con stock cero |
| 5 | `alta_producto` | Agrega una herramienta nueva |
| 6 | `actualizar_stock` | Registra una venta o un ingreso de unidades |
| 7 | (en `main`) | Sale del programa |

## Estructura del proyecto

| Archivo | Contenido |
|---|---|
| `main.py` | `main()` y `mostrar_menu()`: crea el inventario, muestra el menú y captura los errores con `try/except` |
| `logica_negocio.py` | Funciones de las opciones 1 a 6 |
| `funciones_auxiliares.py` | Búsqueda y validaciones: `buscar_herramienta`, `validar_nombre`, `validar_nombre_nuevo`, `validar_opcion`, `validar_stock`, `validar_entero_positivo` y `convertir_entero` |

## Manejo de errores

- Las reglas de negocio (nombre vacío o duplicado, stock negativo, unidades menores o iguales a cero, venta mayor al stock, opción fuera de rango) se validan con `raise ValueError`.
- Las conversiones a entero se capturan con `try/except`.
- En la opción 1 el error se captura dentro de la función y se vuelve a pedir solo el dato inválido. En las opciones 3, 5 y 6 el error sube hasta el `except` de `main()`, que muestra el motivo y vuelve al menú.
- Los casos informativos (inventario vacío, herramienta inexistente, tipo de movimiento inválido) se resuelven con una condición y un mensaje.
- Un dato inválido nunca deja datos a medias ni modifica el stock.

## Cómo ejecutarlo

Requiere Python 3 [version 3.14]. Desde la carpeta del proyecto:

```
python main.py
```

Los tres archivos `.py` deben estar en la misma carpeta.

## Restricciones del trabajo

Solo se usan secuencia, `if/elif/else`, `while`/`for`, funciones y `try/except/raise`. No hay clases, variables globales ni colecciones de datos fuera de `inventario`.
