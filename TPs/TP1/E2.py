"""
Desarrollar una función que reciba tres números enteros positivos correspondientes
al día, mes, año de una fecha y verifique si corresponden a una fecha válida. Debe
tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos.
Devolver True o False según la fecha sea correcta o no. Realizar también un
programa para verificar el comportamiento de la función.
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


def es_positivo(numero: int) -> bool:
    return numero > 0


def recibir_numeros() -> list[int]:
    """Pide tres numeros enteros positivos, los guarda en una lista y devuelve la lista
    post -> devuelve una lista de tres enteros que corresponden
            a el dia, mes y año solicitado.
    """
    fecha = []  # dia, mes, año
    texto = ["Dia", "Mes", "Año"]
    print("Ingrese la fecha en el formato indicado.")
    for i in range(3):
        while True:
            try:
                num = int(input(f"{texto[i]}: "))
                if es_positivo(num):
                    fecha.append(num)
                    break
                print("El numero no es positivo. Reintentar.")
            except ValueError:
                print("Ingrese un numero valido.")
    return fecha


def es_bisiesto(anio: int) -> bool:
    """Comprueba si un año es bisiesto.
    Pre -> recibe un numero entero.
    Post -> si el entero es divisible por cuatro y no es divisible
            por 100 o es divisible por 400 devuelve True, sino False.
    """
    return (anio % 4 == 0) and (anio % 100 != 0) or (anio % 400 == 0)


def validar_fecha(dia: int, mes: int, anio: int) -> bool:
    """Recibe tres parametros enteros y devuelve True si la fecha es valida.
    Pre -> recibe tres parametros enteros positivos.
    Post -> devuelve True si la fecha es valida, false si no lo es.
    """
    if es_bisiesto(anio):
        meses.update({2: 29})
    return (mes <= len(meses.keys())) and (dia <= meses.get(mes))


def main() -> None:
    dia, mes, anio = recibir_numeros()
    if validar_fecha(dia, mes, anio):
        print("La fecha es valida.")
    else:
        print("La fecha no es valida.")


if __name__ == "__main__":
    main()
