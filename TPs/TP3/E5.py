"""
5. Desarrollar un programa que permita realizar reservas en una sala de cine de
N filas con M butacas por cada fila. Desarrollar las siguientes funciones y
utilizarlas en un mismo programa:

mostrar_butacas: Mostrará por pantalla el estado de cada una de las butacas
del cine. Esta función deberá ser invocada antes de que se realice la reserva, y
se volverá a invocar luego de la misma con los estados actualizados.

reservar: Deberá recibir una matriz y la butaca seleccionada, y actualizará la
sala en caso de estar disponible dicha butaca. La función devolverá True/False
si logró o no reservar la butaca.

cargar_sala: Recibirá una matriz como parámetro y la cargará con valores
aleatorios para simular una sala con butacas ya reservadas.

butacas_libres: Recibirá como parámetro la matriz y retornará cuántas butacas
desocupadas hay en la sala.

butacas_contiguas: Buscará la secuencia más larga de butacas libres contiguas en
una misma fila y devolverá las coordenadas de inicio de la misma.
"""

import random as rn


def mostrar_butacas(sala: list[list[int]]) -> None:
    """Muestra el estado de las butacas del cine.

    Pre: sala es una matriz que representa la sala de cine.

    Post: Imprime el estado de las butacas, donde 0 es libre y 1 es reservado.

    """
    print("Estado de las butacas (0: libre, 1: reservado):")
    for i, fila in enumerate(sala):
        print(f"Fila {i + 1}: ", " ".join(map(str, fila)))
    print()


def reservar(sala: list[list[int]], fila: int, columna: int) -> bool:
    """Reserva una butaca en la sala de cine.

    Pre: sala es una matriz que representa la sala de cine.
         fila y columna son índices válidos de la matriz.

    Post: Retorna True si la reserva fue exitosa, de lo contrario False.

    """
    if sala[fila][columna] == 0:
        sala[fila][columna] = 1
        return True
    return False


def cargar_sala(sala: list[list[int]], porcentaje_reservas: int) -> None:
    """Carga la sala con butacas aleatorias reservadas.

    Pre: sala es una matriz que representa la sala de cine.
         porcentaje_reservas es un entero que representa el porcentaje de
         butacas reservadas.

    Post: Actualiza la sala con butacas reservadas según el porcentaje indicado.

    """
    total_butacas = len(sala) * len(sala[0])
    cantidad_reservas = (total_butacas * porcentaje_reservas) // 100
    reservas = rn.sample(range(total_butacas), cantidad_reservas)
    for reserva in reservas:
        fila = reserva // len(sala[0])
        columna = reserva % len(sala[0])
        sala[fila][columna] = 1


def butacas_libres(sala: list[list[int]]) -> int:
    """Retorna la cantidad de butacas libres en la sala.

    Pre: sala es una matriz que representa la sala de cine.

    Post: Retorna un entero que representa la cantidad de butacas libres.

    """
    return sum(fila.count(0) for fila in sala)


def butacas_contiguas(sala: list[list[int]]) -> tuple[int, int]:
    """Busca la secuencia más larga de butacas libres contiguas en una misma
    fila.

    Pre: sala es una matriz que representa la sala de cine.

    Post: Retorna las coordenadas (fila, columna) de inicio de la secuencia más
          larga de butacas libres.

    """
    max_longitud = 0
    coordenadas = (-1, -1)
    for i, fila in enumerate(sala):
        longitud_actual = 0
        inicio = -1
        for j, butaca in enumerate(fila):
            if butaca == 0:
                if longitud_actual == 0:
                    inicio = j
                longitud_actual += 1
            else:
                if longitud_actual > max_longitud:
                    max_longitud = longitud_actual
                    coordenadas = (i, inicio)
                longitud_actual = 0
        if longitud_actual > max_longitud:
            max_longitud = longitud_actual
            coordenadas = (i, inicio)
    return coordenadas


def main() -> None:
    filas = int(input("Ingrese el número de filas en la sala: "))
    columnas = int(input("Ingrese el número de butacas por fila: "))
    sala = [[0 for _ in range(columnas)] for _ in range(filas)]
    porcentaje_reservas = int(
        input("Ingrese el porcentaje de butacas reservadas al inicio: ")
    )
    cargar_sala(sala, porcentaje_reservas)
    mostrar_butacas(sala)
    while True:
        fila_reserva = (
            int(input("Ingrese el número de fila para reservar (0 para salir): ")) - 1
        )
        if fila_reserva < 0:
            break
        columna_reserva = int(input("Ingrese el número de butaca para reservar: ")) - 1
        if reservar(sala, fila_reserva, columna_reserva):
            print("Reserva exitosa.")
        else:
            print("La butaca ya está reservada.")
        mostrar_butacas(sala)
    total_libres = butacas_libres(sala)
    print(f"Total de butacas libres: {total_libres}")
    fila_contigua, columna_contigua = butacas_contiguas(sala)
    if fila_contigua != -1:
        print(
            f"La secuencia más larga de butacas libres contiguas comienza en la fila {fila_contigua + 1}, columna {columna_contigua + 1}."
        )
    else:
        print("No hay butacas libres contiguas.")


if __name__ == "__main__":
    main()