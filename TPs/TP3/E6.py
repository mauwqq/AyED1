"""
6. Un hotel necesita un programa para gestionar la operación de sus habitaciones.
El hotel cuenta con 10 pisos y 6 habitaciones por piso. Por cada huésped o grupo
familiar que se aloja en el mismo se registra la siguiente información:
- DNI del cliente (número entero)
- Apellido y Nombre
- Fecha de ingreso (DDMMAAAA)
- Fecha de egreso (DDMMAAAA)
- Cantidad de ocupantes
Se solicita desarrollar un programa que utilice arreglos para realizar las
siguientes tareas:
a. Registrar el ingreso de huéspedes al hotel, hasta que se ingrese un número de
DNI igual a -1. Tener en cuenta que los números de DNI no pueden repetirse y
que la fecha de salida debe ser mayor a la de entrada. El piso y habitación son
asignados arbitrariamente, y no puede asignarse una habitación ya otorgada.
b. Finalizado el ingreso de huéspedes se solicita:
1. Mostrar el piso con mayor cantidad de habitaciones ocupadas.
2. Mostrar cuántas habitaciones vacías hay en todo el hotel.
3. Mostrar el piso con mayor cantidad de personas.
4. Mostrar cuál será la próxima habitación en desocuparse. La fecha actual se
ingresa por teclado. Mostrar todas las que correspondan.
5. Mostrar un listado de todos los huéspedes registrados en el hotel, ordenado
por apellido.
"""

from typing import Dict, Set, Tuple

PISOS = 10
HABITACIONES_POR_PISO = 6

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


def pedir_dni(huespedes: Dict) -> int:
    """Solicita el DNI del huésped y lo valida.

    Pre: No recibe nada.

    Post: Retorna el DNI como un entero. Si se ingresa -1, finaliza la solicitud.

    """
    while True:
        try:
            n = int(input("Ingrese el DNI (-1 para salir): "))
            if n == -1 or len(str(n)) == 8:
                return n
            if n in huespedes:
                print("El DNI ya está registrado. Intente nuevamente.")
            print("Ingrese un DNI valido (8 digitos)")
        except ValueError:
            print("Debe ingresar un numero.")


def pedir_fecha(msj: str) -> int:
    """Solicita una fecha al usuario y la valida.

    Pre: msj es un string que se muestra como mensaje al solicitar la fecha.

    Post: Retorna la fecha como un entero en formato DDMMAAAA si es válida.

    """
    while True:
        try:
            fecha = int(input(msj))
            if (fecha > 0) and validar_fecha(str(fecha)):
                return fecha
            print("Ingrese una fecha valida")
        except ValueError:
            print("La fecha debe ser ingresada en numeros (DDMMAAAA)")


def pedir_num(msj: str) -> int:
    """Solicita al usuario un número entero positivo y lo devuelve.

    Pre: Recibe un string, el mensaje que va a mostrar el input para
         recibir el número.

    Post: Retorna el valor ingresado si es un número entero positivo.

    """
    while True:
        try:
            n = int(input(msj))
            if n > 0:
                return n
            print("El numero debe ser positivo.")
        except ValueError:
            print("Debe ingresar un numero.")


def registrar_huespedes(huespedes: Dict, habitaciones_ocupadas: Set) -> None:
    """Registra el ingreso de huespedes al hotel.

    Pre: huespedes es un diccionario donde se almacenan los datos de los
         huespedes.
         habitaciones_ocupadas es un conjunto que contiene las habitaciones
         ocupadas.

    Post: Registra a los huespedes hasta que se ingrese un DNI de -1.

    """
    while True:
        dni = pedir_dni(huespedes)
        if dni == -1:
            break
        elif dni in huespedes:
            print("El DNI ya está registrado. Intente nuevamente.")
            continue
        nombre = input("Ingrese el apellido y nombre del huesped: ")
        while True:
            fecha_ingreso = pedir_fecha("Ingrese la fecha de ingreso (DDMMAAAA): ")
            fecha_egreso = pedir_fecha("Ingrese la fecha de egreso (DDMMAAAA): ")
            if validar_orden_fechas(str(fecha_ingreso), str(fecha_egreso)):
                break
            print(
                "La fecha de egreso debe ser mayor a la de ingreso. Intente nuevamente."
            )
        ocupantes = pedir_num("Ingrese la cantidad de ocupantes: ")
        piso, habitacion = asignar_habitacion(habitaciones_ocupadas)
        if piso is None:
            print("No hay habitaciones disponibles.")
            break
        huespedes[dni] = {
            "nombre": nombre,
            "fecha_ingreso": fecha_ingreso,
            "fecha_egreso": fecha_egreso,
            "ocupantes": ocupantes,
            "piso": piso,
            "habitacion": habitacion,
        }
        habitaciones_ocupadas.add((piso, habitacion))
        print(f"Huesped registrado en Piso {piso + 1}, Habitación {habitacion + 1}.")
    return None


def es_bisiesto(anio: int) -> bool:
    """Comprueba si un año es bisiesto.

    Pre: Recibe el año como un número entero.

    Post: Si el entero es divisible por cuatro y no es divisible
          por 100, o es divisible por 400 es bisiesto y devuelve True, si no False.

    """
    return (anio % 4 == 0) and (anio % 100 != 0) or (anio % 400 == 0)


def validar_fecha(fecha: str) -> bool:
    """Valida si la fecha dada es correcta según el formato DDMMAAAA.

    Pre: fecha debe ser un string en formato DDMMAAAA.

    Post: Retorna True si la fecha es válida, y False en caso contrario,
          considerando el número de días de cada mes y los años bisiestos.

    """
    dia = int(fecha[:2])
    mes = int(fecha[2:4])
    anio = int(fecha[4:])
    if es_bisiesto(anio):
        meses.update({2: 29})
    return (mes in meses) and (dia <= meses.get(mes))


