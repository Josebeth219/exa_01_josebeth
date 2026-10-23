"""=================================================================================================
Institute....: Universidad Técnica Nacional
Campus.......: Pacífico
Career.......: Tecnologías de Información
Course.......: ITI-321 - Programación III
Period.......: 3-2026
Documents....: Exam_01 - Solucion
Goals........: Evaluador de expresiones y juego de cartas con pilas
Professor....: Jorge Ruiz (york)
Student......:
================================================================================================="""
from cls_Stack import cls_Stack
import Subrutinas


def evaluar_expresion(cadena: str) -> bool:
    """
    Evalúa si los paréntesis (), corchetes [] y llaves {} están bien balanceados
    utilizando una instancia de cls_Stack.
    """
    pila = cls_Stack()

    # Validación de restricción: la pila debe iniciar vacía
    if not pila.isempty():
        return False

    pares = {')': '(', ']': '[', '}': '{'}
    aperturas = pares.values()
    cierres = pares.keys()

    for caracter in cadena:
        if caracter in aperturas:
            if pila.isfull():
                raise OverflowError("Límite de pila alcanzado al evaluar la expresión.")
            pila.push(caracter)
        elif caracter in cierres:
            if pila.isempty():
                return False  # Se cerró sin haber abierto previamente
            tope = pila.pop()
            if tope != pares[caracter]:
                return False  # No coincide el tipo de agrupador

    # Validación de restricción: la pila debe terminar vacía para estar balanceada
    resultado = pila.isempty()
    return resultado


def ejecutar_problema_1():
    print("=" * 50)
    print("PROBLEMA #1: EVALUACIÓN DE EXPRESIONES MATEMÁTICAS")
    print("=" * 50)

    # Captura de expresión por parte del usuario
    expresion_usuario = input("Ingrese una expresión matemática para evaluar: ")

    if evaluar_expresion(expresion_usuario):
        print(f"Resultado: La expresión '{expresion_usuario}' está BIEN escrita.\n")
    else:
        print(f"Resultado: La expresión '{expresion_usuario}' está MAL escrita.\n")

    # Pruebas automáticas con los ejemplos de la guía
    ejemplos = [
        ("a+(b*c)", True),
        ("a+(b*c", False),
        ("a+b*c)", False),
        ("a+(b*c]", False),
        ("fx=a+{4.5*[(b/c)-(c*c)]}", True)
    ]

    print("Verificación de casos de prueba de la guía:")
    for expr, esperado in ejemplos:
        valida = evaluar_expresion(expr)
        estado = "CORRECTA" if valida else "INCORRECTA"
        print(f" - {expr:<30} -> {estado}")


if __name__ == "__main__":
    # Ejecución Problema 1
    ejecutar_problema_1()

    # Ejecución Problema 2
    Subrutinas.ejecutar_juego_naipes()