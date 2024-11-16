"""
Resolver el siguiente problema, utilizando funciones:
Se desea llevar un registro de los socios que visitan un club cada día.
Para ello, se ingresa el número de socio de cinco dígitos hasta ingresar un cero
como fin de carga. Se solicita:
a. Informar para cada socio, cuántas veces ingresó al club. Cada socio debe
aparecer una sola vez en el informe.
b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus
ingresos. Mostrar los registros de entrada al club antes y después de
eliminarlo. Informar cuántos ingresos se eliminaron.
"""

from typing import Tuple

socios = {}


def pedir_n_socio() -> int:
    """Solicita al usuario ingresar un número de socio.

    Pre: No recibe nada.

    Post: Devuelve un número entero que representa el número de socio.
          Debe ser un número entero positivo de cinco dígitos. Si se ingresa
          0, se considera como salida. En caso de ingreso inválido, solicita
          nuevamente.

    """
    while True:
        try:
            n = int(input("Ingrese el número de socio (0 para salir: ): "))
            if ((n >= 0) and (len(str(n)) == 5)) or (n == 0):
                return n
            raise ValueError()
        except ValueError:
            print("Debe ingresar un número entero positivo de cinco dígitos.")


def add_socios() -> None:
    """Agrega o actualiza el número de socios en el registro.

    Pre: No recibe nada.

    Post: Permite al usuario ingresar números de socios. Actualiza el registro
          de socios, incrementando el conteo de ingresos para cada número de
          socio ingresado. Termina cuando se ingresa 0.

    """
    while True:
        n_socio = pedir_n_socio()
        if n_socio == 0:
            break
        (
            lambda x: (
                socios.update({x: 1})
                if x not in socios.keys()
                else socios.update({x: socios[x] + 1})
            )
        )(n_socio)
    return None


def eliminar_socio() -> Tuple[int, int]:
    """Elimina un socio del registro.

    Pre: No recibe nada.

    Post: Solicita al usuario el número de socio a eliminar. Si el socio existe,
          lo elimina del registro y devuelve una tupla con el número de socio
          eliminado y sus ingresos perdidos. Si el socio no existe, informa
          al usuario y devuelve una tupla con el número de socio y 0.

    """
    print("Eliminar socio:")
    socio_baja = pedir_n_socio()
    if socio_baja == 0:
        print("Saliendo...")
        return 0, 0
    if socio_baja in socios:
        ingresos_perdidos = socios.get(socio_baja)
        socios.pop(socio_baja)
        return socio_baja, ingresos_perdidos
    print(f"No se encontro el socio {socio_baja}.")
    return socio_baja, 0


def imprimir_socios() -> None:
    """Imprime la lista de socios y sus ingresos.

    Pre: No recibe nada.

    Post: Muestra en pantalla los números de socios y sus correspondientes
          ingresos, formateados en una tabla.

    """
    print("SOCIO\tINGRESOS")
    for n_socio, ingresos in socios.items():
        print(f"{n_socio}\t{ingresos}")
    return None


def main() -> None:
    """Función principal del programa."""
    add_socios()
    imprimir_socios()
    socio_eliminado, ingresos_perdidos = eliminar_socio()
    if socio_eliminado != 0 and ingresos_perdidos != 0:
        print(f"El socio {socio_eliminado} fue eliminado.")
        print(f"Se eliminaron: {ingresos_perdidos} ingresos.")
    imprimir_socios()
    return None


if __name__ == "__main__":
    main()

# End-of-file (EOF)
