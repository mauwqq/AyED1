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

PISOS = 10
HABITACIONES_POR_PISO = 6


def registrar_huespedes(huespedes, habitaciones_ocupadas) -> None:
    """Registra el ingreso de huespedes al hotel.

    Pre: huespedes es un diccionario donde se almacenan los datos de los
         huespedes.
         habitaciones_ocupadas es un conjunto que contiene las habitaciones
         ocupadas.

    Post: Registra a los huespedes hasta que se ingrese un DNI de -1.

    """
    while True:
        dni = int(input("Ingrese el DNI del huesped (o -1 para finalizar): "))
        if dni == -1:
            break
        if dni in huespedes:
            print("El DNI ya está registrado. Intente nuevamente.")
            continue
        nombre = input("Ingrese el apellido y nombre del huesped: ")
        fecha_ingreso = input("Ingrese la fecha de ingreso (DDMMAAAA): ")
        fecha_egreso = input("Ingrese la fecha de egreso (DDMMAAAA): ")
        if not validar_fechas(fecha_ingreso, fecha_egreso):
            print(
                "La fecha de egreso debe ser mayor a la de ingreso. Intente nuevamente."
            )
            continue
        ocupantes = int(input("Ingrese la cantidad de ocupantes: "))
        piso, habitacion = asignar_habitacion(habitaciones_ocupadas)
        if piso is None:
            print("No hay habitaciones disponibles.")
            continue
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


def validar_fechas(fecha_ingreso: str, fecha_egreso: str) -> bool:
    """Valida que la fecha de egreso sea mayor que la de ingreso.

    Pre: fecha_ingreso y fecha_egreso son cadenas con el formato DDMMAAAA.

    Post: Retorna True si la fecha de egreso es mayor, False en caso contrario.

    """
    return fecha_egreso > fecha_ingreso


def asignar_habitacion(habitaciones_ocupadas: set) -> tuple[int, int]:
    """Asigna un piso y habitación disponibles al huesped.

    Pre: habitaciones_ocupadas es un conjunto que contiene las habitaciones ocupadas.

    Post: Retorna el piso y habitación disponibles, o (None, None) si no hay.

    """
    for piso in range(PISOS):
        for habitacion in range(HABITACIONES_POR_PISO):
            if (piso, habitacion) not in habitaciones_ocupadas:
                return piso, habitacion
    return None, None


def mostrar_piso_mayor_ocupacion(huespedes: dict) -> None:
    """Muestra el piso con mayor cantidad de habitaciones ocupadas.

    Pre: huespedes es un diccionario que contiene los datos de los huespedes.

    Post: Imprime el piso con más habitaciones ocupadas.

    """
    ocupacion = [0] * PISOS
    for huesped in huespedes.values():
        ocupacion[huesped["piso"]] += 1
    piso_maximo = ocupacion.index(max(ocupacion))
    print(f"Piso con mayor cantidad de habitaciones ocupadas: {piso_maximo + 1}")


def contar_habitaciones_vacias(huespedes: dict) -> int:
    """Retorna cuántas habitaciones vacías hay en todo el hotel.

    Pre: huespedes es un diccionario que contiene los datos de los huespedes.

    Post: Retorna el número de habitaciones vacías en el hotel.

    """
    total_habitaciones = PISOS * HABITACIONES_POR_PISO
    habitaciones_ocupadas = len(huespedes)
    return total_habitaciones - habitaciones_ocupadas


def mostrar_piso_mayor_personas(huespedes: dict) -> None:
    """Muestra el piso con mayor cantidad de personas.

    Pre: huespedes es un diccionario que contiene los datos de los huespedes.

    Post: Imprime el piso con la mayor cantidad de ocupantes.

    """
    personas_por_piso = [0] * PISOS
    for huesped in huespedes.values():
        personas_por_piso[huesped["piso"]] += huesped["ocupantes"]
    piso_maximo = personas_por_piso.index(max(personas_por_piso))
    print(f"Piso con mayor cantidad de personas: {piso_maximo + 1}")


def mostrar_proxima_habitacion_desocuparse(huespedes: dict, fecha_actual: str) -> None:
    """Muestra cuál será la próxima habitación en desocuparse.

    Pre: huespedes es un diccionario que contiene los datos de los huespedes.
         fecha_actual es una cadena con el formato DDMMAAAA.

    Post: Imprime las habitaciones que se desocuparán en la fecha actual.

    """
    proxima_habitacion = []
    for huesped in huespedes.values():
        if huesped["fecha_egreso"] == fecha_actual:
            proxima_habitacion.append((huesped["piso"] + 1, huesped["habitacion"] + 1))
    if proxima_habitacion:
        print("Habitaciones que se desocuparán en la fecha actual:")
        for piso, habitacion in proxima_habitacion:
            print(f"Piso {piso}, Habitación {habitacion}")
    else:
        print("No hay habitaciones que se desocupen hoy.")


def mostrar_huespedes(huespedes: dict) -> None:
    """Muestra un listado de todos los huespedes registrados, ordenado por apellido.

    Pre: huespedes es un diccionario que contiene los datos de los huespedes.

    Post: Imprime el listado de huespedes registrados.

    """
    huespedes_ordenados = sorted(
        huespedes.items(), key=lambda x: x[1]["nombre"].split()[0]
    )
    print("Listado de huespedes registrados:")
    for dni, huesped in huespedes_ordenados:
        print(
            f"DNI: {dni}, Nombre: {huesped['nombre']}, Fecha Ingreso: {huesped['fecha_ingreso']}, Fecha Egreso: {huesped['fecha_egreso']}, Ocupantes: {huesped['ocupantes']}, Piso: {huesped['piso'] + 1}, Habitación: {huesped['habitacion'] + 1}"
        )


def main() -> None:
    huespedes = {}
    habitaciones_ocupadas = set()
    registrar_huespedes(huespedes, habitaciones_ocupadas)
    mostrar_piso_mayor_ocupacion(huespedes)
    habitaciones_vacias = contar_habitaciones_vacias(huespedes)
    print(f"Total de habitaciones vacías: {habitaciones_vacias}")
    mostrar_piso_mayor_personas(huespedes)
    fecha_actual = input("Ingrese la fecha actual (DDMMAAAA): ")
    mostrar_proxima_habitacion_desocuparse(huespedes, fecha_actual)
    mostrar_huespedes(huespedes)


if __name__ == "__main__":
    main()
