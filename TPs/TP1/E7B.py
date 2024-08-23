"""
Escribir una función diasiguiente(dia, mes año) que reciba como parámetro una
fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros
correspondientes el día siguiente al dado. Utilizando esta función sin modificaciones
ni agregados, desarrollar programas que permitan:
b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.
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


def pedir_fecha(msj: str) -> list[int]:
    fecha = []
    texto = ["Año", "Mes", "Dia"]
    print(msj)
    for i in range(3):
        while True:
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
                                print("Mes invalido, reintentar.")
                                continue
                        case 2:  # dia
                            if comprobar_dia(num, fecha[1]):
                                fecha.append(num)
                            else:
                                print("Dia invalido, reintentar.")
                                continue
                    break
                else:
                    print("El numero ingresado debe ser positivo.")
            except ValueError:
                print("Debe ingresar un numero, reintentar.")
    return fecha


def es_bisiesto(anio: int) -> bool:
    return (anio % 4 == 0) and (anio % 100 != 0) or (anio % 400 == 0)


def comprobar_mes(mes: int) -> bool:
    return mes <= len(meses.keys())


def comprobar_dia(dia: int, mes: int) -> bool:
    return dia <= meses.get(mes)


def diasiguiente(anio: int, mes: int, dia: int) -> list[int]:
    if (dia + 1) > meses.get(mes):
        if mes != 12:
            mes += 1
            dia = 1
        else:
            anio += 1
            mes = 1
            dia = 1
    else:
        dia += 1
    return [anio, mes, dia]


def diferencia_dias(fecha: list[int], fecha2: list[int]) -> int:
    dif = 0
    si_fecha2_antigua = (fecha2[0] < fecha[0]) or (fecha2[1] < fecha[1])
    while fecha != fecha2:
        if si_fecha2_antigua:
            fecha2 = diasiguiente(fecha2[0], fecha2[1], fecha2[2])
        else:
            fecha = diasiguiente(fecha[0], fecha[1], fecha[2])
        dif += 1
    return dif


def nueva_fecha(fecha: list[int], dif_fecha: list[int]) -> list[int]:
    nueva_fecha = []
    for i in fecha:
        nueva_fecha.append(fecha[i] + dif_fecha[i])
    if not comprobar_mes(nueva_fecha[1]):
        nueva_fecha[1] -= 12
    if not comprobar_dia(nueva_fecha[2], nueva_fecha[1]):
        nueva_fecha[2] -= meses.get(nueva_fecha[1])
    return nueva_fecha


def main():
    fecha = pedir_fecha("Ingrese la primera fecha: ")
    fecha2 = pedir_fecha("Ingrese la segunda fecha: ")
    dif = diferencia_dias(fecha, fecha2)
    print(
        f"Los dias entre {fecha[0]}/{fecha[1]}/{fecha[2]} y {fecha2[0]}/{fecha2[1]}/{fecha2[2]} son {dif}."
    )


if __name__ == "__main__":
    main()
