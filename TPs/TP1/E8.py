"""
La siguiente función permite averiguar el día de la semana para una fecha
determinada. La fecha se suministra en forma de tres parámetros enteros y la
función devuelve 0 para domingo, 1 para lunes, 2 para martes, etc. Escribir un
programa para imprimir por pantalla el calendario de un mes completo,
correspondiente a un mes y año cualquiera basándose en la función
suministrada. Considerar que la semana comienza en domingo.
"""

dias = {
    0: "Domingo",
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
}


meses = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}


def es_bisiesto(anio: int) -> bool:
    """Comprueba si un año es bisiesto.

    Pre: Recibe el año como un número entero.

    Post: Si el entero es divisible por cuatro y no es divisible
          por 100, o es divisible por 400 es bisiesto y devuelve True, si no False.

    """
    return (anio % 4 == 0) and (anio % 100 != 0) or (anio % 400 == 0)


def pedir_fecha() -> tuple[int]:
    """Pide la fecha al usuario, la válida y la devuelve.

    Post: Devuelve una tupla(mes,año), valores enteros.

    """
    fecha = []
    while not fecha[1:]:
        try:
            mes = int(input("Ingrese el mes: "))
            if (mes <= 0) or (mes > 12):
                print("Ingrese un mes válido.")
            else:
                fecha.append(mes)
                anio = int(input("Ingrese el año: "))
                if es_bisiesto(anio):
                    meses[2] = 29
                if anio > 0:
                    fecha.append(anio)
        except ValueError:
            print("Debe ingresar un número.")
    return fecha


def dia_de_la_semana(q: int, m: int, anio: int) -> int:
    """Usando la congruencia de Zeller para el calendario Gregoriano
    calcula el día de la semana.

    Pre: Recibe el día, mes y año en números enteros.

    Post: Devuelve el día de la semana de la fecha brindada.

    """
    if m > 3:
        m -= 2
    else:
        m += 10
        anio -= 1
    j = anio // 100
    k = anio % 100
    h = (((26 * m - 2) // 10) + q + k + (k // 4) + (j // 4) - (2 * j)) % 7
    return h


def imprimir_calendario(mes: int, anio: int) -> None:
    """Imprime el calendario del mes que el usuario inserto.
    Ejecuta dia_de_la_semana las veces necesarias para imprimir el mes entero
    de la fecha brindada.

    Pre: Recibe el mes y el año en números enteros positivos.

    Post: Imprime el calendario del mes y retorna None.

    """
    for i in range(1, meses.get(mes) + 1):
        dia = dia_de_la_semana(i, mes, anio)
        if dia == 0:
            print("-" * 25)
        print(f"{i}: {dias.get(dia)}")
    return None


def main() -> None:
    mes, anio = pedir_fecha()
    imprimir_calendario(mes, anio)


if __name__ == "__main__":
    main()
