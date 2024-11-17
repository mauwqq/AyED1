"""
Escribir una función que reciba como parámetro una tupla conteniendo una fecha
(día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada
en formato extendido. La función debe contemplarse que el año se ingrese en dos
dígitos, los que serán interpretados según un año de corte definido dentro del
programa. Cualquier año mayor que éste se considerará del siglo pasado. Por
ejemplo, si el año de corte fuera 30, la función devuelve "12 de Octubre de 2030"
para (12,10,30). Pero si la tupla fuera (25, 12, 31) devolverá "25 de Diciembre de
1931". Si el año se ingresa en cuatro dígitos el año de corte no será tenido en
cuenta. Escribir también un programa para ingresar los datos, invocar a la función y
mostrar el resultado.
"""

months = {
    1: (31, "Enero"),
    2: (28, "Febrero"),
    3: (31, "Marzo"),
    4: (30, "Abril"),
    5: (31, "Mayo"),
    6: (30, "Junio"),
    7: (31, "Julio"),
    8: (31, "Agosto"),
    9: (30, "Septiembre"),
    10: (31, "Octubre"),
    11: (30, "Noviembre"),
    12: (31, "Diciembre"),
}


def input_date(msg: str) -> str:
    """
    Asks for a date in DDMMAAAA or DDMMAA format and returns it as a string.

    Pre: msg is a string.

    Post: Returns a string.

    Raises: ValueError: if the date is not numeric or not in the correct format.

    """
    while True:
        try:
            date = input(msg)
            if len(date) in [6, 8] and date.isdigit():
                return date
            raise ValueError(
                "Debe ingresar una fecha válida en formato DDMMAAAA o DDMMAA."
            )
        except ValueError as e:
            print(e)


def valid_date(day: int, month: int, year: int) -> bool:
    """
    Checks if the input date is valid considering the days of each month and leap years.

    Pre: day, month, year are non-negative integers.

    Post: True if the date is valid, otherwise False.

    """

    if month == 2 and (not (year % 4) and (year % 100 != 0)) or not (year % 400):
        return day <= 29
    return (month in months) and (day <= months[month][0])


def convert_date(date: str, cut: int = 30) -> str:
    """Converts a date in extended format and returns it.

    Pre: date is a string.
         cut is a non-negative integer.

    Post: returns a string.

    """
    day, month, year = int(date[:2]), int(date[2:4]), int(date[4:])
    if len(date) == 6:
        year += 2000 if year <= cut else 1900
    if not valid_date(day, month, year):
        raise ValueError("La fecha ingresada no es válida.")
    return f"{day} de {months[month][1]} de {year}"


def main() -> None:
    """Main function of program."""
    date = input_date("Ingrese una fecha en formato DDMMAAAA o DDMMAA: ")
    try:
        conv_date = convert_date(date)
        print(f"Fecha en formato extendido: {conv_date}")
    except ValueError as e:
        print(e)
    return None


if __name__ == "__main__":
    main()

# End-of-file (EOF)
