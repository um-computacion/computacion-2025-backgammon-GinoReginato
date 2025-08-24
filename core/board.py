class Board:
    def __init__(self):

        self.__points__ = [[] for _ in range(24)]
        self.setup_board()

    def setup_board(self):
        # Configuración inicial simple del tablero 
        self.__points__[0] = [1, 1]       # 2 fichas en punto 1
        self.__points__[11] = [1]*5       # 5 fichas en punto 12
        self.__points__[16] = [1]*3       # 3 fichas en punto 17
        self.__points__[18] = [1]*5       # 5 fichas en punto 19

    def print_board(self):
        for i, point in enumerate(self.__points__):
            print(f"Punto {i+1}: {len(point)} fichas")

if __name__ == "__main__":
    board = Board()
    board.print_board()
