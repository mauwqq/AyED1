"""
Escribir una función diasiguiente(dia, mes año) que reciba como parámetro una
fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres
enteros correspondientes el día siguiente al dado. Utilizando esta función sin
modificaciones ni agregados, desarrollar programas que permitan:
a. Sumar N días a una fecha.
"""

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


def pedir_fecha() -> list[int]:
    """Solicita la fecha al usuario verificado cada valor ingresado. Primero
    solicita el año, si es bisiesto actualiza la cantidad de dias de febrero en
    meses. Despues solicita el mes que comprueba con comprobar_mes y por ultimo
    solicita el dia.

    Post: Devuelve una lista de tres enteros con la fecha en formato YY/MM/DD.

    """
    fecha = []
    texto = ["Año", "Mes", "Dia"]
    print("Ingrese la fecha")
    for i in range(3):
        while not fecha[2:]:
            try:
                num = int(input(f"{texto[i]}: "))
                if num > 0:
                    match i:
                        case 0:  # año
                            fecha.append(num)
                            if es_bisiesto(num):
                                meses.update({2: 29})
                        case 1:  # mes
                            if comprobar_mes(num):
                                fecha.append(num)
                            else:
                                print("Mes inválido, reintentar.")
                                continue
                        case 2:  # dia
                            if comprobar_dia(num, fecha[1]):
                                fecha.append(num)
                            else:
                                print("Día inválido, reintentar.")
                                continue
                    break
                print("El número ingresado debe ser positivo.")
            except ValueError:
                print("Debe ingresar un número, reintentar.")
    return fecha


def es_bisiesto(anio: int) -> bool:
    """Comprueba si un año es bisiesto.

    Pre: Recibe el año como un número entero.

    Post: Si el entero es divisible por cuatro y no es divisible
          por 100, o es divisible por 400 es bisiesto y devuelve True, si no False.

    """
    return (anio % 4 == 0) and (anio % 100 != 0) or (anio % 400 == 0)


def comprobar_mes(mes: int) -> bool:
    """Comprueba si el mes dado como parámetro es válido.

    Pre: Recibe el mes como un número entero positivo.

    Post: Si el número está en las claves del diccionario, meses devuelve True.
          Si el número no está en las claves del diccionario, meses devuelve
          False.

    """
    return mes in meses


def comprobar_dia(dia: int, mes: int) -> bool:
    """Comprueba que el día ingresado por el usuario sea válido verificando que
    sea menor o igual al valor del mes en meses.

    Pre: día es un número entero positivo.
         mes es un número entero positivo.

    Post: Devuelve True si día es menor o igual a la cantidad de días del mes.
          Devuelve False si día es mayor a la cantidad de días del mes.

    """
    return dia <= meses.get(mes)


def pedir_cuanto_adelantar() -> int:
    """Solicita al usuario un número entero positivo y lo devuelve.

    Post: Devuelve un número entero positivo.

    """
    while True:
        try:
            num = int(input("Cuantos días quiere sumar a la fecha: "))
            if num > 0:
                break
            print("El número ingresado debe ser positivo.")
        except ValueError:
            print("Debe ingresar un número, reintentar.")
    return num


def diasiguiente(dia: int, mes: int, anio: int) -> tuple[int]:
    """Suma un dia a la fecha ingresada.

    Pre: dia, mes y anio son números enteros positivo.

    Post: Devuelve una tupla de tres enteros(dia, mes, año) con la fecha
          modificada.

    """
    if (dia + 1) < meses.get(mes):
        dia += 1
    else:
        if mes != 12:
            mes += 1
            dia = 1
        else:
            anio += 1
            mes = 1
            dia = 1
    return dia, mes, anio


def calcular_fecha(adelanto: int, dia: int, mes: int, anio: int) -> tuple[int]:
    """Bucle que ejecuta diasiguiente las veces que sea necesario para llegar
    a la fecha deseada.

    Pre: adelanto, dia, mes, anio son numeros enteros positivos.

    Post: Devuelve la fecha en una tupla(dia,mes,año).

    """
    i = 0
    while i < adelanto:
        dia, mes, anio = diasiguiente(dia, mes, anio)
        i += 1
    return dia, mes, anio


def main() -> None:
    anio, mes, dia = pedir_fecha()
    print(f"La fecha es: {dia}/{mes}/{anio}")
    adelanto = pedir_cuanto_adelantar()
    dia, mes, anio = calcular_fecha(adelanto, dia, mes, anio)
    print(f"{adelanto} días después: {dia}/{mes}/{anio}")


if __name__ == "__main__":
    main()
