from core.game import Game

class BackgammonCLI:
    def __init__(self):
        self.__game__ = None
        self.__running__ = True

    def run(self):
        print("=== BACKGAMMON ===")
        print("Comandos: nueva, tablero, tirar, mover, cambiar, salir")

        while self.__running__:
            try:
                cmd = input("\n> ")
                cmd = cmd.encode("utf-8", errors="ignore").decode("utf-8").strip().lower()
            except (UnicodeDecodeError, EOFError):
                print("Entrada inválida, intente de nuevo.")
                continue

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
        try:
            p1 = input("Jugador 1: ")
            p2 = input("Jugador 2: ")
            p1 = p1.encode("utf-8", errors="ignore").decode("utf-8").strip()
            p2 = p2.encode("utf-8", errors="ignore").decode("utf-8").strip()
        except (UnicodeDecodeError, EOFError):
            print("Error en los nombres. Intente de nuevo.")
            return

        if not p1 or not p2:
            print("Error: los nombres no pueden estar vacíos.")
            return

        self.__game__ = Game(p1, p2)
        print(f"Partida creada: {p1} (X) vs {p2} (O)")
        print(f"Comienza el turno de: {self.__game__.get_turn()}")

    def ver_tablero(self):
        if not self.__game__:
            print("Primero cree una partida con 'nueva'.")
            return

        self.__game__.__board__.print_board()
        print(f"Turno actual: {self.__game__.get_turn()}")
        if self.__game__.remaining_dice:
            print(f"Dados restantes: {self.__game__.remaining_dice}")

    def tirar_dados(self):
        if not self.__game__:
            print("Primero cree una partida con 'nueva'.")
            return

        valores = self.__game__.roll_dice()
        print("Dados:", valores)
        print(f"Turno de: {self.__game__.get_turn()}")

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

        distancia = abs(hasta - desde)
        if not self.__game__.use_die(distancia):
            print(f"No tienes un dado con valor {distancia} disponible.")
            return

        ficha = puntos[desde].pop()
        puntos[hasta].append(ficha)

        print(f"Ficha movida de {desde+1} a {hasta+1}")
        print(f"Turno actual: {self.__game__.get_turn()}")
        if self.__game__.remaining_dice:
            print(f"Dados restantes: {self.__game__.remaining_dice}")

    def cambiar_turno(self):
        if not self.__game__:
            print("Primero cree una partida con 'nueva'.")
            return

        actual = self.__game__.get_turn()
        self.__game__.switch_turn()
        nuevo = self.__game__.get_turn()
        print(f"Turno cambiado: {actual} → {nuevo}")
        print(f"Ahora juega: {nuevo}")


if __name__ == "__main__":
    cli = BackgammonCLI()
    cli.run()
