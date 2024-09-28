"""
Resolver el siguiente problema, diseñando las funciones a utilizar:
Una clínica necesita un programa para atender a sus pacientes. Cada paciente
que ingresa se anuncia en la recepción indicando su número de afiliado
(número entero de 4 dígitos) y además indica si viene por una urgencia
(ingresando un 0) o con turno (ingresando un 1). Para finalizar se ingresa -1
como número de socio. Luego se solicita:
*a. Mostrar un listado de los pacientes atendidos por urgencia y un listado de
los pacientes atendidos por turno en el orden que llegaron a la clínica.
*b. Realizar la búsqueda de un número de afiliado e informar cuántas veces fue
atendido por turno y cuántas por urgencia. Repetir esta búsqueda hasta
que se ingrese -1 como número de afiliado.
"""

# clinica = [[num_afiliado, urgencia]]
clinica = []


def validar_afiliado(n: int) -> bool:
    """Valida si el afiliado tiene 4 números y es positivo.

    Pre: Recibe un número entero "n".

    Post: Devuelve "True" si "n" tiene 4 dígitos y es positivo.
          Sino devuelve "False".

    """
    return (len(str(n)) == 4) and (n > 0)


def validar_menu(n: int) -> bool:
    """Valida si la opción del menú está dentro del rango permitido.

    Pre: Recibe un número entero "n".

    Post: Devuelve "True" si "n" es una opción válida del menú (0 a 3).
          Sino devuelve "False".

    """
    return n >= 0 and n <= 3


def validar_urgencia(n: int) -> bool:
    """Valida si el valor de urgencia es válido.

    Pre: Recibe un número entero "n".

    Post: Devuelve "True" si "n" es 0 o 1.
          Sino, devuelve "False".

    """
    return n >= 0 and n < 2


def urgencia(n: int) -> str:
    """Devuelve un string que indica si el paciente es urgente.

    Pre: Recibe un número entero "n" que representa la urgencia.

    Post: Devuelve "Si" si "n" es 1.
          Sino devuelve "No".

    """
    return "Si" if n == 1 else "No"


def opciones() -> None:
    """Muestra las opciones del menú.

    Pre: No recibe nada.

    Post: Imprime las opciones disponibles para el usuario.

    """
    print(
        "\n 1- Ingresar pacientes.\n",
        "2- Lista de pacientes.\n",
        "3- Buscar paciente por número de afiliado.\n",
        "0- Salir.\n",
    )
    return None


def pedir_numero(msj: str, long: int) -> int:
    """Solicita un número al usuario según el tipo requerido.

    Pre: Recibe un mensaje "msj" y un entero "long" que indica el tipo de número
         a pedir.

    Post: Devuelve un número entero que cumple con las validaciones según el
          tipo.

    """
    while True:
        try:
            n = int(input(msj))
            match long:
                case 1:  # Pedir número de urgencia
                    if validar_urgencia(n):
                        return n
                    print("Ingrese una opción válida.")
                case 2:  # Pedir opcion del menu
                    if validar_menu(n):
                        return n
                    print("Ingrese una opción válida.")
                case 3:  # pedir número de afiliado
                    if validar_afiliado(n) or (n == -1):
                        return n
                    print("Ingrese un numero válido.")
        except ValueError:
            print("Debe ingresar un número.")


def pedir_paciente() -> None:
    """Solicita la información de pacientes y la agrega a la clínica.

    Pre: No recibe nada.

    Post: Agrega pacientes a la lista "clinica" según la información
          proporcionada por el usuario.

    """
    while True:
        afiliado = pedir_numero("Ingrese el número de afiliado (-1 para salir): ", 3)
        if afiliado == -1:
            break
        urgencia = pedir_numero("Ingrese 1 si es urgente o 0 si no lo es: ", 1)
        paciente = [afiliado, urgencia]
        clinica.append(paciente)
    return None


def listado_pacientes() -> None:
    """Imprime la lista de pacientes registrados.

    Pre: No recibe nada.

    Post: Imprime los pacientes y su nivel de urgencia si hay pacientes registrados.
          Sino, informa que no hay pacientes.

    """
    if not clinica:
        print("No hay pacientes registrados.")
    else:
        print("Paciente\tUrgencia")
        for paciente in clinica:
            print(f"{paciente[0]}\t\t{urgencia(paciente[1])}")
    return None


def buscar_paciente() -> None:
    """Busca un paciente por su número de afiliado.

    Pre: No recibe nada.

    Post: Imprime la cantidad de turnos y urgencias del paciente buscado.
          Si no se encuentra, informa al usuario.

    """
    while True:
        afiliado = pedir_numero(
            "Ingrese el afiliado que desea buscar(-1 para salir): ", 3
        )
        if afiliado == -1:
            break
        turno = 0
        urgencia = 0
        for paciente in clinica:
            if afiliado in paciente[:1]:
                if paciente[1] == 0:
                    turno += 1
                else:
                    urgencia += 1
        if not turno and not urgencia:
            print("No se encontró el paciente.")
        else:
            print(
                f"Paciente {afiliado}:\n",
                f"Turno: {turno}\n",
                f"Urgencia: {urgencia}",
            )
    return None


def menu() -> None:
    """Función principal que muestra el menú y maneja las opciones del usuario.

    Pre: No recibe nada.

    Post: Permite al usuario interactuar con el sistema de gestión de pacientes
          hasta que decida salir.

    """
    while True:
        opciones()
        op = pedir_numero("Ingrese una opción: ", 2)
        match op:
            case 1:
                pedir_paciente()
            case 2:
                listado_pacientes()
            case 3:
                buscar_paciente()
            case 0:
                print("Saliendo...")
                break
    return None


def main() -> None:
    """Función principal del programa."""
    menu()
    return None


if __name__ == "__main__":
    main()
