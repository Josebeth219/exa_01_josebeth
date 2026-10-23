import random
import time
from cls_Stack import cls_Stack
"josebeth--documentar"
# Baraja original provista por el profesor
baraja = [
    ["1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B", "9B", "10B", "JB", "QB", "KB"],
    ["1C", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC"],
    ["1D", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"],
    ["1T", "2T", "3T", "4T", "5T", "6T", "7T", "8T", "9T", "10T", "JT", "QT", "KT"]
]


class cls_Jugador:
    def __init__(self, nombre: str):
        self.nombre = nombre
        # Composición: cada jugador tiene su propia pila
        self.partida = cls_Stack()
        # Lista para almacenar los naipes obtenidos durante el juego
        self.naipes_jugados = []


def aplanar_baraja(matriz_baraja):
    """Convierte la matriz de 4x13 en una lista plana de 52 cartas."""
    return [carta for fila in matriz_baraja for carta in fila]


def repartir_naipes(jugadores, baraja_origen):
    """
    Reparte un naipe a la vez a cada jugador en forma aleatoria sin repetir,
    hasta que cada jugador alcance el tope de su pila (10 naipes).
    """
    mazo_disponible = aplanar_baraja(baraja_origen)

    # 10 rondas para llenar las pilas de 10 naipes por jugador
    for _ in range(10):
        for jugador in jugadores:
            if not jugador.partida.isfull():
                # Selección aleatoria sin repetición retirando del mazo disponible
                indice = random.randint(0, len(mazo_disponible) - 1)
                carta_seleccionada = mazo_disponible.pop(indice)
                jugador.partida.push(carta_seleccionada)


def ejecutar_juego_naipes():
    print("\n" + "=" * 50)
    print("PROBLEMA #2: BUSCANDO A LA REINA DE CORAZONES")
    print("=" * 50)

    # Instanciación de los 4 jugadores
    nombres = ["Merlina", "Pericles", "Tío Lucas", "Homero"]
    jugadores = [cls_Jugador(nom) for nom in nombres]

    # Validar que las pilas inicien vacías
    for j in jugadores:
        assert j.partida.isempty(), f"La pila de {j.nombre} debe iniciar vacía"

    # Repartir los naipes
    repartir_naipes(jugadores, baraja)

    # Encabezado de columnas
    encabezado = f"{jugadores[0].nombre:<15} {jugadores[1].nombre:<15} {jugadores[2].nombre:<15} {jugadores[3].nombre:<15}"
    print(encabezado)
    print("-" * len(encabezado))

    ganador = None
    hay_cartas = True

    # Ciclo de turnos (hasta 10 rondas de desapilado)
    for _ in range(10):
        fila_impresion = []
        for jugador in jugadores:
            if not jugador.partida.isempty():
                carta = jugador.partida.pop()
                jugador.naipes_jugados.append(carta)
                fila_impresion.append(f"{carta:<15}")

                # Verificar si es la Reina de Corazones (QC)
                if carta == "QC" and ganador is None:
                    ganador = jugador
            else:
                fila_impresion.append(f"{'':<15}")

            time.sleep(2)  # Pausa de 2 segundos por turno

        print("".join(fila_impresion))

        if ganador is not None:
            break

    print("-" * len(encabezado))

    # Validar que las pilas queden vacías al finalizar su uso
    for j in jugadores:
        while not j.partida.isempty():
            j.naipes_jugados.append(j.partida.pop())
        assert j.partida.isempty(), f"La pila de {j.nombre} debe finalizar vacía"

    # Determinar ganador y extraer lista de corazones con List Comprehension
    if ganador:
        print(f"\n¡Tenemos un ganador!: {ganador.nombre} obtuvo la Reina de Corazones (QC).")
        # List comprehension para filtrar cartas que terminan en 'C' (Corazones)
        corazones_ganador = [c for c in ganador.naipes_jugados if c.endswith("C")]
        print(f"Naipes de tipo Corazón acumulados por {ganador.nombre}: {corazones_ganador}")
    else:
        print("\nNingún jugador obtuvo la Reina de Corazones antes de agotar sus cartas.")