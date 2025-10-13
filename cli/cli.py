from core.game import Game

class BackgammonCLI:
    def __init__(self):
        self.__game__ = None
        self.__running__ = True

    def run(self):
        print("=== BACKGAMMON ===")
        print("Comandos: nueva, tablero, tirar, mover, cambiar, salir")

        while self.__running__:
            cmd = input("\n> ").strip().lower()

            if cmd == "nueva":
                self.nueva_partida()
            elif cmd == "tablero":
                self.ver_tablero()
            elif cmd == "tirar":
                self.tirar_dados()
            elif cmd == "mover":
                self.mover_ficha()
            elif cmd == "cambiar":
                self.cambiar_turno()
            elif cmd == "salir":
                print("Fin del juego.")
                self.__running__ = False
            else:
                print("Comando no válido.")

    def nueva_partida(self):
        print("\nNueva partida")
        p1 = input("Jugador 1: ").strip()
        p2 = input("Jugador 2: ").strip()

        if not p1 or not p2:
            print("Error: los nombres no pueden estar vacíos.")
            return

        self.__game__ = Game(p1, p2)
        print(f"Partida creada: {p1} (X) vs {p2} (O)")

    def ver_tablero(self):
        if not self.__game__:
            print("Primero cree una partida con 'nueva'.")
            return

        print("\n=== TABLERO ===")
        puntos = self.__game__.__board__.__points__
        for i, punto in enumerate(puntos):
            cantidad = len(punto)
            if cantidad == 0:
                print(f"Punto {i+1}: vacío")
            else:
                color = punto[0]
                print(f"Punto {i+1}: {cantidad} ({color})")

    def tirar_dados(self):
        if not self.__game__:
            print("Primero cree una partida con 'nueva'.")
            return

        valores = self.__game__.roll_dice()
        print("Dados:", valores)

    def mover_ficha(self):
        if not self.__game__:
            print("Primero cree una partida con 'nueva'.")
            return

        try:
            desde = int(input("Desde punto (1-24): ")) - 1
            hasta = int(input("Hacia punto (1-24): ")) - 1
        except ValueError:
            print("Error: debe ingresar números.")
            return

        puntos = self.__game__.__board__.__points__

        if desde < 0 or desde >= 24 or hasta < 0 or hasta >= 24:
            print("Movimiento fuera del rango.")
            return
        if len(puntos[desde]) == 0:
            print("No hay fichas en ese punto.")
            return

        ficha = puntos[desde].pop()
        puntos[hasta].append(ficha)

        print(f"Ficha movida de {desde+1} a {hasta+1}.")

    def cambiar_turno(self):
        if not self.__game__:
            print("Primero cree una partida con 'nueva'.")
            return

        actual = self.__game__.get_turn().get_name()
        self.__game__.switch_turn()
        nuevo = self.__game__.get_turn().get_name()
        print(f"Turno cambiado: {actual} → {nuevo}")


if __name__ == "__main__":
    cli = BackgammonCLI()
    cli.run()
