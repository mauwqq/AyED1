"""
Escribir un programa para crear una lista por comprensión con los naipes de la
baraja española. La lista debe contener cadenas de caracteres. Ejemplo:
["1 Oros", "2 Oros"... ]. Imprimir la lista por pantalla.
"""

if __name__ == "__main__":
    palos = ["Oros", "Copas", "Espadas", "Bastos"]
    valores = list(range(1, 13))
    naipes = [f"{valor} {palo}" for palo in palos for valor in valores]
    print("\n".join(naipes))
