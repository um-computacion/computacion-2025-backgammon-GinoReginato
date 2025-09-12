class Player:
    def __init__(self, name, color):
        self.__name__ = name
        self.__color__ = color
        self.__checkers__ = 15

    def get_name(self):
        return self.__name__

    def get_color(self):
        return self.__color__

    def get_checkers(self):
        return self.__checkers__

    def remove_checker(self):
        if self.__checkers__ > 0:
            self.__checkers__ -= 1

    def add_checker(self):
        self.__checkers__ += 1
