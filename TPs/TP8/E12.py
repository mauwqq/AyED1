"""
Una librería almacena su lista de precios en un diccionario. Diseñar un programa
para crearlo, incrementar los precios de los cuadernos en un 15%, imprimir un
listado con todos los elementos de la lista de precios e indicar cuál es el ítem más
costoso que venden en el comercio.
"""

op = (
    "Añadir libro",
    "Incrementar precios en un 15%",
    "Imprimir precios",
    "Libro mas caro",
    "Salir",
)
books = {}


def display_menu() -> None:
    """Displays the menu options.

    Pre: None.

    Post: None.

    """
    print(f"{"="*15}MENU{"="*15}")
    for i, choice in enumerate(op):
        print(f"{i+1}. {choice}.")
    print(f"{"="*34}")
    return None


def input_num(msj: str) -> float:
    """Requests a number from the user, then cast it to float and returns it.

    Pre: msj is a string.

    Post Returns a float.

    Raises: ValueError: if the number cant be casted to float.

    """
    while True:
        try:
            return float(input(msj))
        except ValueError:
            print("Por favor ingrese un número válido.")


def menu() -> None:
    """Asks the user to enter an option of the menu, then redirects them to
    the chosen option.

    Pre: None.

    Post: None.

    """
    while True:
        display_menu()
        op = input_num("Seleccione una opcion: ")
        match op:
            case 1:
                add_book()
            case 2:
                increment_prices()
            case 3:
                print_prices()
            case 4:
                pass
            case 5:
                print("Saliendo...")
                break
            case _:
                print("Seleccione una opcion correcta.")
    return None


def input_name(msj: str) -> str:
    """Asks for user input.

    Pre: msj is a string.

    Post: Returns a string

    """
    return input(msj)


def add_book() -> None:
    """Adds a book to the dictionary.

    Pre: None.

    Post: None.

    """
    name = input_name("Ingrese el nombre del libro: ")
    price = input_num("Ingrese el precio del libro: ")
    books[name] = price
    print(f"Libro '{name}' añadido con precio {price}.")
    return None


def increment_prices() -> None:
    """Increments 15% the prices of notebooks.

    Pre: None.

    Post: None.

    """
    if not books:
        print("No hay libros registrados.")
    else:
        for name, price in books.items():
            if "cuaderno" in name.lower():
                books[name] = price * 1.15
        print("Precios de los cuadernos incrementados en un 15%.")
    return None


def print_prices() -> None:
    """Prints the book's names and prices.

    Pre: None.

    Post: None.

    """
    if not books:
        print("No hay libros registrados.")
    else:
        for name, price in books.items():
            print(f"{name}\t{price}")
    return None


def most_expensive() -> None:
    """Gets and prints the most expensive book of the dictionary.

    Pre: None.

    Post: None.

    """
    if not books:
        print("No hay libros registrados.")
    else:
        expensive = max(books, key=books.get)
        print(
            f"El libro más caro es '{most_expensive}' con un precio de ${books[most_expensive]:.2f}."
        )
    return None


def main() -> None:
    """Main function of program"""
    menu()
    return None


if __name__ == "__main__":
    main()

# End-of-file (EOF)
