"""
Descripción:
Este programa calcula las regiones exclusivas e intersecantes de un diagrama
de Venn de 3 conjuntos (A: ChatGPT, B: Claude, C: Gemini) dentro de un Universo (U).
Aplica validaciones estrictas de consistencia lógica antes de realizar los 
cálculos y finaliza con una demostración utilizando la librería nativa 'set'.
"""

def solicitar_entero_positivo(mensaje: str) -> int:
    """
    Función auxiliar para solicitar datos por teclado asegurando 
    que el usuario ingrese un número entero mayor o igual a 0.
    """
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Error: Debe ingresar un número entero mayor o igual a 0.")
                continue
            return valor
        except ValueError:
            print("Error: Entrada inválida. Por favor, ingrese un número entero.")

def main():
    print("=" * 65)
    print("       ANALIZADOR DE DIAGRAMA DE VENN (3 CONJUNTOS) - UTN")
    print("=" * 65)
    
    # 1. Ingreso de datos por teclado
    print("\n[1] Ingreso de datos:")
    total_universo = solicitar_entero_positivo("  -> Ingrese el total del Universo (|U|): ")
    
    print("\n  --- Cardinales de los Conjuntos Principales ---")
    conjunto_A = solicitar_entero_positivo("  -> Cantidad del conjunto A [ChatGPT] (|A|): ")
    conjunto_B = solicitar_entero_positivo("  -> Cantidad del conjunto B [Claude] (|B|): ")
    conjunto_C = solicitar_entero_positivo("  -> Cantidad del conjunto C [Gemini] (|C|): ")
    
    print("\n  --- Intersecciones Dobles ---")
    interseccion_AB = solicitar_entero_positivo("  -> Intersección |A ∩ B|: ")
    interseccion_AC = solicitar_entero_positivo("  -> Intersección |A ∩ C|: ")
    interseccion_BC = solicitar_entero_positivo("  -> Intersección |B ∩ C|: ")
    
    print("\n  --- Intersección Triple ---")
    interseccion_ABC = solicitar_entero_positivo("  -> Intersección triple |A ∩ B ∩ C|: ")

    # 2. Validaciones obligatorias de consistencia lógica
    print("\n[2] Validando consistencia lógica de los datos...")
    
    # Regla 1: Las intersecciones dobles no pueden superar a los conjuntos individuales
    if interseccion_AB > conjunto_A or interseccion_AB > conjunto_B:
        print("ERROR DE CONSISTENCIA: La intersección |A ∩ B| no puede ser mayor que |A| ni que |B|.")
        return
    if interseccion_AC > conjunto_A or interseccion_AC > conjunto_C:
        print("ERROR DE CONSISTENCIA: La intersección |A ∩ C| no puede ser mayor que |A| ni que |C|.")
        return
    if interseccion_BC > conjunto_B or interseccion_BC > conjunto_C:
        print("ERROR DE CONSISTENCIA: La intersección |B ∩ C| no puede ser mayor que |B| ni que |C|.")
        return
        
    # Regla 2: La intersección triple no puede superar a ninguna intersección doble
    if interseccion_ABC > interseccion_AB or interseccion_ABC > interseccion_AC or interseccion_ABC > interseccion_BC:
        print("ERROR DE CONSISTENCIA: La intersección triple |A ∩ B ∩ C| no puede ser mayor que las intersecciones dobles.")
        return

    # Regla 3: Cálculo preliminar de la Unión mediante Inclusión-Exclusión para verificar el Universo
    # |A ∪ B ∪ C| = |A| + |B| + |C| - |A∩B| - |A∩C| - |B∩C| + |A∩B∩C|
    total_union = conjunto_A + conjunto_B + conjunto_C - (interseccion_AB + interseccion_AC + interseccion_BC) + interseccion_ABC
    
    if total_union > total_universo:
        print(f"ERROR DE CONSISTENCIA: El total de la unión ({total_union}) supera el tamaño del Universo (|U| = {total_universo}).")
        return

    print("¡Validación exitosa! Los datos son lógicamente coherentes.\n")

    # 3. Cálculos matemáticos de regiones exclusivas
    # --- Regiones exclusivas (Solo un conjunto) ---
    # Fórmula: Se parte del total del conjunto y se restan las intersecciones dobles, 
    # sumando nuevamente el centro (triple intersección) que fue restado de más.
    solo_A = conjunto_A - interseccion_AB - interseccion_AC + interseccion_ABC
    solo_B = conjunto_B - interseccion_AB - interseccion_BC + interseccion_ABC
    solo_C = conjunto_C - interseccion_AC - interseccion_BC + interseccion_ABC

    # --- Intersecciones dobles exclusivas (excluyendo el centro triple) ---
    solo_AB = interseccion_AB - interseccion_ABC
    solo_AC = interseccion_AC - interseccion_ABC
    solo_BC = interseccion_BC - interseccion_ABC

    # --- Elementos externos (Ninguno) ---
    ninguno = total_universo - total_union

    # 4. Impresión clara y ordenada de resultados
    print("=" * 65)
    print("                 RESULTADOS DEL DIAGRAMA DE VENN")
    print("=" * 65)
    print(f"• Total del Universo (|U|)                  : {total_universo}")
    print(f"• Total de la Unión (|A ∪ B ∪ C|)           : {total_union}")
    print("-" * 65)
    print("Regiones Exclusivas (Pertenecen a un solo conjunto):")
    print(f"  - Solo A (ChatGPT exclusivo)              : {solo_A}")
    print(f"  - Solo B (Claude exclusivo)               : {solo_B}")
    print(f"  - Solo C (Gemini exclusivo)               : {solo_C}")
    print("-" * 65)
    print("Intersecciones Dobles Exclusivas (Sin el centro triple):")
    print(f"  - Solo A y B (ChatGPT y Claude, no Gemini): {solo_AB}")
    print(f"  - Solo A y C (ChatGPT y Gemini, no Claude): {solo_AC}")
    print(f"  - Solo B y C (Claude y Gemini, no ChatGPT): {solo_BC}")
    print("-" * 65)
    print(f"• Intersección Triple (|A ∩ B ∩ C|)           : {interseccion_ABC}")
    print(f"• Ninguno (Fuera de A, B y C)                : {ninguno}")
    print("=" * 65)

    # 5. Función extra de demostración con sets de Python
    demostrar_con_sets_python(
        total_universo, conjunto_A, conjunto_B, conjunto_C,
        interseccion_AB, interseccion_AC, interseccion_BC, interseccion_ABC,
        solo_A, solo_B, solo_C, solo_AB, solo_AC, solo_BC, ninguno, total_union
    )


