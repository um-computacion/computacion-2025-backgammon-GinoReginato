class Board:
    RED = "\033[91m"
    BLUE = "\033[94m"
    RESET = "\033[0m"

    def __init__(self):
        self.__points__ = [[] for _ in range(24)]
        self.setup_initial_positions()

    def setup_initial_positions(self):
        self.__points__[0] = ['X'] * 2
        self.__points__[11] = ['X'] * 5
        self.__points__[16] = ['O'] * 3
        self.__points__[18] = ['O'] * 5

    def get_points(self):
        return self.__points__

    def print_board(self):
        print("\n=== TABLERO ===")

        def ficha_color(ficha):
            if ficha == 'X':
                return self.RED + ficha + self.RESET
            elif ficha == 'O':
                return self.BLUE + ficha + self.RESET
            else:
                return ' '

        points = self.__points__
        top_points = points[12:24]
        bottom_points = points[0:12]
        top_height = max(len(p) for p in top_points)
        bottom_height = max(len(p) for p in bottom_points)

        # Arriba: puntos 13 a 24
        for nivel in range(top_height, 0, -1):
            fila = ""
            for p in top_points:
                if len(p) >= nivel:
                    fila += f" {ficha_color(p[nivel-1])} "
                else:
                    fila += " ▲ "
            print(fila)
        print(" ".join([f"{i+13:2}" for i in range(12)]))
        print("-" * 50)

        # Abajo: puntos 12 a 1
        for nivel in range(bottom_height, 0, -1):
            fila = ""
            for p in reversed(bottom_points):
                if len(p) >= nivel:
                    fila += f" {ficha_color(p[nivel-1])} "
                else:
                    fila += " ▼ "
            print(fila)
        print(" ".join([f"{i+1:2}" for i in range(12)]))