def validar_orden_fechas(fecha_ingreso: str, fecha_egreso: str) -> bool:
    """Valida que la fecha de egreso sea mayor que la de ingreso.

    Pre: fecha_ingreso y fecha_egreso son cadenas con el formato DDMMAAAA.

    Post: Retorna True si la fecha de egreso es mayor, False en caso contrario.

    """
    dia_i, mes_i, anio_i = fecha_ingreso[:2], fecha_ingreso[2:4], fecha_ingreso[4:]
    dia_e, mes_e, anio_e = fecha_egreso[:2], fecha_egreso[2:4], fecha_egreso[4:]
    if anio_e > anio_i:
        return True
    if anio_e == anio_i:
        if mes_e > mes_i:
            return True
        if mes_e == mes_i:
            return dia_e > dia_i
    return False


def asignar_habitacion(habitaciones_ocupadas: Set) -> Tuple[int, int]:
    """Asigna un piso y habitación disponibles al huesped.

    Pre: habitaciones_ocupadas es un conjunto que contiene las habitaciones
         ocupadas.

    Post: Retorna el piso y habitación disponibles, o (None, None) si no hay.

    """
    for piso in range(PISOS):
        for habitacion in range(HABITACIONES_POR_PISO):
            if (piso, habitacion) not in habitaciones_ocupadas:
                return piso, habitacion
    return None, None


def mostrar_piso_mayor_ocupacion(huespedes: Dict) -> None:
    """Muestra el piso con mayor cantidad de habitaciones ocupadas.

    Pre: huespedes es un diccionario que contiene los datos de los huespedes.

    Post: Imprime el piso con más habitaciones ocupadas.

    """
    ocupacion = [0] * PISOS
    for huesped in huespedes.values():
        ocupacion[huesped["piso"]] += 1
    piso_maximo = ocupacion.index(max(ocupacion))
    print(f"Piso con mayor cantidad de habitaciones ocupadas: {piso_maximo + 1}")
    return None


def contar_habitaciones_vacias(huespedes: Dict) -> int:
    """Retorna cuántas habitaciones vacías hay en todo el hotel.

    Pre: huespedes es un diccionario que contiene los datos de los huespedes.

    Post: Retorna el número de habitaciones vacías en el hotel.

    """
    return (PISOS * HABITACIONES_POR_PISO) - (len(huespedes))


def mostrar_piso_mayor_personas(huespedes: Dict) -> None:
    """Muestra el piso con mayor cantidad de personas.

    Pre: huespedes es un diccionario que contiene los datos de los huespedes.

    Post: Imprime el piso con la mayor cantidad de ocupantes.

    """
    personas_por_piso = [0] * PISOS
    for huesped in huespedes.values():
        personas_por_piso[huesped["piso"]] += huesped["ocupantes"]
    piso_maximo = personas_por_piso.index(max(personas_por_piso))
    print(f"Piso con mayor cantidad de personas: {piso_maximo + 1}")
    return None


def mostrar_proxima_habitacion_desocuparse(huespedes: Dict, fecha_actual: int) -> None:
    """Muestra cuál será la próxima habitación en desocuparse.

    Pre: huespedes es un diccionario que contiene los datos de los huespedes.
         fecha_actual es un entero con el formato DDMMAAAA.

    Post: Imprime las habitaciones que se desocuparán en la fecha actual.

    """
    proxima_habitacion = []
    for huesped in huespedes.values():
        if huesped["fecha_egreso"] == fecha_actual:
            proxima_habitacion.append((huesped["piso"] + 1, huesped["habitacion"] + 1))
    if not proxima_habitacion:
        print("No hay habitaciones que se desocupen hoy.")
    else:
        print("Habitaciones que se desocuparán en la fecha actual:")
        for piso, habitacion in proxima_habitacion:
            print(f"Piso {piso}, Habitación {habitacion}")
    return None


def mostrar_huespedes(huespedes: Dict) -> None:
    """Muestra un listado de todos los huespedes registrados, ordenado por
    apellido.

    Pre: huespedes es un diccionario que contiene los datos de los huespedes.

    Post: Imprime el listado de huespedes registrados.

    """
    huespedes_ordenados = sorted(
        huespedes.items(), key=lambda x: x[1]["nombre"].split()[0]
    )
    print("Listado de huespedes registrados:")
    for dni, huesped in huespedes_ordenados:
        print(
            f"DNI: {dni}\n",
            f"Nombre: {huesped['nombre']}\n",
            f"Fecha Ingreso: {huesped['fecha_ingreso']}\n",
            f"Fecha Egreso: {huesped['fecha_egreso']}\n",
            f"Ocupantes: {huesped['ocupantes']}\n",
            f"Piso: {huesped['piso'] + 1}\n",
            f"Habitación: {huesped['habitacion'] + 1}\n",
        )
    return None


def main() -> None:
    """Función principal del programa."""
    huespedes = {}
    registrar_huespedes(huespedes, set())
    mostrar_piso_mayor_ocupacion(huespedes)
    habitaciones_vacias = contar_habitaciones_vacias(huespedes)
    print(f"Total de habitaciones vacías: {habitaciones_vacias}")
    mostrar_piso_mayor_personas(huespedes)
    fecha_actual = pedir_fecha("Ingrese la fecha actual (DDMMAAAA): ")
    mostrar_proxima_habitacion_desocuparse(huespedes, fecha_actual)
    mostrar_huespedes(huespedes)
    return None


if __name__ == "__main__":
    main()
