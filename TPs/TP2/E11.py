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


def validar_afiliado(n):
    """Valida si el afiliado tiene 4 numeros y es positivo."""
    return (n // 1000 != 0) and (n > 0)


def validar_menu(n):
    return n >= 0 and n <= 3


def validar_urgencia(n):
    return n >= 0 and n < 2


def urgencia(n):
    return "Si" if n == 1 else "No"


def opciones() -> None:
    print(
        "\n 1- Ingresar pacientes.\n",
        "2- Lista de pacientes.\n",
        "3- Buscar paciente por numero de afiliado.\n",
        "0- Salir.\n",
    )
    return None


def pedir_numero(msj: str, long: int) -> int:
    while True:
        try:
            n = int(input(msj))
            match long:
                case 1:  # Pedir numero de urgencia
                    if validar_urgencia(n):
                        return n
                    print("Ingrese una opcion valida.")
                case 2:  # Pedir opcion del menu
                    if validar_menu(n):
                        return n
                    print("Ingrese una opcion valida.")
                case 3:  # pedir numero de afiliado
                    if validar_afiliado(n) or (n == -1):
                        return n
                    print("Ingrese un numero valido.")
        except ValueError:
            print("Debe ingresar un numero.")


def pedir_paciente() -> None:
    while True:
        afiliado = pedir_numero("Ingrese el numero de afiliado(-1 para salir): ", 3)
        if afiliado == -1:
            break
        urgencia = pedir_numero("Ingrese 1 si es urgente o 0 si no lo es: ", 1)
        paciente = [afiliado, urgencia]
        clinica.append(paciente)
    return None


def listado_pacientes() -> None:
    if not clinica:
        print("No hay pacientes registrados.")
    else:
        print("Paciente\tUrgencia")
        for paciente in clinica:
            print(f"{paciente[0]}\t\t{urgencia(paciente[1])}")


def buscar_paciente() -> None:
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
            print("No se encontro el paciente.")
        else:
            print(
                f"Paciente {afiliado}:\n",
                f"Turno: {turno}\n",
                f"Urgencia: {urgencia}",
            )


def menu() -> None:
    while True:
        opciones()
        op = pedir_numero("Ingrese una opcion: ", 2)
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
    menu()


if __name__ == "__main__":
    main()