def demostrar_con_sets_python(
    u_val, a_val, b_val, c_val, ab_val, ac_val, bc_val, abc_val,
    s_a, s_b, s_c, s_ab, s_ac, s_bc, ninguno_val, union_calculada
):
    """
    Función extra que utiliza la estructura nativa 'set' de Python para 
    crear conjuntos ficticios y demostrar que las operaciones lógicas (&, |, -) 
    arrojan los mismos resultados que las fórmulas matemáticas aplicadas.
    """
    print("\n" + "=" * 65)
    print("     DEMOSTRACIÓN TÉCNICA CON LA LIBRERÍA 'set' DE PYTHON")
    print("=" * 65)
    print("Generando particiones disjuntas para poblar los conjuntos lógicos...")

    # Construimos identificadores únicos (IDs) para cada región exclusiva del diagrama
    id_id = 1

    particion_solo_A = set(range(id_id, id_id + s_a))
    id_id += s_a

    particion_solo_B = set(range(id_id, id_id + s_b))
    id_id += s_b

    particion_solo_C = set(range(id_id, id_id + s_c))
    id_id += s_c

    particion_solo_AB = set(range(id_id, id_id + s_ab))
    id_id += s_ab

    particion_solo_AC = set(range(id_id, id_id + s_ac))
    id_id += s_ac

    particion_solo_BC = set(range(id_id, id_id + s_bc))
    id_id += s_bc

    particion_centro = set(range(id_id, id_id + abc_val))
    id_id += abc_val

    particion_ninguno = set(range(id_id, id_id + ninguno_val))

    # Construcción final de los conjuntos principales mediante uniones de regiones
    conjunto_A = particion_solo_A | particion_solo_AB | particion_solo_AC | particion_centro
    conjunto_B = particion_solo_B | particion_solo_AB | particion_solo_BC | particion_centro
    conjunto_C = particion_solo_C | particion_solo_AC | particion_solo_BC | particion_centro

    # Verificación de operaciones lógicas vs fórmulas matemáticas
    print("\nVerificando igualdades lógicas:")
    
    # 1. Tamaño del conjunto A
    test_A = len(conjunto_A) == a_val
    print(f"  * len(A) == |A|: {len(conjunto_A)} == {a_val} -> {test_A}")

    # 2. Intersección A ∩ B
    interseccion_py_AB = conjunto_A & conjunto_B
    test_AB = len(interseccion_py_AB) == ab_val
    print(f"  * len(A & B) == |A ∩ B|: {len(interseccion_py_AB)} == {ab_val} -> {test_AB}")

    # 3. Intersección Triple A ∩ B ∩ C
    interseccion_py_abc = conjunto_A & conjunto_B & conjunto_C
    test_abc = len(interseccion_py_abc) == abc_val
    print(f"  * len(A & B & C) == |A ∩ B ∩ C|: {len(interseccion_py_abc)} == {abc_val} -> {test_abc}")

    # 4. Unión Total A ∪ B ∪ C
    union_py = conjunto_A | conjunto_B | conjunto_C
    test_union = len(union_py) == union_calculada
    print(f"  * len(A | B | C) == Unión Calculada: {len(union_py)} == {union_calculada} -> {test_union}")

    print("\nConclusión de la cátedra: Las operaciones con objetos 'set' de Python")
    print("  validan formalmente la consistencia teórica del Principio de Inclusión-Exclusión.")
    print("=" * 65)


if __name__ == "__main__":
    main()