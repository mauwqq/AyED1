"""
Desarrollar una función que devuelva una cadena de caracteres con el nombre del
mes cuyo número se recibe como parámetro. Los nombres de los meses deberán
obtenerse de una lista de cadenas de caracteres inicializada dentro de la función.
Devolver una cadena vacía si el número de mes es inválido. La detección de meses
inválidos deberá realizarse a través de excepciones.
"""


def pedir_numero() -> int:
    """Solicita al usuario el numero de mes que desea buscar en la lista.

    Pre: No recibe nada.

    Post: Retorna un número entero positivo que representa el numero de mes.
          Si el usuario ingresa un valor no válido, vuelve a solicitarlo.

    """
    while True:
        try:
            n = int(input("Ingrese el numero de mes: "))
            if n > 0:
                break
            raise ValueError()
        except ValueError:
            print("Debe ingresar un número entero positivo.")
    return n


def nombre_mes(n: int) -> str:
    """Devuelve el nombre del mes correspondiente al número ingresado.

    Pre: n debe ser un entero que representa el número del mes (1-12).

    Post: Retorna el nombre del mes correspondiente al número ingresado.
          Si el número está fuera del rango válido, retorna una cadena vacía
          y muestra un mensaje de error.

    """
    meses = [
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre",
    ]
    try:
        return meses[n]
    except IndexError:
        print("El numero de mes ingresado es invalido.")
        return ""


def main() -> None:
    """Función principal del programa."""
    n = pedir_numero()
    nombre = nombre_mes(n - 1)
    if nombre:
        print(f"El mes {n} es {nombre}.")
    else:
        print("No hay ningun mes para ese numero.")


if __name__ == "__main__":
    main()
