"""
Se dispone de tres formatos diferentes de archivos de texto en los que se almace-
nan datos de empleados, detallados más abajo. Desarrollar un programa para cada
uno de los formatos suministrados, que permitan leer cada uno de los archivos y
grabar los datos obtenidos en otro archivo de texto con formato CSV.
"""


def type1(path: str, output: str) -> None:
    """Opens a file formatted by a static lengh, formats it into a csv and writes
    the output into a file.

    Pre: file and output are strings.

    Post: Returns None.

    Raises: FileNotFoundError: file was not found on the path given.
            IsADirectoryError: The path is a folder, not a file.
            PermissionError, OSError: The scripts doesn't have
            sufficient permissions to open/write into the file.

    """
    try:
        with open(path, "r", encoding="utf-8") as a, open(
            output, "w", encoding="utf-8"
        ) as b:
            data = a.readlines()
            for line in data:
                b.write(
                    f"{line[:17].strip()},{line[17:28].strip()},{line[28:].strip()}\n"
                )
        print("Archivo 1 actualizado correctamente.")
    except FileNotFoundError:
        print("No se encontro el archivo.")
    except IsADirectoryError:
        print("La ruta suministrada es un directorio.")
    except (PermissionError, OSError) as e:
        print(f"Error: {e}")
    finally:
        return None


def type2(path: str, output: str) -> str:
    """Opens a file with a specified formatting and writes the content in a
    csv output file.

    Pre: path and output are strings.

    Post: Returns None.

        Raises: FileNotFoundError: file was not found on the path given.
            IsADirectoryError: The path is a folder, not a file.
            PermissionError, OSError: The scripts doesn't have
            sufficient permissions to open/write into the file.

    """
    try:
        with open(path, "r", encoding="utf-8") as a, open(
            output, "w", encoding="utf-8"
        ) as b:
            data = a.readlines()
            for line in data:
                line = line.strip()
                ini = 0
                data = []
                lengh = int(line[ini : ini + 2])
                for i in range(3):
                    field = line[ini + 2 : ini + lengh + 2]
                    ini += lengh + 2
                    data.append(field)
                    if i == 2:
                        break
                    lengh = int(line[ini : ini + 2])
                b.write(f'{",".join(data)}\n')
        print("Archivo 2 actualizado correctamente.")
    except FileNotFoundError:
        print("No se encontro el archivo.")
    except IsADirectoryError:
        print("La ruta suministrada es un directorio.")
    except (PermissionError, OSError) as e:
        print(f"Error: {e}")
    finally:
        return None


def main() -> None:
    """Main function of program."""
    type1("archivo1.txt", "output_1.txt")
    type2("archivo2.txt", "output_2.txt")
    return None


if __name__ == "__main__":
    main()
