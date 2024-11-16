"""
Desarrollar las siguientes funciones utilizando tuplas para representar fechas y ho-
rarios, y luego escribir un programa que las vincule:
a. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha
válida.
b. Sumar N días a una fecha.
c. Ingresar un horario desde teclado, verificando que sea correcto.
d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al
segundo se considerará que el primero corresponde al día anterior. En ningún
caso la diferencia en horas puede superar las 24 horas.
"""

from typing import Tuple

months = {
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


def check_valid_date(day: int, month: int, year: int) -> bool:
    """Checks if the given date is valid.

    Pre: day, month and year are non-negative integers.

    Post: Returns True if the date is valid, otherwise False.

    """
    if check_leap(year):
        months[2] = 29
    return (month in months) and (1 <= day <= months[month])


def check_leap(year: int) -> bool:
    """Checks if the year given is a leap year or not

    Pre: year is a non-negative integer.

    Post: Returns True if the year fullfils the condition, otherwise False.

    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def input_date(msj: str) -> Tuple[int]:
    """Asks the user to enter the date.

    Pre: msj is a string.

    Post: Returns a tuple of non-negative integers.

    Raises: ValueError: if the date given does not fullfill the conditions.

    """
    while True:
        try:
            date = input(msj)
            if len(date) == 8 and date.isdigit():
                day, month, year = int(date[:2]), int(date[2:4]), int(date[4:])
                if check_valid_date(day, month, year):
                    break
            raise ValueError()
        except ValueError:
            print("Debe ingresar una fecha valida. En formato DDMMAAAA.")
    return day, month, year


def input_days(msj: str) -> int:
    """Asks the user to enter the day.

    Pre: msj is a string.

    Post: Returns the user input if its a non-negative integer.

    """
    while True:
        try:
            n = int(input(msj))
            if n >= 0:
                break
            raise ValueError()
        except ValueError:
            print("Debe ingresar un número entero no negativo.")
    return n


def next_day(day: int, month: int, year: int) -> Tuple[int]:
    """Calculate the next day of the date given.

    Pre: day, month, and year are non-negative integers.

    Post: Returns a tuple of non-negative integers.

    """
    if day < months[month]:
        day += 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
    return day, month, year


def calculate_date(forward: int, day: int, month: int, year: int) -> Tuple[int]:
    """Calculates the new date, forwarding the days the user gave.

    Pre: forward, day, month and year are non-negative integers.

    Post: Returns a tuple of non-negative integers.

    """
    for _ in range(forward):
        day, month, year = next_day(day, month, year)
    return day, month, year


def check_valid_schedule() -> Tuple[int]:
    """Checks if the schedule given by the user input is valid.

    Pre: None.

    Post: Returns a tuple of integers.

    Raises: ValueError: if schedule is invalid.

    """
    while True:
        try:
            schedule = input("Ingrese el horario en formato HH:MM: ")
            hours, minutes = map(int, schedule.split(":"))
            if 0 <= hours < 24 and 0 <= minutes < 60:
                return hours, minutes
            raise ValueError()
        except ValueError:
            print("Formato de horario incorrecto. Debe ser HH:MM.")


def calc_dif_schedules(h1: Tuple[int], h2: Tuple[int]) -> Tuple[int]:
    """Calculates the time diff between two schedules.

    Pre: h1 and h2 are tuples of non-negative integers.

    Post: Returns the time between the two schedules as a tuple of non-negative integers.

    """
    hours1, minutes1 = h1
    hours2, minutes2 = h2
    total_min1 = hours1 * 60 + minutes1
    total_min2 = hours2 * 60 + minutes2
    if total_min1 > total_min2:
        total_min1 -= 24 * 60
    dif_mins = total_min2 - total_min1
    return dif_mins // 60, dif_mins % 60


def main() -> None:
    """Main function of program."""
    date = input_date("Ingrese la fecha en formato DDMMAAAA: ")
    n_days = input_days("Cuánto desea adelantar en días: ")
    new_date = calculate_date(n_days, *date)
    print(f"La nueva fecha es: {new_date[0]}/{new_date[1]}/{new_date[2]}")
    time1 = check_valid_schedule()
    time2 = check_valid_schedule()
    time_diff = calc_dif_schedules(time1, time2)
    print(
        f"La diferencia entre los horarios es: {time_diff[0]} horas y {time_diff[1]} minutos."
    )
    return None


if __name__ == "__main__":
    main()

# End-of-file (EOF)
