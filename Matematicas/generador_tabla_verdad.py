"""
Generador de Tablas de Verdad
Trabajo Integrador - Matematica y Programacion

Conectivos disponibles:
    not a        -> negacion (~)
    a and b      -> conjuncion (^)
    a or b       -> disyuncion (v)
    imp(a, b)    -> implicancia (->)  [requiere parentesis: es una funcion]
    bic(a, b)    -> bicondicional (<->) [requiere parentesis: es una funcion]
Variables permitidas: p, q, r
"""

def imp(a, b):
    """Implicancia: solo es falsa cuando a es V y b es F. Equivale a (no a) o b."""
    return (not a) or b

def bic(a, b):
    """Bicondicional: verdadera cuando a y b tienen el mismo valor."""
    return bool(a) == bool(b)

def generar_combinaciones(cantidad_variables):
    """Genera las 2^n filas usando el sistema binario: cada numero i se
    convierte a binario de n digitos; 1 = Verdadero, 0 = Falso.
    La primera variable es el digito de la izquierda (cambia mas lento)."""
    combinaciones = []
    for i in range(2 ** cantidad_variables):
        # format convierte i a binario con n digitos, rellenando con ceros.
        # Ejemplo con 3 digitos: i=0 -> "000", i=5 -> "101"
        binario = format(i, "0" + str(cantidad_variables) + "b")
        fila = []
        for digito in binario:
            fila.append(digito == "1")
        combinaciones.append(fila)
    return combinaciones

def es_valida(expresion, variables):
    """Revisa que la expresion solo use palabras permitidas y que se pueda
    evaluar. Devuelve True o False."""
    permitidos = ["not", "and", "or", "imp", "bic"] + variables

    # Separamos la expresion en palabras (tokens)
    limpia = expresion
    for caracter in "(),":
        limpia = limpia.replace(caracter, " ")
    tokens = limpia.split()

    # Cada palabra debe estar en la lista de permitidos
    for token in tokens:
        if token not in permitidos:
            return False

    # imp y bic son funciones: si aparecen, debe haber parentesis
    if "imp" in tokens or "bic" in tokens:
        if "(" not in expresion:
            return False

    # Prueba de evaluacion: evaluamos una vez con todo Verdadero.
    # Si falla, la expresion tiene algun error de sintaxis.
    entorno = {"imp": imp, "bic": bic}
    for v in variables:
        entorno[v] = True
    try:
        # eval ejecuta el texto como codigo de Python. El {"__builtins__": {}}
        # vacia las funciones de Python (open, input, etc.) para que solo se
        # pueda usar nuestra logica. No es seguridad total, pero es una
        # medida de proteccion razonable para este trabajo.
        eval(expresion, {"__builtins__": {}}, entorno)
        return True
    except Exception:
        return False

def evaluar_expresion(expresion, asignacion):
    """Evalua la expresion con los valores V/F de la fila actual."""
    entorno = {"imp": imp, "bic": bic}
    entorno.update(asignacion)
    return bool(eval(expresion, {"__builtins__": {}}, entorno))

def mostrar_tabla(variables, expresion, combinaciones, resultados):
    """Imprime la tabla y clasifica la expresion."""
    encabezado = " | ".join(variables) + " | " + expresion
    print("\n" + encabezado)
    print("-" * len(encabezado))

    for i in range(len(combinaciones)):
        linea = ""
        for valor in combinaciones[i]:
            if valor:
                linea = linea + "V | "
            else:
                linea = linea + "F | "
        if resultados[i]:
            print(linea + "V")
        else:
            print(linea + "F")

    verdaderas = 0
    for r in resultados:
        if r:
            verdaderas = verdaderas + 1

    if verdaderas == len(resultados):
        print("\nLa expresion es una TAUTOLOGIA.")
    elif verdaderas == 0:
        print("\nLa expresion es una CONTRADICCION.")
    else:
        print("\nLa expresion es una CONTINGENCIA.")


# --- PROGRAMA PRINCIPAL ---
print("=== GENERADOR DE TABLAS DE VERDAD ===")

cantidad = 0
while cantidad < 1 or cantidad > 3:
    try:
        cantidad = int(input("Cantidad de variables (1 a 3): "))
        if cantidad < 1 or cantidad > 3:
            print("Debe ser un numero entre 1 y 3.")
    except ValueError:
        print("Entrada invalida: ingrese un numero entero.")

variables = []
for v in ["p", "q", "r"]:
    if len(variables) < cantidad:
        variables.append(v)

print("Variables activas:", ", ".join(variables))
print("Ejemplos: (p and q) or not r   |   imp(p, bic(q, r))")

expresion = ""
while not es_valida(expresion, variables):
    expresion = input("\nIngrese la expresion logica: ").strip()
    if not es_valida(expresion, variables):
        print("Expresion invalida. Revise variables y sintaxis.")

combinaciones = generar_combinaciones(cantidad)
resultados = []
for fila in combinaciones:
    asignacion = {}
    for i in range(len(variables)):
        asignacion[variables[i]] = fila[i]
    resultados.append(evaluar_expresion(expresion, asignacion))

mostrar_tabla(variables, expresion, combinaciones, resultados)
